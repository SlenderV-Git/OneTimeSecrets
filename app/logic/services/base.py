from abc import ABC
from typing import TypeVar, Any, Generic

from pydantic import BaseModel

from app.infra.repo.base import BaseSecretsRepo


RT = TypeVar("RT", bound = BaseSecretsRepo)
SR = TypeVar("SR", bound= Any)

class BaseSecretService(BaseModel, ABC, Generic[RT, SR]):
    repository : RT
        
    async def create(self, secret : SR) -> None:
        pass
    
    async def get(self, *args) -> SR:
        pass