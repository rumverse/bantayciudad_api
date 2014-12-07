#!/usr/bin/env python
# -*- coding: utf-8 -*-
# resources/location.py

import falcon
import json
from base import Collection as BaseCollection, Object as BaseObject
from models import location
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

    def on_get(self, req, resp):

        resp.status = falcon.HTTP_200
        self.body = {
            "status": resp.status,
            "result": {
                  "locationid": 1,
                  "zip": 1226,
                  "fulltext_location": "Legaspi Village, Makati City, PH",
                  "safety_score": {
                      "overall": 99,
                      "traffic accidents": 100,
                      "violence": 100,
                      "drugs": 100,
                      "fire": 100,
                      "disaster": 90
                  },
                  "safety_message": "Relatively safe, you can walk around",
                  "created": 1417867943,
                  "username": "rex@onvolo.com",
                  "userid": 1
            },
            "error": ""
        }
        resp.body = json.dumps(self.body)
