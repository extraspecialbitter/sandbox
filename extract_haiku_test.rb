#!/usr/bin/env ruby

require "nokogiri"

# get the date

doc = Nokogiri::HTML File.read(ARGV[0])
output = doc.css('span[@id="date"]').first.text[/\d+ \w+ \d+/].gsub(' ','-') + $/

# get the remaining text

path = '//address/following-sibling::p//text()'
doc.xpath(path).each { |line| output << line.text.strip << $/ }

File.write("snippet.txt", output)
