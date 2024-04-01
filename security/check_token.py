from fastapi import HTTPException

import requests
import os

def check_token(token):
    if token is None:
        raise HTTPException(401, detail='Unauthorized')


    response = requests.get(f"{os.getenv('AUTH_API_PATH')}/auth/session")
    # is_active_token = body['is_active_token']

    # if is_active_token is False:
    #     raise HTTPException(status_code=401, detail='This is not a valid Token')