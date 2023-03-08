from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from src.db.db import get_session
from src.db.models import User
from src.schemas.user_request import UserRequest


class UserService:
    _db_context: Session

    def __init__(self, db_context: Session = Depends(get_session)):
        self._db_context = db_context

    async def get(self, telegram_user_id: str) -> User:
        user = self._db_context.query(User).filter(User.telegram_id == telegram_user_id).first()

        if user is None:
            raise HTTPException(status_code=404, detail="User not found")

        return user

    async def post(self, user: UserRequest) -> User:
        model = User(**user.dict())
        self._db_context.add(model)
        self._db_context.commit()
        self._db_context.refresh(model)

        return model
