import requests
import settings

responses = []

for symbol in settings.TICKER_SYMBOLS:
    ticker_data = requests.get(url="https://api.stocktwits.com/api/2/streams/symbol/{}.json".format(symbol))
    for message in ticker_data.json()['messages']:
        responses.append(message['body'])

for message in responses:
    print(message)
