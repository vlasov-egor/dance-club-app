import sys

import sqlalchemy

sys.path.append("..")
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "Users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("fullname", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("telegram_alias", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("telegram_id", sqlalchemy.String, nullable=True)
)

subscriptions = sqlalchemy.Table(
    'Subscriptions',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('token', sqlalchemy.String, unique=True),
    sqlalchemy.Column('start_date', sqlalchemy.DateTime),
    sqlalchemy.Column('end_date', sqlalchemy.DateTime),
    sqlalchemy.Column('available_hours', sqlalchemy.Float),
    sqlalchemy.Column('total_hours', sqlalchemy.Float),
    sqlalchemy.Column('user_id', sqlalchemy.ForeignKey('Users.id')),
)
