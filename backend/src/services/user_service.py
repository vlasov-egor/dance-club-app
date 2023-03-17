from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from src.db.db import get_session
from src.db.models import User
from src.schemas.user_request import UserFilter, UserRegister


class UserService:
    _db_context: Session

    def __init__(self, db_context: Session = Depends(get_session)):
        self._db_context = db_context

    async def get(self, user_filter: UserFilter) -> User:
        # Todo:
        if user_filter.telegram_alias:
            user = self._db_context.query(User).filter(User.telegram_id == user_filter.telegram_alias).first()

        if user is None:
            raise HTTPException(status_code=404, detail="User not found")

        return user

    async def register(self, user: UserRegister) -> User:
        model = User(telegram_id=user.telegram_id,
                     telegram_alias=user.telegram_alias,
                     fullname=user.firstname.strip() + ' ' + user.lastname.strip())
        self._db_context.add(model)
        self._db_context.commit()
        self._db_context.refresh(model)

        return model
