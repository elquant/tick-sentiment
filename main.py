import twitter
import settings
import tweepy

from utils import to_cash_tag
from twitter.inbound_processor import StreamListener


def connect_to_twitter():
    print("Establishing connection to Twitter API...")
    stream_listener = StreamListener()
    stream = tweepy.Stream(auth=twitter.api.auth, listener=stream_listener, daemon=True)
    stream.filter(track=map(to_cash_tag, settings.TICKER_SYMBOLS), is_async=True)


def connect_to_stocktwits():
    print("Establishing connection to StockTwits API...")


if __name__ == '__main__':
    connect_to_twitter()
    connect_to_stocktwits()
    input("Press enter to finish the program...")
