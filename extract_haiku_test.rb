#!/usr/bin/env ruby

# some initializations

@interesting = false
@haiku_text = ""

# read the file between the two "body" tags

fname = ARGV[0]

IO.foreach(fname) do |line|
  if line.match(/body="start"/)
    @interesting = true
  end

# meanwhile let's grab the date string and process it

  start_column = 4
  end_column = 6

  target_range = (start_column-1)..(end_column-1)

  if line.match(/<dfn>Date<\/dfn>/)
    pieces = line.split(" ")
    @date_string = pieces[target_range].join("-")
  end

  if line.match(/body="end"/)
    @interesting = false
  end

  if @interesting 
    @haiku_text << line
  end
end
# puts @haiku_text

require "nokogiri"

doc = Nokogiri::HTML(@haiku_text)
doc.xpath('//address/following-sibling::p//text()').each {|n| p n}

# puts doc

begin
  file = File.open("snippet.txt", "w")
  file.write(@date_string) 
# file.write(@haiku_text) 
rescue IOError => e
  #some error occur, dir not writable etc.
ensure
  file.close unless file == nil
end
