import json
import requests

url_usd = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=5&page=1' \
          '&sparkline=false&price_change_percentage=24h '

requests = requests.get(url_usd)
results = requests.json()

# print(json.dumps(results, sort_keys=True, indent=4))

for u in range(0, 5):
    usd = (json.dumps(results[u]['current_price']))

    print("$" + "{:.2f}".format(float(usd)))

