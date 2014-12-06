#!/usr/bin/env python
# -*- coding: utf-8 -*-
import falcon
import json
from base import Collection as BaseCollection, Object as BaseObject
from models import alerts
import logging
import time

def deserialize(req, resp, resource, params):
    # req.stream corresponds to the WSGI wsgi.input environ variable,
    # and allows you to read bytes from the request body.
    #
    # See also: PEP 3333
    body = req.stream.read()
    if not body:
        raise falcon.HTTPBadRequest('Empty request body',
                                    'A valid JSON document is required.')

    try:
        params['doc'] = json.loads(body.decode('utf-8'))

    except (ValueError, UnicodeDecodeError):
        raise falcon.HTTPError(falcon.HTTP_753,
                               'Malformed JSON',
                               'Could not decode the request body. The '
                               'JSON was incorrect or not encoded as UTF-8.')


def serialize(req, resp, resource):
    resp.body = json.dumps(req.context['doc'])

class Collection(BaseCollection):

    def on_post(self, req, resp):

        try:
            resp.status = falcon.HTTP_200
            """
                api_key=1234&description=Traffic Accident with Bus and Jeepney&zip=1605
                &latitude=121.65&longitude=54.1212
                &photo=http://myimages.com/id/1&severity=warning&type=traffic
                &user_type=authority&userid=1"
            """
            data = {
                "description": req.get_param("description") or "",
                "zip": req.get_param("zip") or "",
                "latitude": req.get_param("latitude") or 14.551426,
                "longitude": req.get_param("longitude") or 121.02562,
                "photo": req.get_param("photo") or None,
                "severity": req.get_param("severity") or None, #info, warning, emergency
                "type": req.get_param("type") or None, # traffic, fire, violence, medical, disaster, crime, None (as in nil), community, announcement
                "user_type": req.get_param("user_type") or "normal", #normal, authority, system
                "userid": req.get_param("user_id") or None,
                "username": req.get_param("username") or None,
                "created": int(time.time())
            }

            collection = alerts.Collection()
            mongo_id = collection.collection.insert(data)

            self.body = {
                "status": resp.status,
                "result": {
                    "alertid": str(mongo_id)
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

    def on_get(self, req, resp):

        resp.status = falcon.HTTP_200
        self.body = {
            "status": resp.status,
            "result": [
                {
                  "alertid": 1,
                  "description": "Traffic Accident with Bus and Jeepney",
                  "zip": 1226,
                  "latitude": 121.45,
                  "longitude": 54.23,
                  "severity": "info",
                  "type": "traffic",
                  "created": 1417849697,
                  "username": "rex@onvolo.com",
                  "user_type": "authority",
                  "photo": "http://myimages.com/id/1&severity=warning&type=traffic",
                  "userid": 1
                },
                {
                  "alertid": 2,
                  "description": "Traffic Accident with Bus and Jeepney",
                  "zip": 1226,
                  "latitude": 121.45,
                  "longitude": 54.26,
                  "severity": "warning",
                  "type": "traffic",
                  "created": 1417849697,
                  "username": "rex@onvolo.com",
                  "user_type": "authority",
                  "photo": "http://myimages.com/id/1&severity=warning&type=traffic",
                  "userid": 1
                },
                {
                  "alertid": 3,
                  "description": "Traffic Accident with Bus and Jeepney",
                  "zip": 1226,
                  "latitude": 121.45,
                  "longitude": 54.25,
                  "severity": "emergency",
                  "type": "traffic",
                  "created": 1417849697,
                  "username": "rex@onvolo.com",
                  "user_type": "authority",
                  "photo": "http://myimages.com/id/1&severity=warning&type=traffic",
                  "userid": 1
                }
            ],
            "error": ""
        }
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
                  "user_type": "authority",
                  "photo": "http://myimages.com/id/1&severity=warning&type=traffic",
                  "userid": 1
            },
            "error": ""
        }
        resp.body = json.dumps(self.body)
