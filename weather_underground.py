#!/usr/bin/python

# This script fetches the weather from the WeatherUnderground RSS feed and prints it out.

import urllib
from xml.etree.cElementTree import parse
from datetime import datetime, timedelta
import os
from os.path import join
from sys import argv
try:
    import cPickle as pickle
except ImportError:
    import pickle

#Usage: weather_underground.py 

RSS_FEED_URL = 'http://api.wunderground.com/api/2ad1a5da2e974bd8/geolookup/conditions/forecast/q/MA/Wayland.xml'

if RSS_FEED_URL == '':
    print 'Edit the script to specify'
    print 'your RSS feed URL from'
    print 'http://api.wunderground.com'
    exit
end

rss = parse(urllib.urlopen(url)).getroot()

begin
    xml = XmlSimple.xml_in(text)
    current_observation = xml['current_observation'][0]
rescue
    puts "Error: Could not parse the XML!"
    exit
end

puts "Weather (" + current_observation['observation_time'][0].sub(/..., \d\d ... \d\d\d\d /,'') + '):'
puts "    Currently: " + current_observation['weather'][0] + ", " + current_observation['temp_f'][0] + " F"
puts "     Humidity: " + current_observation['relative_humidity'][0] 
puts "         Wind: " + current_observation['wind_mph'][0] + " mph"
puts "    Barometer: " + current_observation['pressure_in'][0] + " in"
# puts "      Sunrise: " + current_observation['astronomy'][0]['sunrise']
# puts "       Sunset: " + current_observation['astronomy'][0]['sunset']

begin
    xml = XmlSimple.xml_in(text)
    forecast = xml['forecast'][0]
rescue
    puts "Error: Could not parse the XML!"
    exit
end

puts " "
# puts "Forecast (As of " + forecast['txt_forecast'][0]['date'][0] + "):"
(0..7).each do |i|
    puts "       " + forecast['txt_forecast'][0]['forecastdays'][0]['forecastday'][i]['title'][0] + ": " + forecast['txt_forecast'][0]['forecastdays'][0]['forecastday'][i]['fcttext'][0]
end
