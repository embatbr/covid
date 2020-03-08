# -*- coding: utf-8 -*-

import os


PROJECT_ROOT_PATH = os.environ.get('PROJECT_ROOT_PATH')
SUBROOT_PATH = os.environ.get('SUBROOT_PATH')
FILES_DIRPATH = '{}/files'.format(PROJECT_ROOT_PATH)
INPUT_FILES_DIRPATH = '{}/inputs'.format(FILES_DIRPATH)
OUTPUT_FILES_DIRPATH = '{}/outputs'.format(FILES_DIRPATH)

JAVA_HOME = os.environ.get('JAVA_HOME', '/usr/lib/jvm/java-8-openjdk-amd64')
MAX_RESULT_SIZE = '2g'
