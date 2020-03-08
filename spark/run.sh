#!/bin/bash

export PROJECT_ROOT_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export SUBROOT_PATH="${PROJECT_ROOT_PATH}/spark"
cd ${SUBROOT_PATH}


QUESTION="${1}"


if [ -z "$SPARK_HOME" ]; then
    export SPARK_HOME="${HOME}/apps/spark"
fi

export PYSPARK_PYTHON=python3
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64


${SPARK_HOME}/bin/spark-submit \
    --packages org.apache.hadoop:hadoop-aws:2.7.3 \
    --py-files functions.py,settings.py \
    --master local[*] \
    main.py ${QUESTION}
