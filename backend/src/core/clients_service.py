from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.dependencies import DbSessionDep
from src.database.models.client import Client


class ClientsService:
    _db_session: AsyncSession

    def __init__(self, session: DbSessionDep):
        self._db_session = session

    async def get_all_clients(self) -> list[Client]:
        # Todo: add filtering for teacher
        stmt = select(Client).order_by(Client.name)
        result = await self._db_session.execute(stmt)
        return result.scalars().all()

    async def create(self, client: Client) -> Client:
        client.teacher_id = 1
        client.used_sessions = 0

        self._db_session.add(client)
        await self._db_session.commit()
        await self._db_session.refresh(client)

        return client
