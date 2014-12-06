#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
import pymongo
from base import Collection as BaseCollection, Object as BaseObject
import datetime
import logging
from bantayciudad import logger

class Collection(BaseCollection):

    client = None
    database = None
    collection = None
    db_name = 'bantayciudad_core'
    collection_name = 'alerts'

    def __init__(self, **kw):

        self.client = pymongo.MongoClient()
        self.database = self.client[self.db_name]
        self.collection = self.database[self.collection_name]

"""
    This class is an SQLAlchemy ORM class object
"""
class Item(BaseObject):

    def __init__(self, *args, **kwargs):
        BaseObject.__init__(self, args, kwargs)

    def set_id(self, idn=None):

        if idn is not None:
            self.id = idn
        return self

    def set_event_type(self, event_type="entry"):

        self.event_type = event_type
        return self

    def set_sentry_id(self, sentry_id=None):

        self.sentry_id = sentry_id
        return self

    def set_uid(self, uid=None):

        self.uid = uid
        return self

    def set_status(self, status=None):

        self.status = status
        return self

    @logger.log
    def save(self, force_insert=True, only=False ):

        data = dict(self.get_data())
        ret = self._collection.insert(data)

        return ret

    @logger.log
    def get(self, idn):

        ret = self._collection.find_one(idn)
        if ret is None or len(ret) <= 0:
            self.id = ret["_id"]
            self.uid = ret["uid"]
            self.sentry_id = ret["sentry_id"]
            self.event_type = ret["event_type"]
            self.time = ret["time"]
            self.status = ret["status"]
        return self


if __name__ == "__main__":

    obj = Item(id='1', uid='1', event_type='1', status='1', sentry_id='1', time=12344555555)
    print obj.save()
    # obj.status = 1
    # obj.save()

