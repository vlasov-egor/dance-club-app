from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from src.db.models import User
from src.schemas.user_request import UserFilter, UserLogin, UserRegister
from src.services.user_service import UserService

router = APIRouter(prefix="/users")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/token")


async def get_current_user(token: str = Depends(oauth2_scheme), _user_service: UserService = Depends(UserService)):
    user_in_db: User = await _user_service.get(UserFilter(telegram_alias=token))
    if not user_in_db:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user_in_db


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    return current_user


# Todo: try just Depends()
@router.post("/token")
async def login(user: UserLogin, _user_service: UserService = Depends(UserService)):
    user_in_db: User = await _user_service.get(UserFilter(telegram_alias=user.telegram_alias))
    if not user_in_db:
        raise HTTPException(status_code=400, detail="Incorrect username")

    return {"access_token": user_in_db.telegram_alias, "token_type": "bearer"}


@router.get("/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@router.post("/register")
async def register(user: UserRegister, _user_service: UserService = Depends(UserService)):
    return await _user_service.register(user)
