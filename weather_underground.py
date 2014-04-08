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

# start parsing for individual fields

location = parsed_json['location']['city']
c_time = parsed_json['current_observation']['observation_time']
weather = parsed_json['current_observation']['weather']
temp_f = parsed_json['current_observation']['temp_f']
wind_mph = parsed_json['current_observation']['wind_mph']
humidity = parsed_json['current_observation']['relative_humidity']
# forecast_title = parsed_json['forecast']['title']
# forecast_data = parsed_json['forecast']['fcttext']

# and print

print "\n"
print "Weather in %s (%s)\n" % (location, c_time)
print "Currently: %s, %s" % (weather, temp_f)
print "Wind: %s mph" % (wind_mph)
print "Humidity: %s\n" % (humidity)
# print "%s: %s" (forecast_title, forecast_data)
print "\n"
f.close()

# puts " "
# puts "Forecast (As of " + forecast['txt_forecast'][0]['date'][0] + "):"
# (0..7).each do |i|
#     puts "       " + forecast['txt_forecast'][0]['forecastdays'][0]['forecastday'][i]['title'][0] + ": " + forecast['txt_forecast'][0]['forecastdays'][0]['forecastday'][i]['fcttext'][0]
# end
