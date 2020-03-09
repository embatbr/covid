#!/bin/bash

export PROJECT_ROOT_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export SUBROOT_PATH="$PROJECT_ROOT_PATH/spark"
cd $SUBROOT_PATH


kill -9 $(cat spark.pid)
rm spark.pid
