from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship

from src.database.base import Base


class Teacher(Base):
    __tablename__ = "Teachers"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    clients = relationship("Client", back_populates="teacher", cascade="all, delete-orphan")
