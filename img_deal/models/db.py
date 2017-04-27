# coding: utf8

from settings import config
from pymongo import MongoClient

conn = MongoClient(host=config.MONGODB_HOST)
db_main = conn[config.MONGODB_NAME]


class DB(object):
    def __init__(self):
        self._registered_collection = {}

    def register(self, f):
        decorator = f
        self._registered_collection[f.__name__] = f(db_main[f.__collection__])

        if decorator is not None:
            return decorator

    def __getattr__(self, key):
        if key in self._registered_collection:
            return self._registered_collection[key]
        raise KeyError


db = DB()
