import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel

DATABASE_URL = "postgresql://postgres:postgres@localhost:6432/postgres"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "Users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String)
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)
