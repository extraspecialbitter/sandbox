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

# read in the longitude and latitude coordinates

f = urllib2.urlopen(url_coord)
json_string = f.read()
parsed_json = json.loads(json_string)
f.close()

# parse for and print location

city = parsed_json['properties']['relativeLocation']['properties']['city']
state = parsed_json['properties']['relativeLocation']['properties']['state']
print "\n            %s, %s" % (city, state)

# read in forecast and observation station URLs

url_stations = parsed_json['properties']['observationStations']

# read in observation station data

g = urllib2.urlopen(url_stations)
json_string = g.read()
parsed_json = json.loads(json_string)
g.close()

# get station ID

station_id = parsed_json['features'][0]['id']
url_observation = station_id + '/observations/latest'

# read in observed data

h = urllib2.urlopen(url_observation)
json_string = h.read()
parsed_json = json.loads(json_string)
h.close()

current_desc = parsed_json['properties']['textDescription']
current_temp_c = parsed_json['properties']['temperature']['value']
current_temp_f = 9.0/5.0 * current_temp_c + 32
current_temp_f = int(round(current_temp_f))
print "            %s, %s" % (current_desc, current_temp_f)

# print "  Wind: %s mph" % (wind_mph)
# print "  Humidity: %s\n" % (humidity)

print "\n"
