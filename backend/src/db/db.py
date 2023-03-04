import asyncio

import sqlalchemy
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_scoped_session
from sqlalchemy.orm import sessionmaker

metadata = sqlalchemy.MetaData()


class Database:
    def __init__(self, db_url: str):
        self._engine = create_async_engine(
            db_url,
            future=True,
            pool_size=80,
            max_overflow=19,
            echo=True
        )
        self.__sessionmaker = sessionmaker(
            self._engine,
            expire_on_commit=False,
            class_=AsyncSession,
            future=True
        )
        self._session_factory = async_scoped_session(self.__sessionmaker, scopefunc=asyncio.current_task)

    async def on_startup(self):
        async with self._engine.connect() as conn:
            await conn.run_sync(metadata.create_all)

    async def get_session(self) -> AsyncSession:
        session: AsyncSession = await self._session_factory()
        try:
            async with session.begin():
                yield session
        finally:
            await session.close()
