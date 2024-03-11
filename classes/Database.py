from pymongo import MongoClient

class Database:
    def __init__(self):
        self.url = ''
        self.USER = ''
        self.PASSWORD = ''

        self.client = MongoClient('mongodb://localhost:27017/')

        self.database = self.client.get_database('users')

        self.collection = self.database.get_collection('users')
    
    def getAllUsers(self):
        return self.collection.find()
