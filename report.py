import json
from datetime import datetime


class Report:
    def __init__(self):
        self.REPORT_NAME = datetime.now().strftime('%Y-%m-%d_%H:%M:%S') + '.json'
        self.REPORT = {}
        self.BEST_CRYPTO_24H = ''
        self.BEST_CRYPTO_2H_VOLUME = 0
        self.TOP_10_TREND = []
        self.FLOP_10_TREND = []
        self.TOP_20 = []
        self.TOP_76_MLN = []

    def get_best_crypto_24h(self):
        return self.BEST_CRYPTO_24H

    def get_best_crypto_24h_volume(self):
        return self.BEST_CRYPTO_2H_VOLUME

    def set_best_crypto_24h(self, crypto_symbol):
        self.BEST_CRYPTO_24H = crypto_symbol

    def set_best_crypto_24h_volume(self, crypto_volume):
        self.BEST_CRYPTO_2H_VOLUME = crypto_volume

    def is_top_trend(self, increment):
        return len(self.TOP_10_TREND) == 0 or increment > self.TOP_10_TREND[0]['increment']

    def delete_top_crypto(self):
        del self.TOP_10_TREND[0]

    def is_flop_trend(self, increment):
        return len(self.FLOP_10_TREND) == 0 or increment < self.FLOP_10_TREND[0]['increment']

    def delete_flop_crypto(self):
        del self.FLOP_10_TREND[0]

    def create_report_dictionary(self):
        self.REPORT = {
            'best_24h_crytpo': self.BEST_CRYPTO_24H,
            'top_10_trend': self.TOP_10_TREND,
            'flop_10_trend': self.FLOP_10_TREND,
            'top_20': self.TOP_20,
            'top_76_mln': self.TOP_76_MLN,
        }

    def create_new_report(self):
        self.create_report_dictionary()
        report_json = json.dumps(self.REPORT, indent=2)

        report_file = open(self.REPORT_NAME, "w")
        report_file.write(report_json)
