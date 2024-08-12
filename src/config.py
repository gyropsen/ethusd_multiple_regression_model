from dataclasses import dataclass

from environs import Env


@dataclass
class RabbitMQ:
    host: str
    port: str
    user: str
    password: str

    @property
    def rabbitmq_url(self):
        return f"amqp://{self.user}:{self.password}@{self.host}:{self.port}"


@dataclass
class APITokens:
    financialmodelingprep: str


@dataclass
class DataBase:
    host: str
    port: int
    user: str
    password: int
    db_name: str

    @property
    def database_url_asyncpg(self):
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}"


@dataclass
class Config:
    api_tokens: APITokens
    data_base: DataBase
    rabbitmq: RabbitMQ
    params: list


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        api_tokens=APITokens(financialmodelingprep=env("FINANCIALMODELINGPREP")),
        data_base=DataBase(
            host=env("POSTGRES_HOST"),
            port=int(env("POSTGRES_PORT")),
            user=env("POSTGRES_USER"),
            password=env("POSTGRES_PASSWORD"),
            db_name=env("POSTGRES_DB"),
        ),
        rabbitmq=RabbitMQ(
            host=env("RABBITMQ_HOST"),
            port=env("RABBITMQ_PORT"),
            user=env("RABBITMQ_USER"),
            password=env("RABBITMQ_PASSWORD"),
        ),
        params=["ETHUSD", "BZUSD", "GOLD", "SPY", "NGUSD", "USDTUSD", "USDX", "DJIA", "LTCUSD", "BNBUSD", "XRPUSD"],
    )


config = load_config()
