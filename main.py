from twitter.api_connector import TwitterConnector
from twitter.inbound_processor import StreamListener
import settings
import tweepy


def connect_to_twitter():
    print("Establishing connection to Twitter API...")
    api = TwitterConnector()
    stream_listener = StreamListener()
    stream = tweepy.Stream(auth=api.auth,
                           listener=stream_listener,
                           daemon=True)
    stream.filter(track=settings.TRACK_KEYWORDS,
                  is_async=True)


def connect_to_stocktwits():
    print("Establishing connection to StockTwits API...")


if __name__ == '__main__':
    connect_to_twitter()
    connect_to_stocktwits()
    input("Press enter to finish the program...")
