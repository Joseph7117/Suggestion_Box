'''
    This is the Database class: shared class by the Data Models
'''
from pymongo import MongoClient

class Database(object):
    URI = "mongodb://127.0.0.1/:27017"
    DATABASE = "suggestions"

    @staticmethod
    def initialize():
        client = MongoClient(URI)
