from abc import ABC, abstractmethod

from aiohttp import ClientSession


class API_ABC(ABC):
    @abstractmethod
    async def get_price(self, session: ClientSession, params: dict, url: str):
        pass
