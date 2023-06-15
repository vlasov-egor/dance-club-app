# Dependency
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.session import SessionLocal


async def get_db() -> AsyncSession:
    async with SessionLocal() as session:
        yield session
