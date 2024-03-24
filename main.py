from fastapi import FastAPI
from routes.user import user
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.include_router(user)