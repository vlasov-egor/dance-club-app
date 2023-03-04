import sqlalchemy

from src.db.db import metadata

subscriptions = sqlalchemy.Table(
    'Subscriptions',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('token', sqlalchemy.String, unique=True),
    sqlalchemy.Column('start_date', sqlalchemy.DateTime),
    sqlalchemy.Column('end_date', sqlalchemy.DateTime),
    sqlalchemy.Column('available_hours', sqlalchemy.Float),
    sqlalchemy.Column('total_hours', sqlalchemy.Float),
    sqlalchemy.Column('user_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('user.id')),
)
