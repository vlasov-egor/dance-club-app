import contextlib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from config import get_settings
from . import models


class Database:
    def __init__(self, db_url: str):
        self._engine = create_engine(db_url, echo=True)
        self._session_factory = sessionmaker(bind=self._engine, autocommit=False, autoflush=False)

    def on_startup(self):
        models.ModelBase.metadata.create_all(self._engine)

    @contextlib.contextmanager
    def get_session(self) -> Session:
        session: Session = self._session_factory()
        try:
            with session.begin():
                yield session
        finally:
            session.close()


database = Database(get_settings().DATABASE_URL)


def get_session() -> Session:
    with database.get_session() as session:
        return session
