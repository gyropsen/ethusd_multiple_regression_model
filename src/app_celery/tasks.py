import asyncio

from src.api.base_api import BaseAPI
from src.app_celery.celery import app
from src.config import config
from src.database.manager import Database
from src.utils import update_model


db = Database()
fin_api = BaseAPI(config.api_tokens.financialmodelingprep)


@app.task
def periodic_update_data():
    asyncio.run(update_model(db, fin_api, config.params))
