# -*- coding: utf-8 -*-

import falcon

from app import controllers


class RESTfulApplication(object):

    def __init__(self, application, routes):
        self.application = application
        self.routes = routes

    def expose(self):
        for (endpoint, controller) in self.routes.items():
            self.application.add_route(endpoint, controller)


application = falcon.API()

routes = {
    '/': controllers.HealthController()
}

restful_application = RESTfulApplication(application, routes)
restful_application.expose()
