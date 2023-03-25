from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .config import get_settings
from src.db.db import Database
from src.routers import user_router

settings = get_settings()
db = Database(settings.DATABASE_URL)

app = FastAPI(
    title="Dance-club-API",
    on_startup=[db.on_startup]
)

app.include_router(user_router.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)
