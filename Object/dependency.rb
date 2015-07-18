class Dependency
  attr_reader :type,:governor,:dependent
  def initialize(type,governor,dependent)
    @type = type
    @governor = governor
    @dependent = dependent
  def toString
    puts "[Type #{@type}] [Governnor #{@governor}] [Dependent #{@dependent}]"
  end
  def compare(other)
    other.ToString == self.ToString
  end
end
