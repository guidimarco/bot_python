"""
    The program generate a new report with the following information:
    - best_24h_crytpo: symbol of the best crypto in the last 24h in terms of volume
    - top_10_trend: list of the best crypto based on percentage increment
    - flop_10_trend: list of the worst crypto based on percentage increment
    - top_20: top 20 cryptos with the following information:
        - unit_value: value (in USD) of one crypto
        - profit: % of profit
    - top_76_mln: top cryptos with volume > 76 mln $
"""
import operator
from market_cap import MarketCap
from report import Report

report = Report()
market_cap = MarketCap()
cryptos = market_cap.fetch_cryptos()

for index, crypto in enumerate(cryptos):
    # Get TOP 20 crypto (Market Cap ranking)
    if index < 20:
        report.TOP_20.append({
            'symbol': market_cap.get_crypto_symbol(crypto),
            'unit_value': market_cap.get_crypto_price(crypto),
            'profit': market_cap.get_crypto_percent_change_24h(crypto),
        })

    # Filter for volume 24h
    crypto_volume_24h = market_cap.get_crypto_volume_24h(crypto)
    if crypto_volume_24h > report.get_best_crypto_24h_volume():
        report.set_best_crypto_24h(crypto_volume_24h)
    if crypto_volume_24h > 76000000:
        report.TOP_76_MLN.append({
            'symbol': market_cap.get_crypto_symbol(crypto),
            'unit_value': market_cap.get_crypto_price(crypto),
        })

    # Get TOP and FLOP 10 crypto for percent increment (24h)
    crypto_percent_change_24h = market_cap.get_crypto_percent_change_24h(crypto)
    if report.is_top_trend(crypto_percent_change_24h):
        top_10_trend = report.TOP_10_TREND
        top_10_trend.append({
            'symbol': market_cap.get_crypto_symbol(crypto),
            'increment': crypto_percent_change_24h,
        })
        top_10_trend.sort(key=operator.itemgetter('increment'))
        if len(top_10_trend) > 10:
            report.delete_top_crypto()
    if report.is_flop_trend(crypto_percent_change_24h):
        flop_10_trend = report.FLOP_10_TREND
        flop_10_trend.append({
            'symbol': market_cap.get_crypto_symbol(crypto),
            'increment': crypto_percent_change_24h,
        })
        flop_10_trend.sort(key=operator.itemgetter('increment'), reverse=True)
        if len(flop_10_trend) > 10:
            report.delete_flop_crypto()

    # Generete new report
    report.create_new_report()
