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
    print "%s [ mi | fl | way | cc | rb | nyc ]" % sys.argv[0]
    print "\n"
    sys.exit(1)
elif len(sys.argv) == 2:
    station = sys.argv[1]
    urlbase = 'https://api.weather.gov/points/'

    if station == 'mi':
        url_coord = urlbase + '46.4116,-86.655'
    elif station == 'fl':
        url_coord = urlbase + '26.142,-81.7948'
    elif station == 'way':
        url_coord = urlbase + '42.3209,-71.3642'
    elif station == 'cc':
        url_coord = urlbase + '41.6488,-70.348'
    elif station == 'rb':
        url_coord = urlbase + '33.845,-118.3872'
    elif station == 'nyc':
        url_coord = urlbase + '40.7128,-74.006'
    else:
        print "\nThis station feed has not been implemented yet."
        print "\n"
        sys.exit(1)

# read in the JSON metadata

f = urllib2.urlopen(url_coord)
json_string = f.read()
parsed_json = json.loads(json_string)

# start parsing metadata

city = parsed_json['properties']['relativeLocation']['properties']['city']
state = parsed_json['properties']['relativeLocation']['properties']['state']

# print location

print "\nForecast for %s, %s" % (city, state)

# read in forecast data

url_forecast = parsed_json['properties']['forecast']
f.close()

g = urllib2.urlopen(url_forecast)
json_string = g.read()
parsed_json = json.loads(json_string)

# parse forecast data

# print "    Currently: %s, %s" % (weather, temp_f)
# print "         Wind: %s mph" % (wind_mph)
# print "     Humidity: %s\n" % (humidity)
# print "Forecast:"
# print "Date: %s" % (forecast_date)
# print "Debug: %s" % (forecast_array)

# parse and print the forecast

for i in range(0, 6):
    forecast_title = parsed_json['properties']['periods'][i]['name']
    forecast_data  = parsed_json['properties']['periods'][i]['detailedForecast']
    print "    %s: %s" % (forecast_title, forecast_data)
print "\n"
g.close()

