from typing import overload
from app.domain.dto.secrets import Secret
from app.infra.repo.base import BaseSecretsRepo
from .base import BaseSecretService


class SecretService(BaseSecretService[BaseSecretsRepo, Secret]):
    async def create(self, secret: Secret) -> None:
        await self.repository.create(secret=secret)
    
    async def get(self, secret_key : str) -> Secret:
        return await self.repository.get(secret_key)