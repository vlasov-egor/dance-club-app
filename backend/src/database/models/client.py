from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.database.base import Base


class Client(Base):
    __tablename__ = "Clients"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    teacher_id = Column(Integer, ForeignKey("Teachers.id"), nullable=False)
    teacher = relationship("Teacher", back_populates="clients")
