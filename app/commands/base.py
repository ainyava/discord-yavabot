from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    async def run(self, message: str) -> None:
        raise NotImplementedError
