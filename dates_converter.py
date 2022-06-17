from datetime import datetime

def convert_dates_format():
    dates = []
    with open("Dates.txt", "r") as file:
        lines = file.read().splitlines()
        for line in lines:
            dates.append(datetime.strptime(line, '%d.%m.%Y').strftime("%d-%m-%Y"))
    print(dates)


    with open('Converted_dates.txt', mode='wt') as result:
        for date in dates:
            result.write('{}\n'.format(date))

convert_dates_format()