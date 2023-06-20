from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from src.database.base import Base


class Client(Base):
    __tablename__ = "Clients"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    available_sessions = Column(Float)
    used_sessions = Column(Float)

    teacher_id = Column(Integer, ForeignKey("Teachers.id"), nullable=False)
    teacher = relationship("Teacher", back_populates="clients")
