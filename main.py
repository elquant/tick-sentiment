from twitter.api_connector import TwitterConnector
from twitter.inbound_stream import StreamListener
import settings
import tweepy

def connect_to_twitter():
    print("Establishing connection with Twitter API...")
    api = TwitterConnector()
    stream_listener = StreamListener()
    stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
    stream.filter(track=settings.TRACK_KEYWORDS)
    print("Streaming from Twitter API is now active.")    
    
def connect_to_stocktwits():
    print("Establishing connection with StockTwits API...")
    print("Streaming from StockTwits API is now active.")
    
if __name__ == '__main__':
    connect_to_twitter()
    connect_to_stocktwits()
