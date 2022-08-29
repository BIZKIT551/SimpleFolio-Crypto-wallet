import requests
import time
from django.shortcuts import render


class CryptoNews:
    def __init__(self):
        self.CryptoControlAPI = 'https://cryptocontrol.io/api/v1/public/news?key=7a38f7bf0ffcd66da060b3f4c9b5d9ba'

        self.previous_request = None
        self.news_list = []

    def get_news_dict(self, seconds_to_wait=60):

        if not self.previous_request or self.previous_request + seconds_to_wait < time.time():
            print("requested", self.previous_request, time.time())
            self.previous_request = time.time()
            news_request = requests.get(self.CryptoControlAPI)
            results = news_request.json()

            # self.api.getLatestNews('en')

            for i in range(0, 5):
                self.news_list.append(
                    {
                        'title': results[i]['title'],
                        'publishedAt': results[i]['publishedAt'],
                        'sourceDomain': results[i]['sourceDomain'],
                        'url': results[i]['url'],
                        'thumbnail': results[i]['thumbnail']
                    },
                )
        return self.news_list


crypto_news = CryptoNews()


def news_view(request):
    x = crypto_news.get_news_dict()
    print('------', x)
    context = {
        'crypto_news': 'x'
    }

    return render(request, 'cryptocontrol/news.html', context=context)