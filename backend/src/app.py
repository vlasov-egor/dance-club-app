import asyncio

from fastapi import FastAPI

from config import Settings
from .db.db import Database


async def create_app():
    app = FastAPI()
    db = Database(Settings.DATABASE_URL)

    # app.include_router(...)
    return app


if __name__ == "__main__":
    app = create_app()
    asyncio.run(app)
