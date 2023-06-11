from fastapi import FastAPI
from database import db

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
