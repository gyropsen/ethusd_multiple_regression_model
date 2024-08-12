import pandas as pd
import scipy
import statsmodels.formula.api as sm
import asyncio

from src.api.base_api import BaseAPI
from src.database.manager import Database


async def get_dataframe(data) -> pd.DataFrame:
    """
    Получить датафрейм из данных
    :param data: запрос из бд
    :return: DataFrame
    """
    print(len(data))
    return pd.DataFrame(
        columns=[
            "dates",
            "ethusd_close",
            "bzusd_close",
            "gold_close",
            "spy_close",
            "ngusd_close",
            "usdtusd_close",
            "usdx_close",
            "djia_close",
            "ltcusd_close",
            "bnbusd_close",
            "xrpusd_close",
        ],
        data=data,
    )


async def get_ols(formula: str, df: pd.DataFrame, i) -> pd.DataFrame | None:
    """
    Получить модель множественной регрессии
    :param formula: формула построения
    :param df: датафрейм
    :param i: порядковый номер
    :return: модель множественной регрессии
    """
    result = sm.ols(formula=formula, data=df).fit()
    if result.fvalue > scipy.stats.f.ppf(0.05, result.df_model, result.df_resid):
        tvalues = result.tvalues.drop(index=["Intercept"])
        delete_column = tvalues.loc[tvalues.abs() == tvalues.abs().min()].keys().tolist()
        return result, delete_column
    else:
        print(f"Модель {i} Отклоняется, т.е. между ethusd_close и хотя бы одним х1..хn не существует линейной связи")
        return


async def get_model(df: pd.DataFrame) -> pd.DataFrame:
    """
    Получить фильтрованную модель множественной регрессии
    :param df: датафрейм
    :return: фильтрованная модель множественной регрессии
    """
    df_drop_dates = df.drop(["dates"], axis=1)
    # correlation_matrix = df_drop_dates.corr()

    columns = list(df_drop_dates.columns)[1:]
    pd.set_option("display.max_columns", None)
    # columns =  ['bzusd_close', 'gold_close', 'spy_close', 'ngusd_close', 'usdtusd_close', 'usdx_close', 'djia_close',
    # 'ltcusd_close', 'bnbusd_close', 'xrpusd_close']

    delete_columns = []
    filter_ols = None
    for i in range(len(columns)):
        formula = f"ethusd_close ~ {" + ".join(list(set(columns).difference(set(delete_columns))))}"
        if i == 0:
            df_drop = df_drop_dates
        else:
            df_drop = df_drop_dates.drop(columns=delete_columns, axis=1)
        ols, delete_column = await get_ols(formula=formula, df=df_drop, i=i)
        delete_columns.extend(delete_column)
        if ols:
            filter_ols = ols
    return filter_ols


async def update_model(db: Database, fin_api: BaseAPI, params: list) -> None:
    """
    Функция очистки и обновления данных
    :param db: менеджер бд
    :param fin_api: менеджер api
    :param params: конфиг файлы
    :return: None
    """
    # Очистка таблиц от старых данных
    await db.delete_all()
    # Получение данных
    result = await asyncio.gather(
        *[asyncio.create_task(fin_api.pars_data(symbol, days=90)) for symbol in params]
    )
    # Запись в базу данных
    await asyncio.gather(*[db.insert_all(res[0], res[1]) for res in result])

    # Получение датафрейма из базы данных
    df = await get_dataframe(await db.get_dataframe())

    # Построение модели
    model = await get_model(df)
    print(model)
