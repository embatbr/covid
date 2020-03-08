# -*- coding: utf-8 -*-

import sys

from pyspark.sql import SparkSession

from functions import line2dict, convert, questions
import settings


if __name__ == '__main__':
    filename = 'access_log_{Jul,Aug}95'

    args = sys.argv[1:]
    job_id = args[0]
    question = int(args[1])

    spark_context = SparkSession.builder.appName('covid').getOrCreate().sparkContext
    spark_context._conf.set("spark.executorEnv.JAVA_HOME", settings.JAVA_HOME)
    spark_context._conf.set("spark.driver.maxResultSize", settings.MAX_RESULT_SIZE)

    filepath = '{}/{}'.format(settings.INPUT_FILES_DIRPATH, filename)
    rdd = spark_context.textFile(filepath)
    rdd = rdd.map(line2dict)
    rdd = rdd.map(convert)

    questions[question](rdd, job_id)

    spark_context.stop()
