import requests
import datetime

SUNDAY_NUMBER = 6

def calculate_exchange_rates(date, currency):
    if not check_working_day(date):
        date = get_next_working_day(date)

    url = 'https://api.nbp.pl/api/exchangerates/tables/a/{}'.format(date)
    response = requests.get(url, {'format': 'api'})

    for rate in response.json()[0]['rates']:
        if rate['code'] == currency:
            result = rate['mid']
    return result

def check_working_day(date_string):
    date_in_format = datetime.datetime.strptime(date_string, '%Y-%m-%d')
    return False if date_in_format.weekday() in [5, 6] else True


def get_next_working_day(date_string):
    date_in_format = datetime.datetime.strptime(date_string, '%Y-%m-%d')
    # TODO take care of holidays - iterate through next days and send requests - check 404
    difference = (SUNDAY_NUMBER + 1) - date_in_format.weekday()
    date_result_in_format = date_in_format + datetime.timedelta(days=difference)
    date_result_string = date_result_in_format.strftime('%Y-%m-%d')

    return date_result_string


print(calculate_exchange_rates('2021-06-26', 'USD'))