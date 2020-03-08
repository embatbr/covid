# -*- coding: utf-8 -*-

import falcon


class HealthController(object):

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = 'Healthy as a horse'
