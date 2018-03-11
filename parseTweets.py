from empath import Empath
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
		negResult = lexicon.analyze(tweet, categories=["violence", "hate", "aggression", "crime", "prison", "suffering", "kill", "irritability", "death", "ridicule", "neglect", "fight", "injury", "rage", "sadness", "torment", "anger", "ugliness", "pain", "negative_emotion"])
		print(negResult)
		a.append(sum(negResult.values())/len(negResult))
	return sum(a)
		
def searchForPos(twts):
	a = []
	for tweet in twts:
		posResult = lexicon.analyze(tweet, categories=["cheerfulness", "family", "pride", "leisure", "exercise", "celebration","love", "trust", "politeness", "optimism", "joy", "affection", "friends", "achievement", "contentment", "positive_emotion"])
		print(posResult)
		a.append(sum(posResult.values())/len(posResult))
	return sum(a)
		