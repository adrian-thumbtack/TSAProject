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
		negResult = lexicon.analyze(tweet, categories=["negative_emotion"])
		print(negResult)
		a.append(sum(negResult.values())
	return sum(a)
		
def searchForPos(twts):
	a = []
	for tweet in twts:
		posResult = lexicon.analyze(tweet, categories=["positive_emotion"])
		print(posResult)
		a.append(sum(posResult.values())
	return sum(a)
		