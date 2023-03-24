from pydantic import BaseModel

from src.schemas.subscription_response import SubscriptionLiteResponse


class UserFilter(BaseModel):
    fullname: str | None
    telegram_alias: str | None
    telegram_id: str | None


class UserResponse(BaseModel):
    id: int
    fullname: str
    telegram_alias: str
    telegram_id: str
    is_admin: bool
    subscriptions: list[SubscriptionLiteResponse] | None

    class Config:
        orm_mode = True


class UserServiceModel(BaseModel):
    id: int
    fullname: str
    telegram_alias: str
    telegram_id: str
    is_admin: bool

    class Config:
        orm_mode = True
