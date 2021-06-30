import requests
import datetime

FRIDAY_NUMBER = 4

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
    if not check_working_day(date):
        date = get_prev_working_day(date)

    url = 'https://api.nbp.pl/api/exchangerates/tables/a/{}'.format(date)
    response = requests.get(url, {'format': 'api'})

    if response.status_code == 404:
        return 0.000

    for rate in response.json()[0]['rates']:
        if rate['code'] == currency:
            result = rate['mid']
    return result

def check_working_day(date_string):
    date_in_datetime_format = datetime.datetime.strptime(date_string, '%Y-%m-%d')
    return False if date_in_datetime_format.weekday() in [5, 6] else True


def get_prev_working_day(date_string):
    date_in_datetime_format = datetime.datetime.strptime(date_string, '%Y-%m-%d')
    # TODO take care of holidays - iterate through next days and send requests - check 404
    difference = date_in_datetime_format.weekday() - FRIDAY_NUMBER 
    date_result_in_format = date_in_datetime_format - datetime.timedelta(days=difference)
    date_result_string = date_result_in_format.strftime('%Y-%m-%d')

    return date_result_string

# print(calculate_exchange_rates('2021-06-26', 'USD'))
print(calculate_multiple_exchange_rates())
