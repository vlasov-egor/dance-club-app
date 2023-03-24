from fastapi import Header, Depends
from fastapi.exceptions import HTTPException

from src.schemas.user import UserFilter, UserServiceModel
from src.services.user_service import UserService


async def get_current_user(user_id: str | None = Header(default=None),
                           _user_service: UserService = Depends(UserService)) -> UserServiceModel:
    if user_id is None:
        raise HTTPException(status_code=404, detail="Cannot get user from request")

    if (user := await _user_service.get(UserFilter(telegram_id=user_id))) is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user
