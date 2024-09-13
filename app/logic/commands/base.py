from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar
from pydantic import BaseModel

from app.logic.services.base import BaseSecretService


class BaseCommand(BaseModel):
    pass

CT = TypeVar('CT', bound=BaseCommand)
CR = TypeVar('CR', bound=Any)

class BaseCommandHandler(BaseModel, ABC, Generic[CT, CR]):
    service : BaseSecretService
    
    @abstractmethod
    async def handle(self, command : CT) -> CR:
        pass
    
