#!/usr/bin/env ruby

require "nokogiri"

class PlainTextExtractor < Nokogiri::XML::SAX::Document
  attr_reader :plaintext
  # Initialize the state of interest variable with false
  def initialize
    @interesting = false
    @pre = false
    @plaintext = ""
  end

  def start_element(name, attrs = [])
    if name == "pre"
      @pre = true
    end
  end

  def end_element(name, attrs = [])
    if name == "pre"
      @pre = false
    end
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
    if @interesting and not @pre
      @plaintext << string
    end
  end
end

fname = ARGV[0]
start_column = 4
end_column = 6

target_range = (start_column-1)..(end_column-1)

IO.foreach(fname) do |line|
  if line.match(/<dfn>Date<\/dfn>/)
    pieces = line.split(" ")

    @date_string = pieces[target_range].join("-")
#   puts @date_string
  end
end

pte = PlainTextExtractor.new
parser = Nokogiri::HTML::SAX::Parser.new(pte)
parser.parse_file ARGV[0]

# puts pte.plaintext

begin
  file = File.open("snippet.txt", "w")
  file.write(@date_string) 
  file.write(pte.plaintext) 
rescue IOError => e
  #some error occur, dir not writable etc.
ensure
  file.close unless file == nil
end
