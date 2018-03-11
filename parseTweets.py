from empath import Empath
lexicon = Empath()

def searchTweets(twts):
	for tweet in twts:
		result = lexicon.analyze(tweet, categories=["violence", "hate", "aggression", "crime", "prison", "suffering", "kill", "irritability", 
		"death", "ridicule", "neglect", "fight", "injury", "rage", "sadness", "torment", "anger", "ugliness", "pain", "negative_emotion"], normalize=True)
		negEmotion = lexicon.analyze(tweet, categories=["negative_emotion"], normalize=True)
		print(result)
		print(negEmotion)