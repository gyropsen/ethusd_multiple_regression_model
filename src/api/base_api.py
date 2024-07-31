from datetime import datetime, timedelta

import aiohttp
from aiohttp import ClientSession

from src.api.api_abc import API_ABC
from src.database.manager import Database


class BaseAPI(API_ABC):
    def __init__(self, token: str):
        self.__token = token

    async def get_price(self, session: ClientSession, params: dict, url: str) -> list:
        params["apikey"] = self.__token
        async with session.get(url, params=params) as response:
            data: list = await response.json()
        return data

    async def pars_data(self, symbol, days: int = 30, interval: str = "15min"):
        today = datetime.now()
        url = f"https://financialmodelingprep.com/api/v3/historical-chart/{interval}/{symbol}"
        params = {
            "from": (today - timedelta(days=days)).strftime("%Y-%m-%d"),
            "to": today.strftime("%Y-%m-%d"),
        }
        async with aiohttp.ClientSession() as session:
            data: list = await self.get_price(session, params, url)
        return data, symbol
