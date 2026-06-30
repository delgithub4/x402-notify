from abc import ABC, abstractmethod


class ChannelInterface(ABC):

    @abstractmethod
    async def dispatch(
        self,
        payload,
    ):
        ...
