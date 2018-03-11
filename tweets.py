import tweepy
from tweepy import OAuthHandlerac
from unidecode import unidecode

consumer_key = 'lBd0fokEEx2ncJCZUEWVLIUN8'
consumer_secret = 'AcQ2C1idexoxb0msBycqid2H1QbdtKZXRJh0cMPkpUAaKEWrC6'
access_token = '4142122823-8mPPgiEnFIEK4MMPGtmaJ8bhxY7rBLP0IdrAN5e'
access_secret = 'MTyQVvSLkq2OUVbHEVXDTIY58eFgLCvRLyZmvOpcCEx0i'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

for status in tweepy.Cursor(api.user_timeline, screen_name='@realDonaldTrump').items():
    print unidecode(status._json['text']).encode('utf-8')
