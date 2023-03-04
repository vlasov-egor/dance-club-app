from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.db.db import ModelBase


class User(ModelBase):
    __tablename__ = "Users"

    id: int = Column(Integer, primary_key=True)
    fullname: str = Column(String, nullable=True)
    telegram_alias: str = Column(String, nullable=True)
    telegram_id: str = Column(String, nullable=True)

    subscriptions = relationship("Subscription", back_populates="user")