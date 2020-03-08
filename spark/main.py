# -*- coding: utf-8 -*-

import sys

from pyspark.sql import SparkSession

from functions import line2dict, convert, questions
import settings


if __name__ == '__main__':
    filename = 'access_log_{Jul,Aug}95'

    args = sys.argv[1:]
    question = int(args[0])

    spark_context = SparkSession.builder.appName('covid').getOrCreate().sparkContext
    spark_context._conf.set("spark.executorEnv.JAVA_HOME", settings.JAVA_HOME)
    spark_context._conf.set("spark.driver.maxResultSize", settings.MAX_RESULT_SIZE)

    filepath = '{}/files/{}'.format(settings.PROJECT_ROOT_PATH, filename)
    rdd = spark_context.textFile(filepath)
    rdd = rdd.map(line2dict)
    rdd = rdd.map(convert)

    print()
    print(questions[question](rdd))
    print()

    spark_context.stop()
