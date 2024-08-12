import asyncio

from src.api.base_api import BaseAPI
from src.app_celery.celery import app
from src.config import load_config
from src.database.manager import Database
from src.utils import clear_and_update_data

config = load_config()
db = Database()
fin_api = BaseAPI(config.api_tokens.financialmodelingprep)


@app.task
def periodic_update_data():
    asyncio.run(clear_and_update_data(db, fin_api, config.params))


@app.task
async def add(x, y):
    pass
