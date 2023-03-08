from pydantic import BaseModel

from src.schemas.subscription_response import SubscriptionLiteResponse


class UserResponse(BaseModel):
    id: int
    fullname: str
    telegram_alias: str
    telegram_id: str
    is_admin: bool
    subscriptions: list[SubscriptionLiteResponse]
