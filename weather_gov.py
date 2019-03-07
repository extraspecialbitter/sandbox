#!/usr/bin/python

# This script fetches the weather from the Weather.Gov API site and prints it out.

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
    print "%s [ mx | mi | fl | way | cc | rb | nyc | ca ]" % sys.argv[0]
    print "\n"
    sys.exit(1)
elif len(sys.argv) == 2:
    station = sys.argv[1]
    urlbase = 'https://api.weather.gov/points/'

    if station == 'mx':
        url_forecast = urlbase + 'geolookup/conditions/forecast/q/zmw:00000.3.WMMSL.json'
        url_sunrise  = urlbase + 'astronomy/q/zmw:00000.3.WMMSL.json'
    elif station == 'mi':
        url_forecast = urlbase + 'geolookup/conditions/forecast/q/MI/Munising.json'
        url_sunrise  = urlbase + 'astronomy/q/MI/Munising.json'
    elif station == 'fl':
        url_forecast = urlbase + 'geolookup/conditions/forecast/q/zmw:34101.1.99999.json'
        url_sunrise  = urlbase + 'astronomy/q/zmw:34101.1.99999.json'
    elif station == 'way':
        url_coord = urlbase + '42.3209,-71.3642'
    elif station == 'cc':
        url_forecast = urlbase + 'geolookup/conditions/forecast/q/zmw:02632.1.99999.json'
        url_sunrise  = urlbase + 'astronomy/q/zmw:02632.1.99999.json'
    elif station == 'rb':
        url_forecast = urlbase + 'geolookup/conditions/forecast/q/zmw:90277.1.99999.json'
        url_sunrise  = urlbase + 'astronomy/q/zmw:90277.1.99999.json'
    elif station == 'nyc':
        url_forecast = urlbase + 'geolookup/conditions/forecast/q/NY/NewYork.json'
        url_sunrise  = urlbase + 'astronomy/q/NY/NewYork.json'
    elif station == 'ca':
        url_forecast = urlbase + 'geolookup/conditions/forecast/q/pws:KCACAMBR16.json'
        url_sunrise  = urlbase + 'astronomy/q/pws:KCACAMBR16.json'
    else:
        print "\nThis station feed has not been implemented yet."
        print "\n"
        sys.exit(1)

# read in the JSON forecast data

f = urllib2.urlopen(url_coord)
json_string = f.read()
parsed_json = json.loads(json_string)

# start parsing current weather

location = parsed_json['properties']['relativeLocation']['properties']['city']
# c_time = parsed_json['current_observation']['observation_time']
# weather = parsed_json['current_observation']['weather']
# temp_f = parsed_json['current_observation']['temp_f']
# wind_mph = parsed_json['current_observation']['wind_mph']
# humidity = parsed_json['current_observation']['relative_humidity']
# forecast_date = parsed_json['forecast']['txt_forecast']['date']
# forecast_array = parsed_json['forecast']['txt_forecast']['forecastday']

# and print

print "\nWeather in %s" % (location)
# print "    Currently: %s, %s" % (weather, temp_f)
# print "         Wind: %s mph" % (wind_mph)
# print "     Humidity: %s\n" % (humidity)
# print "Forecast:"
# print "Date: %s" % (forecast_date)
# print "Debug: %s" % (forecast_array)

# parse and print the forecast

# for i in range(0, 8):
#     forecast_title = parsed_json['forecast']['txt_forecast']['forecastday'][i]['title']
#     forecast_data  = parsed_json['forecast']['txt_forecast']['forecastday'][i]['fcttext']
#     print "    %s: %s" % (forecast_title, forecast_data)
# print "\n"
f.close()

