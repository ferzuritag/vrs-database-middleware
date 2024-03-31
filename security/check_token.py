import requests
import os

def check_token(token):
    response = requests.get(f"{os.getenv('AUTH_API_PATH')}/auth/session")
    pass