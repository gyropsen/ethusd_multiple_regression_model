from datetime import datetime

from sqlalchemy import delete, text

from src.database.database import async_engine, async_session_factory
from src.database.models import (Base, BNBUSDPrices, BZUSDPrices, DJIAPrices, ETHPrices, GOLDPrices, LTCUSDPrices,
                                 NGUSDPrices, SPYPrices, USDTUSDPrices, USDXPrices, XRPUSDPrices)

tables = [
    ETHPrices,
    BZUSDPrices,
    GOLDPrices,
    SPYPrices,
    NGUSDPrices,
    USDTUSDPrices,
    USDXPrices,
    DJIAPrices,
    LTCUSDPrices,
    BNBUSDPrices,
    XRPUSDPrices,
]


class Database:
    async def create_new_tables(self):
        if not await self.exists_tables():
            async with async_engine.begin() as conn:
                await conn.run_sync(Base.metadata.drop_all)
                await conn.run_sync(Base.metadata.create_all)

    @staticmethod
    async def drop_tables():
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)

    @staticmethod
    async def exists_tables() -> list:
        async with async_engine.begin() as conn:
            result = await conn.execute(
                text("""SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE table_schema = 'public'""")
            )
            table = result.all()
            return table

    @staticmethod
    async def insert_all(data: list, symbol: str):
        """
        Добавить данные в бд
        :param data: данные с котировками
        :param symbol: сивмол котировки
        """
        for table in tables:
            if symbol.lower() in table.__tablename__:
                async with async_session_factory() as session:
                    # Преобразование каждой котировки в формат таблицы и добавление в бд
                    data_price = []
                    for price in data:
                        data_price.append(
                            table(
                                date=datetime.strptime(price["date"], "%Y-%m-%d %H:%M:%S"), close_price=price["close"]
                            )
                        )
                    session.add_all(data_price)
                    await session.flush()
                    await session.commit()

    @staticmethod
    async def delete_all():
        """
        Очистить базу данных
        """
        for table in tables:
            async with async_session_factory() as session:
                statement = delete(table)
                await session.execute(statement)
                await session.commit()

    @staticmethod
    async def get_dataframe():
        """
        Поулчить данные согласно запросу
        :return:
        """
        async with async_engine.begin() as conn:
            result = await conn.execute(
                text(
                    """select date, ethusd_prices.close_price as ethusd_close,
                                     bzusd_prices.close_price as bzusd_close,
                                     gold_prices.close_price as gold_close,
                                     spy_prices.close_price as spy_close,
                                     ngusd_prices.close_price as ngusd_close,
                                     usdtusd_prices.close_price as usdtusd_close,
                                     usdx_prices.close_price as usdx_close,
                                     djia_prices.close_price as djia_close,
                                     ltcusd_prices.close_price as ltcusd_close,
                                     bnbusd_prices.close_price as bnbusd_close,
                                     xrpusd_prices.close_price as xrpusd_close
                        from ethusd_prices
                        inner join bzusd_prices using (date)
                        inner join gold_prices using (date)
                        inner join spy_prices using (date)
                        inner join ngusd_prices using (date)
                        inner join usdtusd_prices using (date)
                        inner join usdx_prices using (date)
                        inner join djia_prices using (date)
                        inner join ltcusd_prices using (date)
                        inner join bnbusd_prices using (date)
                        inner join xrpusd_prices using (date)
                        where date in (select date from ethusd_prices
                                        INTERSECT
                                        select date from bzusd_prices
                                        INTERSECT
                                        select date from gold_prices
                                        INTERSECT
                                        select date from spy_prices
                                        INTERSECT
                                        select date from ngusd_prices
                                        INTERSECT
                                        select date from usdtusd_prices
                                        INTERSECT
                                        select date from usdx_prices
                                        INTERSECT
                                        select date from djia_prices
                                        INTERSECT
                                        select date from ltcusd_prices
                                        INTERSECT
                                        select date from bnbusd_prices
                                        INTERSECT
                                        select date from xrpusd_prices)"""
                )
            )
            table = result.all()
            return table
