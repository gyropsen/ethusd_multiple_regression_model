import aiohttp
import pytest

from src.api.base_api import APIAlphavantage
from src.config import Config, load_config


@pytest.fixture
def get_config_data():
    return load_config()


@pytest.mark.asyncio
async def test_api_alphavantage(get_config_data: Config):
    api = APIAlphavantage(get_config_data.api_tokens.alphavantage_token)
    params = {
        "function": "NATURAL_GAS",
        "interval": "monthly",
    }
    async with aiohttp.ClientSession() as session:
        data = await api.get_prices_for_symbol(session, params)
    assert data
    assert data.get("Error Message") is None


# @pytest.mark.parametrize("arg_1, arg_2, expected_result", [(2, 2, f"{date_now} foo ok"),
#                                                            (2, "2",
#                                                             f"{date_now} foo error: unsupported operand type(s) for +:"
#                                                             " 'int' and 'str' Inputs: (2, '2') {}"),
#                                                            (None, None,
#                                                             f"{date_now} foo error: unsupported operand type(s) for "
#                                                             "+: 'NoneType' and 'NoneType' Inputs: (None, None) {}")
#                                                            ])
