from pydantic import BaseModel


class UserRequest(BaseModel):
    fullname: str
    telegram_alias: str
    telegram_id: str
    is_admin: bool
