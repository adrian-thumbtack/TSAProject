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
    consumer_key = "FOwqj340c3ad38QA1rMhmhH5p"
    consumer_secret = "dq0Ofk0PzjOCWSOny53HtDcVTYlYjpEMN83Ri041J1dlXHK7qf"
    access_token = "3707523437-Ka8eBPi56wuxgd1IHnlIBH5Bp2n5VJzM6H1z4x9"
    access_secret = "5hwNEuCIZ5pECawUibd01WjoiHdIX9bvKezhNx6FjFZAE"
    if not sys.warnoptions:
        warnings.simplefilter("ignore")
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    return api
def get_tweets(api, name="realDonaldTrump"):
    tweets = []
    for status in tweepy.Cursor(api.user_timeline, screen_name="@{0}".format(name)).items():
        try:
            twt = re.search("(.*)(?:http)", unidecode(status._json["text"]).encode("utf-8"))
            if twt:
                twt = twt.group(1)
                tweets.append(twt)
        except:
            pass
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
serv.bind(("",8080))
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
