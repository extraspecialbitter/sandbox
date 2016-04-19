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

# parse arguments

if len(sys.argv) != 2:
    print "\nUsage:"
    print "%s [ mx | tx | mi | az | fl | way | rb | nyc | ca ]" % sys.argv[0]
    print "\n"
    sys.exit(1)
elif len(sys.argv) == 2:
    station = sys.argv[1]
    urlbase = 'http://api.wunderground.com/api/2ad1a5da2e974bd8/'

    if station == 'tx':
        url_forecast = urlbase + 'geolookup/conditions/forecast/q/TX/Austin.json'
    elif station == 'mx':
        url_forecast = urlbase + 'geolookup/conditions/forecast/q/zmw:00000.3.WMMSL.json'
    elif station == 'mi':
        url_forecast = urlbase + 'geolookup/conditions/forecast/q/MI/Munising.json'
    elif station == 'az':
        url_forecast = urlbase + 'geolookup/conditions/forecast/q/AZ/Phoenix.json'
    elif station == 'fl':
        url_forecast = urlbase + 'geolookup/conditions/forecast/q/zmw:34101.1.99999.json'
    elif station == 'way':
        url_forecast = urlbase + 'geolookup/conditions/forecast/q/MA/Wayland.json'
    elif station == 'rb':
        url_forecast = urlbase + 'geolookup/conditions/forecast/q/zmw:90277.1.99999.json'
    elif station == 'nyc':
        url_forecast = urlbase + 'geolookup/conditions/forecast/q/NY/NewYork.json'
    elif station == 'ca':
        url_forecast = urlbase + 'geolookup/conditions/forecast/q/pws:KCACAMBR16.json'
    else:
        print "\nThis station feed has not been implemented yet."
        print "\n"
        sys.exit(1)

# read in the JSON forecast data

f = urllib2.urlopen(url_forecast)
json_string = f.read()
parsed_json = json.loads(json_string)

# start parsing current weather

location = parsed_json['location']['city']
c_time = parsed_json['current_observation']['observation_time']
weather = parsed_json['current_observation']['weather']
temp_f = parsed_json['current_observation']['temp_f']
wind_mph = parsed_json['current_observation']['wind_mph']
humidity = parsed_json['current_observation']['relative_humidity']
forecast_date = parsed_json['forecast']['txt_forecast']['date']
forecast_array = parsed_json['forecast']['txt_forecast']['forecastday']

# and print

print "\nWeather in %s" % (location)
print "    Currently: %s, %s" % (weather, temp_f)
print "         Wind: %s mph" % (wind_mph)
print "     Humidity: %s\n" % (humidity)

print "\n"

