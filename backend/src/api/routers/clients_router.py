from typing import Annotated

from fastapi import APIRouter, Depends

from src.core import ClientsServiceDep
from src.core.clients_service import ClientsService

router = APIRouter()


@router.get("/")
async def get_all(clients_service: ClientsServiceDep):
    return await clients_service.get_all_clients()
