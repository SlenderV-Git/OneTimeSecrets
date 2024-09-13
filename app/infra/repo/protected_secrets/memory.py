from app.domain.dto.secrets import ProtectedSecret
from ..base import BaseSecretsRepo


class MemoryProtectedSecretsRepository(BaseSecretsRepo[ProtectedSecret]):
    _memory : list[ProtectedSecret] = []
        
    async def create(self, secret: ProtectedSecret):
        self._memory.append(secret)

    async def get(self, secret_key: str, password: str) -> ProtectedSecret:
        for secret in self._memory:
            if secret.secret_key == secret_key and secret.password == password:
                return secret