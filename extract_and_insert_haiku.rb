#!/usr/bin/env ruby

require "nokogiri"

require 'mysql'

begin
    con = Mysql.new 'localhost', 'root', 'menagerie', 'haiku_archive'

    con.query("CREATE TABLE IF NOT EXISTS \
        archive_2012(haiku_text VARCHAR(120) not null, date_written CHAR(12) not null)")

rescue Mysql::Error => e
    puts e.errno
    puts e.error

ensure
    con.close if con
end

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
start_column = 3
end_column = 5

target_range = (start_column-1)..(end_column-1)

IO.foreach(fname) do |line|
  if line.match(/<strong>Date:<\/strong>/)
    pieces = line.split(" ")

    date_string = pieces[target_range].join("-")
    puts date_string
#   con.query("INSERT INTO archive_2012(date_written) VALUES(%{date_string})")
  end
end

pte = PlainTextExtractor.new
parser = Nokogiri::HTML::SAX::Parser.new(pte)
parser.parse_file ARGV[0]

puts pte.plaintext
# con.query("INSERT INTO archive_2012(haiku_text) VALUES(%{pte.plaintext})")
