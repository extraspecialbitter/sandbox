#!/usr/bin/env ruby

require "rubygems"
require "nokogiri"
 
class PlainTextExtractor < Nokogiri::XML::SAX::Document
 
  attr_reader :plaintext
 
  # Initialize the state of interest variable with false
  def initialize
    @interesting = false
    @plaintext = ""
  end
 
  # This method is called whenever a comment occurs and
  # the comments text is passed in as string.
  def comment(string)
    case string.strip       # strip leading and trailing whitespaces
    when /^body="start"/     # match starting comment
      @interesting = true
    when /^body="end"/
      @interesting = false  # match closing comment
    end
  end
 
  # This callback method is called with any string between
  # a tag.
  def characters(string)
    @plaintext << string if @interesting
  end
end
 
pte = PlainTextExtractor.new
parser = Nokogiri::HTML::SAX::Parser.new(pte)
parser.parse_file ARGV[0]
puts pte.plaintext
