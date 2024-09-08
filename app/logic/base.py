from abc import ABC
from typing import TypeVar, Any, Generic

from app.infra.repo.base import BaseSecretsRepo


RT = TypeVar("RT", bound = BaseSecretsRepo)
SR = TypeVar("SR", bound= Any)

class BaseSecretService(ABC, Generic[RT, SR]):
    def __init__(self, repository : RT) -> None:
        self._repository = repository
        
    async def create(self, secret : SR) -> None:
        pass
    
    async def get(self, *args) -> SR:
        pass