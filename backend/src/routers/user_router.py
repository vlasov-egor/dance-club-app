from fastapi import APIRouter, Depends

from src.schemas.user_request import UserRequest
from src.schemas.user_response import UserResponse
from src.services.user_service import UserService

router = APIRouter(prefix="/users")


@router.get("/{telegram_user_id}", response_model=UserResponse | None)
async def get(telegram_user_id: str, _user_service: UserService = Depends(UserService)):
    return await _user_service.get(telegram_user_id)


@router.post("/")
async def post(user: UserRequest, _user_service: UserService = Depends(UserService)):
    return await _user_service.post(user)
