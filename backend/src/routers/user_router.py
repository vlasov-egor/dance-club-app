from typing import Annotated

from fastapi import APIRouter, Depends

from src.routers.dependecies import get_current_user
from src.schemas.user import UserServiceModel

router = APIRouter(prefix="/users")


@router.get("/")
def get_current(user: UserServiceModel = Depends(get_current_user)):
    return user
