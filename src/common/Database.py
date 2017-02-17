'''
    This is the Database class: shared class by the Data Models
'''
from pymongo import MongoClient

class Database(object):
    #Defining the Database and URI as static variables
    URI = 'mongodb://127.0.0.1:27017'
    DATABASE = None

    #Ensure the instance of the Database Class is shared across all methods thus making the models static
    @staticmethod
    def initialize():
        client = MongoClient(Database.URI)
        Database.DATABASE = client['suggestions']

    @staticmethod
    def insert_data(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def delete(collection, query):
        Database.DATABASE[collection].remove(query)