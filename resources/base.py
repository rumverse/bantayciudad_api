#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is an EVENT type resource, which captures all event types (entry, exit etc) from a tracked entity
(i.e User, Student, Truck etc).
"""
import elasticsearch
import pymongo
import falcon
import json


class Collection(object):
    body = {}

    def __init__(self, **kw):
        self.body = {}


class Object(object):
    body = {}

    def __init__(self, **kw):
        self.body = {}