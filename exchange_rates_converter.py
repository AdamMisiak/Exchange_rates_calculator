import requests
import datetime

FRIDAY_NUMBER = 4
URL_BASE = 'https://api.nbp.pl/api/exchangerates/tables/a/'

def calculate_multiple_exchange_rates():
    with open("Input.txt", "r") as file:
        dates = file.read().splitlines()
    with open('Output.txt', mode='wt') as result:
        for date in dates:
            date_in_datetime_format = datetime.datetime.strptime(date, '%d.%m.%Y')
            date_prev_day = date_in_datetime_format - datetime.timedelta(days=1)
            date_converted = date_prev_day.strftime('%Y-%m-%d')
            # TODO add more currencies
            result.write('{}\n'.format(calculate_exchange_rates(date_converted, 'USD')))

def calculate_exchange_rates(date, currency):
    date = get_working_day_date(date)

    url = URL_BASE + date
    response = requests.get(url, {'format': 'api'})

    if response.status_code == 404:
        date = get_working_day_before_holiday(date)

    for rate in response.json()[0]['rates']:
        if rate['code'] == currency:
            result = rate['mid']
    return result

def get_working_day_date(date):
    date_in_datetime_format = datetime.datetime.strptime(date, '%Y-%m-%d')

    if date_in_datetime_format.weekday() in [5, 6]: # 5 and 6 = Saturday and Sunday
        return get_working_day_before_weekend(date)
    # else:
        # url = URL_BASE + date
        # response = requests.get(url, {'format': 'api'})
        # if response.status_code == 404:
        #     return get_working_day_before_holiday(date)
    return date

def get_working_day_before_weekend(date):
    date_in_datetime_format = datetime.datetime.strptime(date, '%Y-%m-%d')
    difference = date_in_datetime_format.weekday() - FRIDAY_NUMBER 
    date_result_in_datetime_format = date_in_datetime_format - datetime.timedelta(days=difference)
    date_result_string = date_result_in_datetime_format.strftime('%Y-%m-%d')
    return date_result_string

def get_working_day_before_holiday(date):
    date_in_datetime_format = datetime.datetime.strptime(date, '%Y-%m-%d')
    date_prev_in_datetime_format = date_in_datetime_format
    url = URL_BASE + date
    response = requests.get(url, {'format': 'api'})
    while response.status_code == 404:
        date_prev_in_datetime_format = date_prev_in_datetime_format - datetime.timedelta(days=1)
        date_result_string = date_prev_in_datetime_format.strftime('%Y-%m-%d')
        url = URL_BASE + date_result_string
        response = requests.get(url, {'format': 'api'})
    return date_result_string

calculate_multiple_exchange_rates()
