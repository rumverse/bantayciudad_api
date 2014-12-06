#!/usr/bin/env python
# -*- coding: utf-8 -*-
import falcon
import json
from base import Collection as BaseCollection, Object as BaseObject
from models import events
import logging

class Collection(BaseCollection):

    def on_post(self, req, resp):
        try:
            resp.status = falcon.HTTP_200
            event_obj = events.Object()
            idn = req.get_param("id") or None
            event_obj.set_id(idn)
            idn = event_obj.save()
            del event_obj

            self.body = {
                'data': {
                    'id': str(idn)
                },
                'status': resp.status,
                'success': True,
                'error_msg': False
            }
            resp.body = json.dumps(self.body)

        except Exception as e:

            self.body["data"] = False
            self.body["status"] = falcon.HTTP_500
            self.body["success"] = False
            self.body["error_msg"] = e.message

            logging.error(e.message)
            resp.status = falcon.HTTP_200
            resp.body = json.dumps(self.body)


class Object(BaseObject):

    def on_get(self, req, resp, idn):
        events.Object.get(idn)
        resp.body = json.dumps(self.body)
