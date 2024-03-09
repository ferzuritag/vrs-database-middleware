from fastapi import APIRouter
from methods.get import get
from methods.post import post
from methods.put import put
from methods.delete import delete

user = APIRouter()

@user.delete('/user')
def on_get():
    return get()

@user.post('/user')
def on_post():
    return post()

@user.put('/user')
def on_put():
    return put()

@user.delete('/user')
def on_delete():
    return delete()
    