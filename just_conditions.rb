#!/usr/bin/ruby
require 'net/http'
require 'xmlsimple'

# This script fetches the weather from the Yahoo! Weather RSS feed and prints it out.
# This can be used for Conky, for example.
# By Brian Carper
# http://briancarper.net

RSS_FEED_URL = 'http://xml.weather.yahoo.com/forecastrss?p=02451&u=Fahrenheit'

if RSS_FEED_URL == '' then
    puts 'Edit the script to specify'
    puts 'your RSS feed URL from'
    puts 'http://weather.yahoo.com'
    exit
end

begin
    text = Net::HTTP.get(URI.parse(RSS_FEED_URL))
rescue
    puts "ERROR: Failed fetching RSS feed!"
    exit
end

begin
    xml = XmlSimple.xml_in(text)
    channel = xml['channel'][0]
rescue
    puts "Error: Could not parse the XML!"
    exit
end

temp_units = ' ' + channel['units'][0]['temperature']
baro_units = ' ' + channel['units'][0]['pressure']
wind_units = ' ' + channel['units'][0]['speed']

puts "    " + channel['item'][0]['condition'][0]['text'] + ', ' + channel['item'][0]['condition'][0]['temp'] + temp_units
