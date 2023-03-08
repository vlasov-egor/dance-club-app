from pydantic import BaseModel


class UserRequest(BaseModel):
    fullname: str | None
