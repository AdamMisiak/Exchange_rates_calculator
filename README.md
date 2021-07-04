# Exchange rates calculator

Script created to calculate currencies exchange rates for specific days. Script used to calculate proper amount of tax from dividends to pay to Polish Tax Office. Created using requests.


## Table of contents
* [Technologies](#technologies)
* [Setup](#setup)
* [Contact](#contact)

## Technologies
* Python version: 3.8.5

## Setup
To create virtual environment:
```
python3 -m venv venv
```

To activate virtual environment:
```
source venv/bin/activate
```

To install library:
```
pip install -r requirements.txt
```

Example input in Input.txt file:
```
04.01.2021	LYNX	ADP	2	USD
04.01.2021	LYNX	GPC	3	USD
05.01.2021	LYNX	BBY	3	USD
11.01.2021	LYNX	MO	5	USD
20.01.2021	LYNX	CSCO	7	USD
```

To run script:
```
python3 exchange_rates_converter.py
```

Example output in Output.txt file:
```
3.7584
3.7584
3.6998
3.6919
3.7416
```

## Contact
Created by Adam Misiak
