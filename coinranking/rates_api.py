import json
from pydantic import BaseModel, ValidationError, NonNegativeFloat
import httpx
from os import getenv
import requests


def btc_exchange_price() -> float:
    """Grab BTC price in USD"""
    querystring = {"referenceCurrencyUuid": "yhjMzLPhuIDl"}
    headers = {
        "X-RapidAPI-Key": getenv("btc_api_token"),
        "X-RapidAPI-Host": getenv("btc_api_host")
    }
    response = requests.get(getenv("btc_url"), headers=headers, params=querystring)
    data = response.json()['data']
    btc_price = (data['price'])
    return float(btc_price)


def usd_exchange_rate() -> float:
    """Grab USD rate from NBP api"""
    response = requests.get(url=getenv("usd_url"))
    rates = response.json()['rates']
    usd_rate = rates[0]['bid']
    return usd_rate
