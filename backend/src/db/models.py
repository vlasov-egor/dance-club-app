import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

ModelBase = declarative_base()


class User(ModelBase):
    __tablename__ = "Users"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    fullname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    telegram_alias = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    telegram_id = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    is_admin = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)

    subscriptions = relationship('Subscription', back_populates="user", uselist=False)

    def __repr__(self):
        return f"<User {self.id}, {self.fullname}, {self.telegram_alias}, {self.telegram_id}, {self.is_admin}>"


class Subscription(ModelBase):
    __tablename__ = "Subscriptions"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    token = sqlalchemy.Column(sqlalchemy.String, unique=True)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime)
    available_hours = sqlalchemy.Column(sqlalchemy.Float)
    total_hours = sqlalchemy.Column(sqlalchemy.Float)

    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('Users.id'))
    user = relationship('User', back_populates='subscriptions')

    def __repr__(self):
        return f"<Subscription {self.id}, {self.token}, {self.start_date}, {self.end_date}, {self.available_hours}, {self.total_hours}, {self.user_id}>"
