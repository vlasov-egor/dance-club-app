from pydantic import BaseModel


class ClientCreateRequest(BaseModel):
    name: str
    available_sessions: float
