from app.domain.dto.secrets import Secret
from ..base import BaseSecretsRepo


class MemorySecretsRepository(BaseSecretsRepo[Secret]):
    _memory : list[Secret] = []
        
    async def create(self, secret: Secret):
        self._memory.append(secret)

    async def get(self, secret_key: str) -> Secret:
        for secret in self._memory:
            if secret.secret_key == secret_key:
                return secret
