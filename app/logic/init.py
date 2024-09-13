from functools import lru_cache
from typing import Type
from punq import Container, Scope

from app.infra.repo.protected_secrets.memory import MemoryProtectedSecretsRepository
from app.infra.repo.secrets.memory import MemorySecretsRepository
from app.logic.commands.base import BaseCommandHandler
from app.logic.commands.protected_secret import (
    CreateProtectedSecretCommand,
    CreateProtectedSecretHandler,
)
from app.logic.commands.secret import CreateSecretCommand, CreateSecretHandler, GetSecretCommand, GetSecretHandler
from app.logic.mediator import Mediator
from app.logic.services.base import BaseSecretService
from app.logic.services.protected_secrets import ProtectSecretService
from app.logic.services.secrets import SecretService


@lru_cache(1)
def init_container():
    return _init_container()


def _init_container() -> Container:
    container = Container()
    secret_service = SecretService(repository=MemorySecretsRepository())
    protected_secret_service = ProtectSecretService(repository=MemoryProtectedSecretsRepository())
    
    container.register(GetSecretHandler, instance = GetSecretHandler(service=secret_service))
    container.register(CreateProtectedSecretHandler, instance = CreateProtectedSecretHandler(service=protected_secret_service))
    container.register(CreateSecretHandler, instance = CreateSecretHandler(service=secret_service))

    def init_mediator():
        mediator = Mediator()
        mediator.register_command(
            GetSecretCommand,
            [container.resolve(GetSecretHandler)],
        )
        mediator.register_command(
            CreateSecretCommand,
            [container.resolve(CreateSecretHandler)],
        )
        mediator.register_command(
            CreateProtectedSecretCommand,
            [container.resolve(CreateProtectedSecretHandler)],
        )

        return mediator

    container.register(Mediator, factory=init_mediator)

    return container
