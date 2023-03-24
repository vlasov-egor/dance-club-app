from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.db.db import get_session
from src.db.models import User
from src.schemas.user import UserFilter, UserServiceModel


class UserService:
    _db_context: Session

    def __init__(self, db_context: Session = Depends(get_session)):
        self._db_context = db_context

    async def get(self, user_filter: UserFilter) -> UserServiceModel | None:
        query = (
            select(User)
        )

        if user_filter.telegram_id is not None:
            query = query.where(User.telegram_id == user_filter.telegram_id)
        if user_filter.telegram_alias is not None:
            query = query.where(User.telegram_alias == user_filter.telegram_alias)
        if user_filter.fullname is not None:
            query = query.where(User.fullname == user_filter.fullname)

        result = self._db_context.scalars(query).one_or_none()

        return UserServiceModel.from_orm(result)
