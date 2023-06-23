from sqlalchemy import Column, Integer, DateTime, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from src.database.base import Base


class Subscription(Base):
    __tablename__ = "Subscriptions"

    id = Column(Integer, primary_key=True)

    start_date = Column(DateTime)
    end_date = Column(DateTime)

    available_sessions = Column(Float)
    visited_sessions = Column(Float, default=0)

    is_active = Column(Boolean, default=True)

    client_id = Column(Integer, ForeignKey("Clients.id"), nullable=False)
    client = relationship("Client", back_populates="subscriptions", cascade="all, delete-orphan")

    teacher_id = Column(Integer, ForeignKey("Teachers.id"), nullable=False)
    teacher = relationship("Teacher", back_populates="subscriptions", cascade="all, delete-orphan")
