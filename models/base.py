#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is an EVENT type resource, which captures all event types (entry, exit etc) from a tracked entity
(i.e User, Student, Truck etc).
"""
import sys
sys.path.append("../")
from bantayciudad.db import *
import pymongo

"""
    This class
"""
class Collection(object):

    client = None
    database = None
    collection = None

    def __init__(self, *args, **kwargs):
        cl = pymongo.MongoClient()
        self.client = cl
        self.database = self.client.test
        self.collection = self.database.test

Base = declarative_base()
class Object(Base):
    """
    This is a MongoCollection object instance
    """
    _collection = None

    def __init__(self, *args, **kwargs):
        collection = Collection()
        self._collection = collection.collection

    def get_data(self):

        return self.__dict__.get('_data')

    def save(self):

        data = dict(self.get_data())
        ret = self._collection.insert(data)
        return ret

