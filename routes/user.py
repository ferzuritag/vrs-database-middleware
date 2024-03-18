from fastapi import APIRouter, Request

from methods.get_user_by_id import get_user_by_id
from methods.post_user import post_user
from methods.delete_user import delete_user

user = APIRouter()

@user.get('/users/{user_email}')
def get(user_email):
    return get_user_by_id(user_email)

@user.post('/users')
async def post(request: Request):
    return await post_user(request)

@user.delete('/users/{user_email}')
async def delete(user_email):
    return delete_user(user_email)