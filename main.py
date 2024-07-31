import asyncio

from src.api.base_api import BaseAPI
from src.config import load_config
from src.database.manager import Database
from src.utils import get_dataframe, get_model


async def main():
    # Конфигурация
    config = load_config()

    # База данных
    db = Database()
    await db.create_new_tables()

    while True:
        # Очистка таблиц от старых данных
        await db.delete_all()

        # API и получение данных
        fin_api = BaseAPI(config.api_tokens.financialmodelingprep)
        result = await asyncio.gather(
            *[asyncio.create_task(fin_api.pars_data(symbol, days=90)) for symbol in config.params]
        )

        # Запись в базу
        for res in result:
            await db.insert_all(res[0], res[1])

        # Получение датафрейма из базы данных
        df = await get_dataframe(await db.get_dataframe())

        # Построение модели
        model = await get_model(df)
        print(model)

        # Использование модели
        # ...

        # Задержка для повторения
        await asyncio.sleep(60 * 30)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Завершено пользователем")
    except Exception as e:
        print(e)
