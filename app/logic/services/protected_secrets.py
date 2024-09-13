from typing import overload
from app.domain.dto.secrets import ProtectedSecret
from app.infra.repo.base import BaseSecretsRepo
from .base import BaseSecretService


class ProtectSecretService(BaseSecretService[BaseSecretsRepo, ProtectedSecret]):
    repository : BaseSecretsRepo
    
    async def create(self, secret: ProtectedSecret) -> None:
        await self.repository.create(secret=secret)
    
    async def get(self, secret_key : str, password : str) -> ProtectedSecret:
        return await self.repository.get(secret_key, password)