from pymongo import MongoClient

class UsersDatabase:
    def __init__(self):

        self.client = MongoClient()

        self.database = self.client.get_database('users')

        self.users_collection = self.database.get_collection('users')
    
