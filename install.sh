#!/bin/bash

LANGUAGE=$1
ACTION=$2
PACKAGE=$3

case $LANGUAGE in
  "js")
    docker compose exec -w /opt/node_app local-node npm "$ACTION" --save "$PACKAGE"
    ;;
  "python")
    echo "Edit packages in python/requirements.txt then run 'docker-compose build'"
    ;;
esac

