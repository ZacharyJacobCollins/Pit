from textblob import TextBlob
class Sentence: 
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
    def getNouns(self):
        nouns = []
        for word in self.words:
            if self.getPos(word) == "Noun":
                nouns.append(word)
        return nouns
    def __init__(self,string):
        s = TextBlob(string)
        self.PartOfSpeech = {}
        for tag in s.tags:
            self.PartOfSpeech[tag[0]] = tag[1]
        self.words = s.words
        self.nouns = self.getNouns()