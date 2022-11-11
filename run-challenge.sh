#!/bin/bash

LANGUAGE=$1
CHALLENGE_ID=$2

case $LANGUAGE in
  "js")
    docker exec -it local-node-container ts-node challenges/"$CHALLENGE_ID"/js/solution.ts
    ;;
  "python")
    docker-compose run --rm local-python challenges/"$CHALLENGE_ID"/python/solution.py
    ;;
esac