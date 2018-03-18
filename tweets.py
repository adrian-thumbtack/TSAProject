import tweepy
from tweepy import OAuthHandler
import re
from unidecode import unidecode
import sys
import warnings

def initialize():
    consumer_key = "lBd0fokEEx2ncJCZUEWVLIUN8"
    consumer_secret = "AcQ2C1idexoxb0msBycqid2H1QbdtKZXRJh0cMPkpUAaKEWrC6"
    access_token = "4142122823-8mPPgiEnFIEK4MMPGtmaJ8bhxY7rBLP0IdrAN5e"
    access_secret = "MTyQVvSLkq2OUVbHEVXDTIY58eFgLCvRLyZmvOpcCEx0i"

    if not sys.warnoptions:
        warnings.simplefilter("ignore")

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)
    return api

def get_tweets(api, name="realDonaldTrump"):
    tweets = []
    for status in tweepy.Cursor(api.user_timeline, screen_name="@{0}".format(name)).items():
        twt = re.search("(.*)(?:http)", unidecode(status._json["text"]).encode("utf-8"))
        if twt:
            twt = twt.group(1)
            tweets.append(twt)
    return tweets

# test code
# if __name__ == "__main__":
#     api = initialize()
#     twts = get_tweets(api)
