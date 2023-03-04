import asyncio

from fastapi import FastAPI, Depends

from config import Settings
from src.db.db import Database

settings = Settings()

db = Database(settings.DATABASE_URL)
app = FastAPI()

app.add_event_handler("startup", db.on_startup)

# app.include_router(...)
