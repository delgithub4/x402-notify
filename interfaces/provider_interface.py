from abc import ABC, abstractmethod


class ProviderInterface(ABC):

    @abstractmethod
    async def execute(
        self,
        payload,
    ):
        ...
