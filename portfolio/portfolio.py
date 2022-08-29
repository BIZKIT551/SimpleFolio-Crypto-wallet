from django.shortcuts import render
import requests
import sys, os


# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')


# Restore
def enablePrint():
    sys.stdout = sys.__stdout__


class Values:

    def get_crypto_p_data_dict(self):
        usd_url = "https://api.coingecko.com/api/v3/coins/markets?" \
                  "vs_currency=usd&order=market_cap_desc&per_page=250&page=1" \
                  "&sparkline=false&price_change_percentage=24h"
        gbp_url = "https://api.coingecko.com/api/v3/coins/markets?" \
                  "vs_currency=gbp&order=market_cap_desc&per_page=250&page=1" \
                  "&sparkline=false&price_change_percentage=24h"

        previous_request = None

        crypto_dict = None
        crypto_dict = dict()

        requests1 = requests.get(usd_url)
        results1 = requests1.json()

        requests2 = requests.get(gbp_url)
        results2 = requests2.json()

        for i in range(0, 250):
            crypto_dict[results1[i]['id']] = {
                'coin_name': results1[i]['name'],
                'changes': results1[i]['price_change_percentage_24h'],
                'usd': results1[i]['current_price'],
                'gbp': results2[i]['current_price']
            }

        return crypto_dict


class Portfolio(Values):

    def __init__(self, coin, holdings):
        self.coin = coin
        self.holdings = holdings

    def Pull_Coin_Dat(self):

        called_crypto_dict = self.get_crypto_p_data_dict()

        try:

            Holdings_Value_USD = float(called_crypto_dict[self.coin]['usd']) * float(self.holdings)

            Holdings_Value_GBP = float(called_crypto_dict[self.coin]['gbp']) * float(self.holdings)

            print(self.coin, " USD Value of Coin", " Coin value is: $", '{0:.2f}'.format(Holdings_Value_USD))

            print(self.coin, " GBP Value of Coin", " Coin value is: £", '{0:.2f}'.format(Holdings_Value_GBP))

            print("\n")

        except:
            if self.coin in called_crypto_dict: del called_crypto_dict[self.coin]
            print("You entered an invalid Coin name or Holding amount")