from twitter_api.api_connector import TwitterConnector
from twitter_api.inbound_stream import StreamListener
import settings
import tweepy

if __name__ == '__main__':
    api = TwitterConnector()
    stream_listener = StreamListener()
    stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
    stream.filter(track=settings.TRACK_KEYWORDS)
    print("Streaming from Twitter API is now active.")
