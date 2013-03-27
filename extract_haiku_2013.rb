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

require "nokogiri"

doc = Nokogiri::HTML(@haiku_text)
# doc.xpath('//address/following-sibling::p//text()').each {|n| p n}
output = @date_string + $/
doc.xpath('//address/following-sibling::p//text()').each { |line| output << ( line.text.strip + $/ ) }

File.write("snippet.txt", output)
