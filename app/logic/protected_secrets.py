from typing import overload
from app.domain.dto.secrets import ProtectedSecret
from app.infra.repo.base import BaseSecretsRepo
from .base import BaseSecretService


class ProtectSecretService(BaseSecretService[BaseSecretsRepo, ProtectedSecret]):
    async def create(self, secret: ProtectedSecret) -> None:
        await self._repository.create(secret=secret)
    
    async def get(self, secret_key : str, password : str) -> ProtectedSecret:
        return await self._repository.get(secret_key, password)