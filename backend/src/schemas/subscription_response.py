from datetime import datetime

from pydantic import BaseModel


class SubscriptionLiteResponse(BaseModel):
    id: int
    token: str
    start_date: datetime
    end_date: datetime
    available_hours: float
    total_hours: float
