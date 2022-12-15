# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
from pprint import pprint

URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

params = {
    "start": "1",
    "limit": "1",
    "convert": "USD"
}

headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": "4c775e06-4bc8-4916-92e7-dc0bc568bc85"
}

data = requests.get(URL, headers=headers, params=params).json()
pprint(data)
