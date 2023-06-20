from typing import Annotated

from fastapi import APIRouter, Depends

from src.api.schemas.client import ClientCreateRequest
from src.core import ClientsServiceDep
from src.core.clients_service import ClientsService
from src.database.models.client import Client

router = APIRouter()


@router.get("/")
async def get_all(clients_service: ClientsServiceDep):
    return await clients_service.get_all_clients()


@router.post("/")
async def create(client: ClientCreateRequest, clients_service: ClientsServiceDep):
    return await clients_service.create(Client(**client.dict()))
