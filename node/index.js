// simple node web server that displays hello world
// optimized for Docker image

const express = require('express');
// this example uses express web framework so we know what longer build times
// do and how Dockerfile layer ordering matters. If you mess up Dockerfile ordering
// you'll see long build times on every code change + build. If done correctly,
// code changes should be only a few seconds to build locally due to build cache.

const morgan = require('morgan');
// morgan provides easy logging for express, and by default it logs to stdout
// which is a best practice in Docker. Friends don't let friends code their apps to
// do app logging to files in containers.

// Api
const app = express();

app.use(morgan('common'));

app.get('/', function (req, res) {
  res.send('Hello Docker World\n');
});

app.get('/healthz', function (req, res) {
	// do app logic here to determine if app is truly healthy
	// you should return 200 if healthy, and anything else will fail
	// if you want, you should be able to restrict this to localhost (include ipv4 and ipv6)
  res.send('I am happy and healthy\n');
});

app.get('/documents', function (req, res, next) {
  // might have not been connected just yet
  if (db) {
    db.collection('documents').find({}).toArray(function(err, docs) {
      if (err) {
        console.error(err);
        next(new Error('Error while talking to database'));
      } else {
        res.json(docs);
      }
    });
  } else {
    next(new Error('Waiting for connection to database'));
  }
})

module.exports = app;
