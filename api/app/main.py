# -*- coding: utf-8 -*-

import falcon

from app import controllers
from app import executors


class RESTfulApplication(object):

    def __init__(self, application, routes):
        self.application = application
        self.routes = routes

    def expose(self):
        for (endpoint, controller) in self.routes.items():
            self.application.add_route(endpoint, controller)


application = falcon.API()

spark_executor = executors.SparkExecutor()

routes = {
    '/': controllers.HealthController(),
    '/question/{param}': controllers.JobController(spark_executor),
    '/job/{param}': controllers.JobController(spark_executor)
}

restful_application = RESTfulApplication(application, routes)
restful_application.expose()
