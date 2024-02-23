import json
from pydantic import BaseModel, ValidationError, NonNegativeFloat
import httpx
from os import getenv
import requests

class Money(BaseModel):
    btc_usd_price: NonNegativeFloat
    usd_pld_price

    def get_actual_price(url:str,
                         token:str,
                         api_host:str
                         ) -> list:
        querystring = {"referenceCurrencyUuid": "yhjMzLPhuIDl"}
        headers = {
            "X-RapidAPI-Key": token,
            "X-RapidAPI-Host": api_host
        }
        response = requests.get(url, headers=headers, params=querystring)
        print(response.json())
        return 0

    def usd_exchange_rate():
        url = 'http://api.nbp.pl/api/exchangerates/rates/c/usd/today/'
        response = requests.get(url)
        json_response = response.json()
        rates = json_response['rates']
        if len(rates) > 1:
            return "Rates containe more than one dictionary"
        for values in rates:
            return values['ask']


