from coinranking import rates_api

usd_price = rates_api.usd_exchange_rate()
btc_price = rates_api.btc_exchange_price()

print(f"{type(usd_price)} // {usd_price}")
print(f"{type(btc_price)} // {btc_price}")
btc_in_pld = usd_price*btc_price
print(round(btc_in_pld, 2), 'zł')