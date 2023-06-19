from sqlalchemy import select

from src.api.dependencies import db_session
from src.database.models.client import Client


async def get_all_clients(db: db_session):
    # Todo: add filtering for teacher
    query = select(Client).order_by(Client.name)
    return await db.execute(query).scalars().all()
