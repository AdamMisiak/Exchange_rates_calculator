import requests
import datetime

URL_BASE = 'https://api.nbp.pl/api/exchangerates/tables/a/'

def calculate_multiple_exchange_rates():
    dates = []
    with open("Input.txt", "r") as file:
        lines = file.read().splitlines()
        for line in lines:
            dates.append(line.split('\t'))

    with open('Output.txt', mode='wt') as result:
        for date in dates:
            date_in_datetime_format = datetime.datetime.strptime(date[0], '%d.%m.%Y')
            date_prev_day = date_in_datetime_format - datetime.timedelta(days=1) #take rate from day before dividend payout day
            date_converted = date_prev_day.strftime('%Y-%m-%d')

            if date[1] == 'XTB': #do not calculate rates for XTB broker
                result.write('{}\n'.format('-'))
            else:
                result.write('{}\n'.format(calculate_exchange_rates(date_converted, date_in_datetime_format, date[4])))

def calculate_exchange_rates(date_in_string_format, date_in_datetime_format, currency):
    url = URL_BASE + date_in_string_format
    response = requests.get(url, {'format': 'api'})

    while response.status_code == 404:
        date_in_datetime_format = date_in_datetime_format - datetime.timedelta(days=1)
        date_in_string_format = date_in_datetime_format.strftime('%Y-%m-%d')

        url = URL_BASE + date_in_string_format
        response = requests.get(url, {'format': 'api'})

    for rate in response.json()[0]['rates']:
        if rate['code'] == currency:
            result = rate['mid']
    return result

calculate_multiple_exchange_rates()
