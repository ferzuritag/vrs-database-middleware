from classes.UsersDatabase import UsersDatabase
from classes.User import User
from bson.objectid import ObjectId
class UsersDAO:
    def __init__(self):
        self.database = UsersDatabase()
    
    def get_user_by_id(self, id):
        return self.database.users_collection.find_one({
            '_id': ObjectId(id)
        })
    
    def get_user_by_email(self, email):
        return self.database.users_collection.find_one({
            'email': email
        })
    
    def insert_user(self, user: User):
        return self.database.users_collection.insert_one({
            'email': user.email,
            'password': user.password,
            'verified': user.verified,
            'active': user.active
        })
    
    def delete_user_by_email(self, user_email):
        return self.database.database.users_collection.update_one({'email': user_email},{
            '$set': {
                'active': False
            }
        })
        pass

    def close_connection(self):
        self.database.client.close()

    
        
    
