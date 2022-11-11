#!/bin/bash

CONTAINER=$1
ACTION=$2
PACKAGE=$3

docker compose exec local-node -w /opt/node_app "$CONTAINER" npm "$ACTION" --save "$PACKAGE"