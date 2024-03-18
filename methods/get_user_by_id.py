from fastapi import HTTPException

from bson.objectid import ObjectId

from classes.UsersDAO import UsersDAO
from schemas.user import user_schema

def get_user_by_id(user_id):
    usersDAO = UsersDAO()

    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=400, detail='user_id is not a valid mongo id')

    user = usersDAO.get_user_by_id(id=user_id)

    if user is None:
        raise HTTPException(status_code=404, detail='user not found')
    
    usersDAO.close_connection()
    return user_schema(user)
