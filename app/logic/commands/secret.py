from app.domain.dto.secrets import Secret
from app.logic.commands.base import BaseCommand, BaseCommandHandler
from app.logic.services.secrets import SecretService


class CreateSecretCommand(BaseCommand):
    secret_key : str
    secret_value : str
    
class GetSecretCommand(BaseCommand):
    secret_key : str
    

class CreateSecretHandler(BaseCommandHandler[CreateSecretCommand, Secret]):
    async def handle(self, command: CreateSecretCommand) -> Secret:
        secret = Secret(**command.model_dump())
        await self.service.create(secret)
        return secret
    
class GetSecretHandler(BaseCommandHandler[GetSecretCommand, Secret]):
    async def handle(self, command: GetSecretCommand) -> Secret:
        return await self.service.get(command.secret_key)