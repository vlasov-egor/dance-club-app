from typing import Annotated

from fastapi import Depends

from src.core.clients_service import ClientsService

ClientsServiceDep = Annotated[ClientsService, Depends()]
