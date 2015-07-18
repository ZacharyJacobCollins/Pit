require 'java'
require_relative "../libs/stanford-corenlp-full-2015-04-20/stanford-corenlp-3.5.2.jar"
class CentralBody
  @responses = []
  def appendResponse(x)
    @responses << x
  end
end
