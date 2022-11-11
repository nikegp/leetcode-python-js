import os
from itertools import combinations
from time import time

import keras
import nltk
import numpy as np
from keras.callbacks import EarlyStopping
from keras.layers import Dense, Embedding, Flatten
from keras.models import Sequential
from keras.models import model_from_json
from keras.preprocessing.text import Tokenizer
from keras_preprocessing.text import tokenizer_from_json
from nltk.stem.lancaster import LancasterStemmer

from services.autoresponses import K
from services.core import redis_long, obfuscated_service, app
from services.core.exceptions import (
    ValidationServiceException,
    ModelNotFoundServiceException,
    ModelSaveServiceException,
    NoAutoresponsesNetworkException,
)
from services.utils import generate_id, load_blacklist, Script
from .labelencoder import LabelEncoder

stemmer = LancasterStemmer()

np.set_printoptions(threshold=np.inf)

_CACHED_MODELS = {}


class AutoresponsesNeuralModel(object):
    batch_size = 20
    epochs = 200
    max_words = 1024
    max_first_layer_size = 2048
    _black_words = None
    dummy_autoresponse_id = "dummyautoresponseid"
    cache_ttl = 300
    max_cached_items = 100

    def __init__(self, bot_id):
        self.bot_id = bot_id
        self.model = None
        self.x_tokenizer = None
        self.label_encoder = None
        self.network_id = None

    @property
    def s3_bucket(self):
        return obfuscated_service.aws_prefix + "obfuscatedserviceneuralnetworks"

    def generate_id(self):
        return "{}_{}_{}".format(self.bot_id, int(time() * 1000), generate_id())

    @property
    def black_words(self):
        if self._black_words is None:
            self._black_words = load_blacklist()

        return self._black_words

    @property
    def redis_config_key(self):
        if not self.network_id:
            raise ValidationServiceException(
                "Network ID is empty. Train or load your network first"
            )
        return K.bot_nn_config(self.bot_id, self.network_id, "autoresponses")

    def weights_filepath(self, network_id=None):
        id = network_id or self.network_id
        if not id:
            raise ValueError("Network ID can't be empty")

        return "{}/weights_{}.h5".format(app.config["OBFUSCATED_SERVICES_CACHE"], id)

    def _stem_message(self, msg):
        words = nltk.word_tokenize(msg)
        words = [
            stemmer.stem(word)
            for word in words
            if len(word) >= 3 and word not in self.black_words
        ]
        return " ".join(words), len(words)

    @staticmethod
    def validate_data(data):
        if not isinstance(data, dict):
            raise ValidationServiceException("Data must be a dict")

        for key, value in data.iteritems():
            if not isinstance(key, basestring):
                raise ValidationServiceException(
                    'Group name "{}" must be a string'.format(key)
                )

            if not isinstance(value, list):
                raise ValidationServiceException(
                    "Each group must contain a list of items", invalid_group_name=key
                )

            for v in value:
                if not isinstance(v, basestring):
                    raise ValidationServiceException(
                        "Each group item must be a string",
                        invalid_group_name=key,
                        invalid_item=v,
                    )

    def add_meaningful_messages(self, messages):
        words = set()
        for msg in messages:
            words.update(nltk.word_tokenize(msg.lower()))

        words = words - self.black_words

        if not words:
            return []

        words = list(words)
        extra_messages = []

        for start, end in combinations(range(len(words)), 2):
            extra_messages.append(" ".join(words[start : end + 1]))

        return messages + extra_messages

    def stress_nouns(self, messages):
        nouns = set()

        def is_noun(pos):
            return pos[:2] == "NN"

        for msg in messages:
            tokenized = nltk.word_tokenize(msg)
            for (word, pos) in nltk.pos_tag(tokenized):
                if is_noun(pos):
                    nouns.add(word)

        nouns = nouns - self.black_words

        if not nouns:
            return messages

        nouns = list(nouns)
        extra_messages = []

        for start, end in combinations(range(len(nouns)), 2):
            extra_messages.append(" ".join(nouns[start : end + 1]))

        return messages + extra_messages

    def transform_data(self, data):
        result = {"messages": [], "groups": []}
        for group, msgs in data.iteritems():
            msgs = [msg.lower() for msg in msgs]
            for msg in msgs:
                stemmed = self._stem_message(msg)
                if not stemmed[0]:
                    continue
                result["messages"].append(stemmed[0])
                result["groups"].append(group)

        if len(set(result["groups"])) == 1:
            result["messages"].append(self.dummy_autoresponse_id)
            result["groups"].append(self.dummy_autoresponse_id)

        return result

    def get_latest_active_network_id(self):
        return redis_long.get(K.bot_active_autoresponse_nn_id(self.bot_id))

    def build_model(self, used_words_cnt, num_classes):
        type = "embedding"

        model = Sequential()
        if type == "mlp":
            layer_size = min(used_words_cnt * 4, self.max_first_layer_size)
            model.add(
                Dense(layer_size, activation="tanh", input_shape=(used_words_cnt,))
            )
            model.add(Dense(num_classes, activation="softmax"))

        if type == "embedding":
            model.add(Embedding(used_words_cnt, 8, input_length=used_words_cnt))
            model.add(Flatten())
            model.add(Dense(num_classes * 2, activation="tanh"))
            model.add(Dense(num_classes, activation="softmax"))

        return model

    def train(self, data):
        self.validate_data(data)
        data = self.transform_data(data)

        if not data["messages"]:
            return False

        self.network_id = self.generate_id()

        x_tokenizer = Tokenizer()
        x_tokenizer.fit_on_texts(data["messages"])

        total_unique_words = len(x_tokenizer.word_counts)
        used_words_cnt = min(total_unique_words, self.max_words)

        x_tokenizer = Tokenizer(used_words_cnt + 1)
        x_tokenizer.fit_on_texts(data["messages"])

        x_train = x_tokenizer.texts_to_matrix(data["messages"], mode="binary")
        encoder = LabelEncoder(data["groups"])
        y_train_encoded = encoder.transform(data["groups"])
        num_classes = encoder.labels_cnt
        y_train = keras.utils.to_categorical(y_train_encoded, num_classes)

        model = self.build_model(used_words_cnt + 1, num_classes)

        model.compile(
            loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"]
        )

        model.summary()

        model.fit(
            x_train,
            y_train,
            batch_size=self.batch_size,
            epochs=self.epochs,
            verbose=0,
            callbacks=[
                EarlyStopping(monitor="loss", patience=5, verbose=1, min_delta=0.001)
            ],
        )

        self.model = model
        self.x_tokenizer = x_tokenizer
        self.label_encoder = encoder

        return True

    def save_model_weights(self):
        self.model.save_weights(self.weights_filepath())
        return obfuscated_service.upload_file(
            open(self.weights_filepath(), "rb"),
            "application/octet-stream",
            self.network_id,
            self.s3_bucket,
        )

    def save(self):
        if not self.network_id:
            raise ValidationServiceException(
                "Network ID is empty. Train or load your network first"
            )

        if not self.model:
            raise ValidationServiceException(
                "Model is empty, you need to train it first"
            )

        if not self.x_tokenizer:
            raise ValidationServiceException(
                "Tokenizer is empty. Did you train your network?"
            )

        if not self.label_encoder:
            raise ValidationServiceException(
                "Label encoder is empty. Did you train your network?"
            )

        self.save_model_weights()

        config = {
            "model": self.model.to_json(),
            "x_tokenizer": self.x_tokenizer.to_json(),
            "label_encoder": self.label_encoder.to_json(),
        }

        redis_long.hmset(self.redis_config_key, config)

        _activation_script = Script(
            """
                            local latest_active_network_key = unpack(KEYS)
                            local network_id, network_id_ts = unpack(ARGV)

                            local function mysplit(inputstr, sep)
                                if sep == nil then
                                        sep = "%s"
                                end
                                local t={}
                                local i=1
                                for str in string.gmatch(inputstr, "([^"..sep.."]+)") do
                                        t[i] = str
                                        i = i + 1
                                end
                                return t
                            end

                            local active_network_id = redis.call('get', latest_active_network_key)
                            if active_network_id then
                                local pieces = mysplit(active_network_id, "_")
                                if pieces[2] > network_id_ts then
                                    return -1
                                end
                            end

                            redis.call('set', latest_active_network_key, network_id)

                            return active_network_id
                            """
        )

        old_network_id = _activation_script(
            client=redis_long,
            keys=[K.bot_active_autoresponse_nn_id(self.bot_id)],
            args=[self.network_id, self.network_id.split("_")[1]],
        )

        if old_network_id == -1:
            self.delete(self.network_id)
            raise ModelSaveServiceException(
                "The model can't be saved. A newer version is already active"
            )

        self.cache()

        return old_network_id, self.network_id

    def _deactivate(self, network_id):
        _deactivate_script = Script(
            """
                            local latest_active_network_key = unpack(KEYS)
                            local network_id = unpack(ARGV)

                            local active_network_id = redis.call('get', latest_active_network_key)

                            if not active_network_id and not network_id then
                                return 123
                            end

                            if network_id == 'None' or network_id == '' then
                                network_id = active_network_id
                            end

                            if active_network_id == network_id then
                                redis.call('del', latest_active_network_key)
                            end

                            return network_id
                            """
        )

        network_id = _deactivate_script(
            client=redis_long,
            keys=[K.bot_active_autoresponse_nn_id(self.bot_id)],
            args=[network_id],
        )

        return network_id

    def delete(self, network_id=None):
        network_id = self._deactivate(network_id)

        if not network_id:
            raise ValidationServiceException(
                "No autoresponse network found for the bot or network ID is empty",
                network_id=network_id,
            )

        self.network_id = network_id

        redis_long.delete(self.redis_config_key)

        self._clear_cache()
        self._remove_from_s3()

        return network_id

    def _clear_cache(self, network_id=None):
        try:
            os.remove(self.weights_filepath(network_id))
        except OSError:
            pass

        _CACHED_MODELS.pop(network_id or self.network_id, False)

    def _remove_from_s3(self):
        obfuscated_service.delete_s3_object(self.network_id, self.s3_bucket)

    def load_model_weights(self):
        try:
            self.model.load_weights(self.weights_filepath())
            return
        except Exception:
            pass

        try:
            obfuscated_service.download_file_and_save(
                self.network_id, self.s3_bucket, self.weights_filepath(), flush=True
            )
            self.model.load_weights(self.weights_filepath())
            return
        except Exception as e:
            pass

        raise ModelNotFoundServiceException(
            'Requested model "{}" can\'t be loaded. {}'.format(
                self.network_id, e.message
            )
        )

    def load_cached(self):
        cached = _CACHED_MODELS.get(self.network_id)
        if cached:
            self.model = cached["model"]
            self.x_tokenizer = cached["x_tokenizer"]
            self.label_encoder = cached["label_encoder"]
            return True

        return False

    def cache(self):
        def get_network_params(network_id):
            pieces = network_id.split("_")
            return pieces[0], int(pieces[1])

        bot_id, network_ts = get_network_params(self.network_id)
        now = time()

        oldest_cached_model = None

        # drop outdated versions of the NN for the bot and expired ones
        for n_id in _CACHED_MODELS.keys():
            b_id, n_ts = get_network_params(n_id)
            if b_id == bot_id and n_ts < network_ts:
                self._clear_cache(n_id)
                continue

            item = _CACHED_MODELS[n_id]

            if now - item["added_ts"] > self.cache_ttl:
                self._clear_cache(n_id)
                continue

            if (
                not oldest_cached_model
                or oldest_cached_model["added_ts"] > item["added_ts"]
            ):
                oldest_cached_model = item

        if len(_CACHED_MODELS) >= self.max_cached_items:
            self._clear_cache(oldest_cached_model["network_id"])

        item = {
            "network_id": self.network_id,
            "added_ts": now,
            "model": self.model,
            "x_tokenizer": self.x_tokenizer,
            "label_encoder": self.label_encoder,
        }

        _CACHED_MODELS[self.network_id] = item

    def load(self, network_id=None):
        if not network_id:
            network_id = self.get_latest_active_network_id()

        if not network_id:
            raise NoAutoresponsesNetworkException(
                "No autoresponse network found", network_id=network_id
            )

        self.network_id = network_id

        cached = self.load_cached()
        if cached:
            return

        config = redis_long.hgetall(self.redis_config_key)

        if not config:
            return

        self.model = model_from_json(config["model"])
        self.x_tokenizer = tokenizer_from_json(config["x_tokenizer"])
        self.label_encoder = LabelEncoder.load_from_json(config["label_encoder"])

        self.load_model_weights()

        self.cache()

    def classify(self, msg):
        if not self.model:
            self.load()

        if not self.model:
            return []

        msg, length = self._stem_message(msg)

        if msg == self.dummy_autoresponse_id:
            return []

        tokenized = self.x_tokenizer.texts_to_matrix([msg], mode="binary")

        if not any(tokenized[0]):
            return []

        result = self.model.predict(np.array(tokenized))[0]

        return result

    def classify_autoresponse_id(self, msg):
        if not self.label_encoder:
            self.load()

        if not self.label_encoder:
            return None

        chances = self.classify(msg)
        autoresponse_id = None

        for i, chance in enumerate(chances):
            if chance > 0.7:
                autoresponse_id = self.label_encoder.get_label(i)

        return autoresponse_id
