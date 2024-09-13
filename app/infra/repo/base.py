from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, Union

from pydantic import BaseModel
from app.domain.dto.secrets import ProtectedSecret, Secret


RR = TypeVar('RR', bound= Union[Secret, ProtectedSecret])

class BaseSecretsRepo(BaseModel, ABC, Generic[RR]):
    @abstractmethod
    async def create(self, secret: RR):
        pass

    @abstractmethod
    async def get(self, *args) -> RR:
        pass
