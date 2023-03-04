import sqlalchemy
from sqlalchemy.orm import relationship

from src.db.db import metadata

users = sqlalchemy.Table(
    "Users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("fullname", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("telegram_alias", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("telegram_id", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("subscriptions", relationship("Subscription", back_populates="user"))
)
