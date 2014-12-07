#!/usr/bin/env python
# -*- coding: utf-8 -*-
# models/location.py
import pymongo
from base import Collection as BaseCollection, Item as BaseItem
import time
import logging
from bantayciudad import logger
from bson.objectid import ObjectId

class Collection(BaseCollection):

    client = None
    database = None
    collection = None
    db_name = 'bantayciudad_core'
    collection_name = 'location'

    def __init__(self, **kw):

        self.client = pymongo.MongoClient()
        self.database = self.client[self.db_name]
        self.collection = self.database[self.collection_name]

    def recalculate_score(self, id, params):

        location = self.collection.find_one(ObjectId(id))
        if location is not None:
            ## calc here
            if "safety_score" in location:
                for i in params:
                    if i in location:
                        location[i] += 1
                    else:
                        location[i] = 1
            else:
                for i in params:
                    location["safety_score"] = {
                        i: 1
                    }
            self.collection.save({"_id": ObjectId(id)}, location)

        else:
            return False

    def add_score(self, zipc=None, fulltext_location=None, safety_score={}):

        timenow = int(time.time())
        location = {
            "zip": zipc,
            "fulltext_location": fulltext_location,
            "safety_score": safety_score,
            "created": timenow
        }

        return self.collection.insert(location)




class Item(BaseItem):

    def __init__(self, *args, **kwargs):
        logging.log(logging.INFO, "initialized")
