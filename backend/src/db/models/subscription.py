from datetime import datetime

from sqlalchemy import Integer, Column, ForeignKey, String, DateTime, Float

from src.db.db import ModelBase
from .user import User


class Subscription(ModelBase):
    __tablename__ = 'Subscriptions'

    id: int = Column(Integer, primary_key=True)

    token: str = Column(String, unique=True)

    start_date: datetime = Column(DateTime)
    end_date: datetime = Column(DateTime)

    available_hours: float = Column(Float)
    total_hours: float = Column(Float)

    user: User = Column(ForeignKey('user.id'), nullable=True)
    user_id: int = Column(Integer, ForeignKey('user.id'), nullable=True)
