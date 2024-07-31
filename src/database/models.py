from datetime import datetime
from typing import Annotated

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

intpk = Annotated[int, mapped_column(primary_key=True)]


# Создание декларативной базы
class Base(DeclarativeBase):
    pass


class ETHPrices(Base):
    __tablename__ = "ethusd_prices"

    id: Mapped[intpk]
    date: Mapped[datetime]
    close_price: Mapped[float]


class BZUSDPrices(Base):
    __tablename__ = "bzusd_prices"

    id: Mapped[intpk]
    date: Mapped[datetime]
    close_price: Mapped[float]


class GOLDPrices(Base):
    __tablename__ = "gold_prices"

    id: Mapped[intpk]
    date: Mapped[datetime]
    close_price: Mapped[float]


class SPYPrices(Base):
    __tablename__ = "spy_prices"

    id: Mapped[intpk]
    date: Mapped[datetime]
    close_price: Mapped[float]


class NGUSDPrices(Base):
    __tablename__ = "ngusd_prices"

    id: Mapped[intpk]
    date: Mapped[datetime]
    close_price: Mapped[float]


class USDTUSDPrices(Base):
    __tablename__ = "usdtusd_prices"

    id: Mapped[intpk]
    date: Mapped[datetime]
    close_price: Mapped[float]


class USDXPrices(Base):
    __tablename__ = "usdx_prices"

    id: Mapped[intpk]
    date: Mapped[datetime]
    close_price: Mapped[float]


class DJIAPrices(Base):
    __tablename__ = "djia_prices"

    id: Mapped[intpk]
    date: Mapped[datetime]
    close_price: Mapped[float]


class LTCUSDPrices(Base):
    __tablename__ = "ltcusd_prices"

    id: Mapped[intpk]
    date: Mapped[datetime]
    close_price: Mapped[float]


class BNBUSDPrices(Base):
    __tablename__ = "bnbusd_prices"

    id: Mapped[intpk]
    date: Mapped[datetime]
    close_price: Mapped[float]


class XRPUSDPrices(Base):
    __tablename__ = "xrpusd_prices"

    id: Mapped[intpk]
    date: Mapped[datetime]
    close_price: Mapped[float]
