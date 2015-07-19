from textblob import TextBlob
class Sentence:
    def getNouns(self):
        for word in self.PartOfSpeech.keys():
            if self.getPos(word) == "Noun":
                self.nouns.append(word)
    def getPos(self,word):
        if word in self.words:
            term = self.PartOfSpeech[word]
            if term in ("NN","NNS","NNP","JJS"):
                return "Noun"
            if term in ("JJ","JJR","JJS"):
                return "Adjective"
            if term in ("VB","VBD","VBG","VBN","VBP","VBZ"):
                return "Verb"
            if term in ("RB","RBR","RBS"):
                return "Adverb"
            return None
        else:
            return None
    def __init__(self,string):
        self.s = TextBlob(string)
        self.PartOfSpeech = {}
        for tag in self.s.tags:
            self.PartOfSpeech[tag[0]] = tag[1]
        self.words = self.s.words
        self.nouns = []
        self.getNouns()
