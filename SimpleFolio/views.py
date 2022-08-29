from django.shortcuts import render, redirect
from coinGecko import market
from cryptocontrol import news
from portfolio.portfolio import Values
from .models import Portfolio
import json



def crypt_view(request):
    crypto_data = market.CryptoData()

    context = {
        'crypto_data': crypto_data.get_crypto_data_dict()
    }

    return render(request, 'pages/home.html', context=context)



def news_view(request):
    crypto_news = news.crypto_news.get_news_dict()
    context = {
        'crypto_news': crypto_news
    }

    return render(request, 'cryptocontrol/news.html', context=context)


def onboarding(request):
    return render(request, 'pages/onboarding.html')

def portf_view(request):
    portfolio_values = Values()
    coin = []
    coin_data = portfolio_values.get_crypto_p_data_dict()

    for data in coin_data:
       coin.append(data)

    coin_view = Portfolio.objects.all().filter(user_id=request.user.id)
    c = []
    for i in coin_view:
        c.append({
            'id': i.id,
            'coin_name': i.coin_name,
            'amount': i.amount,
            'price_usd': round(coin_data[i.coin_name]['usd'], 2),
            'price_gbp': round(coin_data[i.coin_name]['gbp'], 2),
            'total_usd': round(i.amount * coin_data[i.coin_name]['usd'], 2),
            'total_gbp': round(i.amount * coin_data[i.coin_name]['gbp'], 2)
        })

    context = {
        'coin_view': c,
        'coin_list': coin
    }
    if request.method == 'POST':
        coin_name = request.POST['coin_name']
        amount = request.POST['amount']
        user_id = request.user.id
        portfolio = Portfolio(
            coin_name=coin_name,
            amount=amount,
            user_id=user_id
        )
        portfolio.save()
        return redirect('my-portfolio')
    return render(request, 'pages/portfolio.html', context=context)

def portf_del(requests, id):
    # peform delete function....
    Portfolio.objects.filter(id=id).delete()
    return redirect('my-portfolio')
