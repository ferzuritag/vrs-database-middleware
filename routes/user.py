from typing import Annotated
from fastapi import APIRouter, Request, Header

from methods.get_user_information import get_user_information
from methods.sign_in_user import sign_in_user
from methods.delete_user import delete_user
from methods.confirm_user_account import confirm_user_account

from security.checkAPIKey import check_api_key
from security.check_token import check_token

user = APIRouter()

@user.get('/users/{user_email}')
def getUserInformation(user_email, api_key: Annotated[str | None, Header()] = None):
    check_api_key(api_key)
    return get_user_information(user_email)

@user.get('/users/confirm-account/{user_email}/{account_confirmation_token}')
def confirmUserAccount(user_email, account_confirmation_token):
    return confirm_user_account(user_email,account_confirmation_token)

@user.post('/users')
async def signInUser(request: Request):
    return await sign_in_user(request)

@user.delete('/users/{user_email}')
async def deleteUser(user_email, authorization = Header(None)):
    check_token(token=authorization)
    return delete_user(user_email)