from fastapi import FastAPI
from src.api.routers import clients_router

app = FastAPI()

app.include_router(clients_router.router, prefix="/clients")
