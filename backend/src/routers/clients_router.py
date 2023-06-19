from fastapi import APIRouter
from src.core import clients_service

router = APIRouter()


@router.get("/")
async def get_all():
    return await clients_service.get_all_clients()
