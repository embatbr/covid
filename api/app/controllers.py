# -*- coding: utf-8 -*-

import uuid

import falcon


class HealthController(object):

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = 'Healthy as a horse'


class JobController(object):

    def __init__(self, spark_executor):
        self.spark_executor = spark_executor

    def on_get(self, req, resp, param):
        if req.path.startswith('/question/'):
            question = int(param)
            job_id = uuid.uuid4().hex

            if self.spark_executor.start_job(job_id, question):
                resp.body = job_id
            else:
                resp.body = 'busy'

        elif req.path.startswith('/job/'):
            job_id = param

            result = self.spark_executor.get_result(job_id)
            resp.body = result
