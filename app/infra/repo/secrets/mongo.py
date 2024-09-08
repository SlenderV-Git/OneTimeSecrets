from functools import wraps

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.domain.dao.mongo.secrets import SecretDocument
from app.domain.dto.secrets import Secret
from ..base import BaseSecretsRepo

def init_base(method):
    @wraps(method)
    async def wrapper(self, *args, **kwargs):
        await init_beanie(database=self.client.db_name, document_models=[SecretDocument])
        result = await method(self, *args, **kwargs)
        return result
    return wrapper

class MongoSecretsRepository(BaseSecretsRepo):
    def __init__(self, client : AsyncIOMotorClient):
        self.client = client
    
    @init_base 
    async def create_secret_without_password(self, secret: Secret):
        await SecretDocument(**secret).insert()
    
    @init_base
    async def get_secret(self, secret_key: str) -> Secret:
        pass