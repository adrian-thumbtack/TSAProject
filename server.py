import socket
from empath import Empath
import tweepy
from tweepy import OAuthHandler
import re
from unidecode import unidecode
import sys
import warnings

FINALVERSION = False #if its final version, errors will be caught

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
        twt = re.search("(.*)(?:http)", status._json["text"])
        if twt:
            twt = twt.group(1)
            tweets.append(twt)
    return tweets

lexicon = Empath()
def getScore(twts):
	negScore = searchForNeg(twts)
	posScore = searchForPos(twts)
	print(negScore)
	print(posScore)
	print ((negScore - posScore))
def searchForNeg(twts):
	a = []
	for tweet in twts:
		negResult = lexicon.analyze(tweet, categories=["negative_emotion"])
		print(negResult)
		a.append(sum(negResult.values()))
	return sum(a)
def searchForPos(twts):
	a = []
	for tweet in twts:
		posResult = lexicon.analyze(tweet, categories=["positive_emotion"])
		print(posResult)
		a.append(sum(posResult.values()))
	return sum(a)

filesToSend = {
	b"style.css":b"css",
	b"media/header.jpg":b"jpeg",
	b"about.html":b"html",
	b"favicon.ico":b"ico"
}
defaultFile = [b"depression.html",b"html"]
def sendFile(conn,filename,type):
	conn.send(type)
	conn.send(b"\n\n")
	f = open(filename,"rb")
	conn.send(f.read())
	f.close()
def handler(conn):
	data = conn.recv(1024)
	conn.send(b"HTTP/1.1 200 OK\nContent-type: text/")
	sentSomething = False
	for filename,type in filesToSend.items():
		if data.find(filename) != -1:
			sentSomething = True
			sendFile(conn,filename,type)
			break
	if not sentSomething:
		if data.find(b"results.html") != -1:
			t = b"?twitterhandle="
			s = data.find(t)
			handle = data[s+len(t):data.find(b" ",s)]
			conn.send(b"html\n\n")
			f = open("results.html","rb")
			conn.send(f.read().replace(b"[DEPRESSIONLVL]",getScore(get_tweets(initialize(),handle))))
			f.close()
		else:
			sendFile(conn,defaultFile[0],defaultFile[1])
	conn.close()

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(("",80))
serv.listen(65)
processes = []
while True:
    conn,_ = serv.accept()
    if FINALVERSION:
        try: handler(conn)
        except: pass
    else:
        handler(conn)
serv.close()
