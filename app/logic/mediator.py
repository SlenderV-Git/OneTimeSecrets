from collections import defaultdict
from dataclasses import field
from typing import Iterable
from pydantic import BaseModel

from app.logic.commands.base import CR, CT, BaseCommand, BaseCommandHandler


class Mediator(BaseModel):
    commands_map : dict[CT, list[BaseCommandHandler]] = field(
        default_factory=lambda: defaultdict(list),
        kw_only=True,
    )
    
    def register_command(self,
                         command : CT,
                         handlers : Iterable[BaseCommandHandler[CT, CR]]):
        
        self.commands_map[command].extend(handlers)
        
    async def handle_command(self, command : BaseCommand) -> Iterable[CR]:
        command_type = command.__class__
        handlers = self.commands_map.get(command_type)
        
        return [await handler.handle(command) for handler in handlers]
