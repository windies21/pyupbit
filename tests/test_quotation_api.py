import pytest
from pyupbit.quotation_api import *
from pyupbit.request_api import _call_public_api
import time


def test_get_tickers_defaults():
    tickers  = get_tickers()
    assert "KRW-BTC" in tickers
    assert len(tickers) != 0


def test_get_tickers_with_fiat():
    fiats = ["KRW", "BTC", "USDT"]
    for fiat in fiats:
        fiat_tickers  = get_tickers(fiat)
        for ticker in fiat_tickers:
            assert ticker.startswith(fiat) 


def test_get_tickers_with_limit_info():
    tickers, limit_info = get_tickers(limit_info=True)
    assert isinstance(tickers, list)
    assert isinstance(limit_info, dict)


@pytest.mark.asyncio
async def test_get_ohlcv_defaults():
    resp = await get_ohlcv()
    assert isinstance(resp[0], pd.DataFrame)


def test_get_current_price_defaults():
    price = get_current_price("KRW-BTC")
    assert isinstance(price, float)


def test_get_current_price_multiple_tickers():
    prices = get_current_price(["KRW-BTC", "KRW-XRP"])
    assert isinstance(prices, dict)