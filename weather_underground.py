#!/usr/bin/python

# This script fetches the weather from the WeatherUnderground RSS feed and prints it out.

from datetime import datetime, timedelta
from sys import argv
from os.path import join
import urllib2
import commands, os, socket, subprocess
import time
import getopt
import sys 
import os
import json

if len(argv) > 2:
    print "Usage:"
    print "%s [ mx | tx | up ]" % sys.argv[0]
    print "\n"
    sys.exit(1)

RSS_FEED_URL = 'http://api.wunderground.com/api/2ad1a5da2e974bd8/geolookup/conditions/forecast/q/MA/Wayland.json'

if RSS_FEED_URL == '':
    print "Edit the script to specify"
    print "your RSS feed URL from"
    print "http://api.wunderground.com"
    print "\n"
    sys.exit(1)

# read in the JSON data

f = urllib2.urlopen(RSS_FEED_URL)
json_string = f.read()
parsed_json = json.loads(json_string)
location = parsed_json['location']['city']
temp_f = parsed_json['current_observation']['temp_f']
print "Current temperature in %s is: %s" % (location, temp_f)
f.close()
# rss_string = rss.read()
# print "%s" % rss_string
# soup = BeautifulStoneSoup(rss_string)
# print "%s" % soup
# forecasts = []
# for element in rss.findall('current_observation/item/{%s}forecast':
#   forecasts.append(dict(element.items()))

# print "Weather  + %s" % current_observation['observation_time']
# print "    Currently: " + current_observation['weather'] + ", " + current_observation['temp_f'] + " F"
# puts "     Humidity: " + current_observation['relative_humidity'][0] 
# puts "         Wind: " + current_observation['wind_mph'][0] + " mph"
# puts "    Barometer: " + current_observation['pressure_in'][0] + " in"
# puts "      Sunrise: " + current_observation['astronomy'][0]['sunrise']
# puts "       Sunset: " + current_observation['astronomy'][0]['sunset']

# puts " "
# puts "Forecast (As of " + forecast['txt_forecast'][0]['date'][0] + "):"
# (0..7).each do |i|
#     puts "       " + forecast['txt_forecast'][0]['forecastdays'][0]['forecastday'][i]['title'][0] + ": " + forecast['txt_forecast'][0]['forecastdays'][0]['forecastday'][i]['fcttext'][0]
# end
