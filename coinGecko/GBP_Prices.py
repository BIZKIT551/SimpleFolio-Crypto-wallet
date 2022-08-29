import json
import requests

url_gbp = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=gbp&order=market_cap_desc&per_page=5&page=1' \
          '&sparkline=false&price_change_percentage=24h '

requests = requests.get(url_gbp)
results = requests.json()

# print(json.dumps(results, sort_keys=True, indent=4))

for g in range(0, 5):
    prices = (json.dumps(results[g]['current_price']))

    print("£" + "{:.2f}".format(float(prices)))