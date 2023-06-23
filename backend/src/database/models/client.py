from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from src.database.base import Base


class Client(Base):
    __tablename__ = "Clients"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    subscriptions = relationship("Subscription", back_populates="client", cascade="all, delete-orphan")