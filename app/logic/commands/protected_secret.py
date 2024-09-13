from app.domain.dto.secrets import ProtectedSecret
from app.logic.commands.base import BaseCommand, BaseCommandHandler
from app.logic.services.protected_secrets import ProtectSecretService


class CreateProtectedSecretCommand(BaseCommand):
    secret_key : str
    secret_value : str
    password : str
    

class CreateProtectedSecretHandler(BaseCommandHandler[CreateProtectedSecretCommand, ProtectedSecret]):
    service : ProtectSecretService
    
    async def handle(self, command: CreateProtectedSecretCommand) -> ProtectedSecret:
        secret = ProtectedSecret(**command.model_dump())
        await self.service.create(secret)
        return secret
    
