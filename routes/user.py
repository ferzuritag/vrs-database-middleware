from fastapi import APIRouter
from methods.getAllUsers import get
from methods.postUser import post
from methods.putUser import put
from methods.deleteUser import delete
from classes.Database import Database

from schemas.users import users_schema

user = APIRouter()

@user.get('/users')
def get():
    db = Database()

    users = db.getAllUsers()

    return users_schema(users)