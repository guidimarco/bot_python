import requests


class MarketCap:
    def __init__(self):
        self.URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
        self.PARAMS = {
            "start": "1",
            "convert": "USD"
        }
        self.HEADERS = {
            "Accepts": "application/json",
            "X-CMC_PRO_API_KEY": "4c775e06-4bc8-4916-92e7-dc0bc568bc85"
        }

    def fetch_cryptos(self):
        response = requests.get(self.URL, headers=self.HEADERS, params=self.PARAMS).json()
        return response['data']

    @staticmethod
    def get_crypto_symbol(crypto):
        return crypto['symbol']

    @staticmethod
    def get_crypto_price(crypto):
        return crypto['quote']['USD']['price']

    @staticmethod
    def get_crypto_percent_change_24h(crypto):
        return crypto['quote']['USD']['percent_change_24h']

    @staticmethod
    def get_crypto_volume_24h(crypto):
        return crypto['quote']['USD']['volume_24h']