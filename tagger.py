from sentence import Sentence
from textblob import TextBlob
from itertools import chain
from collections import Counter
def findSubject(lines):
    sentences = []
    if len(lines) == 0:
        print "messages are empty"
        return None
    for m in lines:
        nouns = Sentence(m).nouns
        if len(nouns) > 0:
            sentences.append(nouns)
    if len(sentences) != 0:
        maxNoun = Counter(list(chain(*sentences))).most_common()[0]
    else:
        print "No nouns"
        return None
    if maxNoun[1] >= 2:
        return maxNoun[0].replace(" ","_")
    else:
        return None