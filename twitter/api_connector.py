import private
import tweepy


class TwitterConnector():

    def __init__(self):
        self.auth = tweepy.OAuthHandler(private.TWITTER_APP_KEY,
                                        private.TWITTER_APP_SECRET)
        self.auth.set_access_token(private.TWITTER_KEY,
                                   private.TWITTER_SECRET)
        self.api = tweepy.API(self.auth)
