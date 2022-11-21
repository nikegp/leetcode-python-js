#!/bin/bash

CHALLENGE_URL=$1
CHALLENGE_ID=$2
CHALLENGE_TYPE=$3

display_help()
{
   # Display Help
   echo "Bootstrap files & folders for a new challenge"
   echo
   echo "Syntax: ./prepare-challenge.sh [-h] {CHALLENGE_URL} {CHALLENGE_ID} {CHALLENGE_TYPE}"
   echo "{CHALLENGE_TYPE} is optional, defaults to 'code'. To init a db change pass 'db'."
   echo
}

while getopts ":h" option; do
   case $option in
      h)
         display_help
         exit;;
   esac
done

if [ -z "$CHALLENGE_URL" ]; then
    echo "No challenge URL supplied, see -h option for help"
    exit 0
fi

if [ -z "$CHALLENGE_ID" ]; then
    echo "No challenge ID supplied, see -h option for help"
    exit 0
fi

if [[ $CHALLENGE_URL != https* ]];then
    echo "Wrong challenge URL provided. Did you swap the URL and ID?"
    exit 0
fi

FOLDER="challenges/$CHALLENGE_ID"

if [ -d "$FOLDER" ]; then
    echo "The challenge folder '$FOLDER' already exists."
    exit 0
fi

mkdir "$FOLDER"

if [[ "$CHALLENGE_TYPE" == "db" ]]; then
  mkdir "$FOLDER/db"
  echo "" > "$FOLDER/db/solution.sql"
  echo "" > "$FOLDER/db/ddl.sql"
else
  mkdir "$FOLDER/python"
  mkdir "$FOLDER/js"

  echo "#!/usr/bin/env python\n\n " > "$FOLDER/python/solution.py"
  cat > "$FOLDER/python/solution.py" << EOL
#!/usr/bin/env python
from challenges.utils import expect


if __name__ == "__main__":
    obj = Solution()
    expect(obj.fun(), EXPECTED_OUTPUT)
EOL

  chmod +x "$FOLDER/python/solution.py"

  echo "" > "$FOLDER/js/solution.ts"
fi

echo "$CHALLENGE_URL" > "$FOLDER/description.md"

echo "Done! Good luck with the challenge!"
