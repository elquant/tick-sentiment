import tweepy
import dataset
import settings
import json
from textblob import TextBlob
from sqlalchemy.exc import ProgrammingError


class DataStore():

    def __init__(self):
        self._db = dataset.connect(settings.CONNECTION_STRING)

    def on_tweet(self, tweet, tweet_sentiment):
        description = tweet.user.description
        loc = tweet.user.location
        text = tweet.text
        coords = tweet.coordinates
        geo = tweet.geo
        name = tweet.user.screen_name
        user_created = tweet.user.created_at
        followers = tweet.user.followers_count
        id_str = tweet.id_str
        created = tweet.created_at
        retweets = tweet.retweet_count
        bg_color = tweet.user.profile_background_color
        if geo is not None:
            geo = json.dumps(geo)

        if coords is not None:
            coords = json.dumps(coords)

        try:
            table = self._db[settings.TABLE_NAME]
            table.insert(dict(
                user_description=description,
                user_location=loc,
                coordinates=coords,
                text=text,
                geo=geo,
                user_name=name,
                user_created=user_created,
                user_followers=followers,
                id_str=id_str,
                created=created,
                retweet_count=retweets,
                user_bg_color=bg_color,
                polarity=tweet_sentiment.polarity,
                subjectivity=tweet_sentiment.subjectivity,
            ))
        except ProgrammingError as err:
            print(err)


class StreamListener(tweepy.StreamListener):

    def __init__(self):
        self._data_store = DataStore()
        tweepy.StreamListener.__init__(self)

    def on_status(self, status):
        if hasattr(status, "retweeted_status"):
            return
        blob = TextBlob(status.text)
        self._data_store.on_tweet(tweet=status, tweet_sentiment=blob.sentiment)

    def on_error(self, status_code):
        if status_code == 420:
            return False
