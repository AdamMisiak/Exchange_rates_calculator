import requests


def calculate_exchange_rates(date, currency):
    url = 'https://api.nbp.pl/api/exchangerates/tables/a/{}?format=json'.format(date)
    response = requests.get(url)
    for rate in response.json()[0]['rates']:
        if rate['code'] == currency:
            print(rate['mid'])


calculate_exchange_rates('2021-02-05', 'USD')