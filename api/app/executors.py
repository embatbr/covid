# -*- coding: utf-8 -*-

import os


PROJECT_ROOT_PATH = os.environ.get('PROJECT_ROOT_PATH')
FILES_DIRPATH = '{}/files'.format(PROJECT_ROOT_PATH)
OUTPUT_FILES_DIRPATH = '{}/outputs'.format(FILES_DIRPATH)


class SparkExecutor(object):

    def __init__(self):
        self.current_job = None

    def start_job(self, job_id, question):
        is_idle = not self.current_job
        last_job_finished = os.path.exists('{}/{}'.format(OUTPUT_FILES_DIRPATH, self.current_job))

        if is_idle or last_job_finished:
            if last_job_finished:
                command = "{}/spark/stop.sh"
                os.system(command)

            self.current_job = job_id
            command = "{}/spark/start.sh {} {}".format(PROJECT_ROOT_PATH, self.current_job, question)
            os.system(command)

            return True

        return False

    def get_result(self, job_id):
        job_result_filepath = '{}/{}'.format(OUTPUT_FILES_DIRPATH, job_id)
        if os.path.exists(job_result_filepath):
            with open(job_result_filepath) as f:
                return f.read()

        return None
