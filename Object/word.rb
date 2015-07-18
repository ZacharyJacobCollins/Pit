require 'java'
require_relative "../libs/ritaWN.jar"
wordNet = Java::RitaWordnet::RiWordnet
class Word
  attr_accessor :word, :transposition, :sentiment,:questionType,
  :hypernyms,:holonyms,:synonyms,:antonyms,:similar,:examples,:PartOfSpeech
  def initialize(word)
    return nil if !word.is_a?(String)
    @word = word
    @PartOfSpeech = wordNet.getBestPos(@word)
  end
  def getHyponym
    @hypernums = wordNet.getAllHyponyms(@word,@PartOfSpeech)
  end
  def getHypernyms
    @hyponyms = wordNet.getAllHyponyms(@word,@PartOfSpeech)
  end
  def getHolonyms
    @holonyms = wordNet.getAllHolonyms(@word,@PartOfSpeech)
  end
  def getSynonyms
    @synonyms = wordNet.getAllSynonyms(@word,@PartOfSpeech)
  end
  def getAntonyms
    @antonyms = wordNet.getAntonyms(@word,@PartOfSpeech)
  end
  def getSimilar
    @similar = wordNet.getAllSimilar(@word,@PartOfSpeech)
  end
  def setQuestionType
    questionType = case @PartOfSpeech.type
      when "NN","NNS","VBD","JJ" then "what"
      when "RB" then "how"
      when "NNP","PRP" then "who"
      when /PRG\\$/ then "whose"
      when "PDT","DT" then "which"
      when "RBR","RBS","JJR" then "compared to what"
      when "EX","IN" then "where"
      when "FW" then "which language"
      else "what what"
    end
  end
end
