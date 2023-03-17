from pydantic import BaseModel


class UserRegister(BaseModel):
    telegram_id: str
    telegram_alias: str
    firstname: str
    lastname: str


class UserLogin(BaseModel):
    telegram_alias: str


class UserFilter(BaseModel):
    telegram_alias: str | None
