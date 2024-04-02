from classes.UsersDatabase import UsersDatabase
from classes.User import User

from uuid import uuid4

class UsersDAO:
    def __init__(self):
        self.database = UsersDatabase()
    
    def get_user_by_email(self, user_email):
        return self.database.users_collection.find_one({
            'email': user_email
        })
    
    def insert_user(self, user: User):
        return self.database.users_collection.insert_one({
            'email': user.email,
            'password': user.password,
            'verified': user.verified,
            'active': user.active,
            'account_confirmation_token': str(uuid4())
        })
    
    def delete_user_by_email(self, user_email):
        return self.database.users_collection.update_one(
        {
            'email': user_email
        }, 
        {
            '$set': {
                'active': False
            }
        })
    
    def confirm_user_account(self, user_email, account_confirmation_token):
        return self.database.users_collection.update_one({
            'email': user_email,
            'account_confirmation_token': account_confirmation_token
        }, 
        {
            '$set': {
                'active': True,
                'verified': True
            },
            '$unset': {
                'account_confirmation_token': ''
            }
        })

    def close_connection(self):
        self.database.client.close()

    
        
    
