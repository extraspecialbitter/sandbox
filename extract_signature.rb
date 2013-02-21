#!/usr/bin/env ruby

require 'nokogiri'

doc = Nokogiri.HTML(ARGV[0])

my_xpath = 
"/html/body/comment()[1]/following-sibling::*[not(self::pre)]"

catch :found_ending_text do
  doc.xpath(my_xpath).each do |node|
    node.children.each do |child|
      text = child.text
      throw :found_ending_text if text.include? %q{body="end"}
      next if text.empty?
      puts text.strip
    end
  end
end
