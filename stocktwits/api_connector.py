import requests
import settings

responses = []

for symbol in settings.TICKER_SYMBOLS:
    url = "{}/{}.json".format(settings.STOCKTWITS_API_URL, symbol)
    ticker_data = requests.get(url=url)
    for message in ticker_data.json()['messages']:
        responses.append(message['body'])

for message in responses:
    print(message)
