import requests, time
from django.shortcuts import render


class CryptoData:
    def __init__(self):
        self.usd_url = "https://api.coingecko.com/api/v3/coins/markets?" \
                       "vs_currency=usd&order=market_cap_desc&per_page=250&page=1" \
                       "&sparkline=false&price_change_percentage=24h"
        self.gbp_url = "https://api.coingecko.com/api/v3/coins/markets?" \
                       "vs_currency=gbp&order=market_cap_desc&per_page=250&page=1" \
                       "&sparkline=false&price_change_percentage=24h"

        self.previous_request = None
        self.crypto_dict = []

    def get_crypto_data_dict(self, seconds_to_wait=60):

        if not self.previous_request or self.previous_request + seconds_to_wait < time.time():
            print("requested", self.previous_request, time.time())
            self.previous_request = time.time()
            requests1 = requests.get(self.usd_url)
            results1 = requests1.json()

            requests2 = requests.get(self.gbp_url)
            results2 = requests2.json()

            for i in range(0, 250):
                self.crypto_dict.append(
                    {
                        'symbol': results1[i]['symbol'],
                        'coin_name': results1[i]['name'],
                        'changes': results1[i]['price_change_percentage_24h'],
                        'usd': results1[i]['current_price'],
                        'gbp': results2[i]['current_price']
                    }
                )

        return self.crypto_dict


crypto_data = CryptoData()


def crypt_view(request):
    context = {
        'crypto_data': crypto_data.get_crypto_data_dict()
    }

    return render(request, 'home.html', context=context)