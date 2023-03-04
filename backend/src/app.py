import asyncio

from fastapi import FastAPI, Depends

from config import Settings
from .db.db import Database

settings = Settings()


async def create_app():
    db = Database(settings.DATABASE_URL)
    # mb we can remove this dependency
    app = FastAPI(dependencies=[Depends(db.get_session)])

    # app.include_router(...)
    return app


if __name__ == "__main__":
    app = create_app()
    asyncio.run(app)
