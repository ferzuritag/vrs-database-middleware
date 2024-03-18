from classes.UsersDAO import UsersDAO
from fastapi import HTTPException

def confirm_user_account(user_email,account_confirmation_token):
    usersDAO = UsersDAO()

    user_updated_data = usersDAO.confirm_user_account(user_email, account_confirmation_token)

    if user_updated_data is None:
        raise HTTPException(402, detail=f'Couldnt activate token for user {user_email}')
    
    return {
        'detail': 'Account has been confirmed'
    } 
