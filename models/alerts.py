#!/usr/bin/env python
# -*- coding: utf-8 -*-
# models/alerts.py
import pymongo
from base import Collection as BaseCollection, Item as BaseItem
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

class Item(BaseItem):

    def __init__(self, *args, **kwargs):
        logging.log(logging.INFO, "initialized")