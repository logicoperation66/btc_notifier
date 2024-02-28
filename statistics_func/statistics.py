from coinranking import usd_exchange_rate, btc_exchange_price


def price_calculate() -> float:
    usd_price = usd_exchange_rate()
    btc_price = btc_exchange_price()
    return round(usd_price*btc_price, 2)
