#!/usr/bin/env python
# -*- coding: utf-8 -*-
import falcon
import json
from base import Collection as BaseCollection, Object as BaseObject
from models import users
import logging

class Collection(BaseCollection):

    def on_post(self, req, resp):

        try:
            resp.status = falcon.HTTP_200

            self.body = {
                "status": resp.status,
                "result": {
                    "alertid": 1
                },
                "error": ""
            }
            resp.body = json.dumps(self.body)

        except Exception as e:

            self.body["result"] = False
            self.body["status"] = falcon.HTTP_500
            self.body["error"] = e.message

            logging.error(e.message)
            resp.status = falcon.HTTP_200
            resp.body = json.dumps(self.body)


class Object(BaseObject):

    def on_get(self, req, resp, idn):

        resp.status = falcon.HTTP_200
        self.body = {
            "status": resp.status,
            "result": {
                  "alertid": idn,
                  "description": "Traffic Accident with Bus and Jeepney",
                  "zip": 1605,
                  "latitude": 121.45,
                  "longitude": 54.23,
                  "severity": "warning",
                  "type": "traffic",
                  "created": 1417849697,
                  "username": "rex@onvolo.com",
                  "user_type": "authority"
            },
            "error": ""
        }
        resp.body = json.dumps(self.body)
