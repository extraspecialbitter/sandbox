#!/usr/bin/python

# This script fetches sunrise and sunset times from the WeatherUnderground RSS feed and prints it out.

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

if len(sys.argv) > 2:
    print "\nUsage:"
    print "%s [ mx | tx | mi | az | fl ]" % sys.argv[0]
    print "\n"
    sys.exit(1)
elif len(sys.argv) == 2:
    station = sys.argv[1]

# implementing a case statement using a dictionary 
    def austin():
        return 'http://api.wunderground.com/api/2ad1a5da2e974bd8/astronomy/q/TX/Austin.json'
    def pescadero():
        return 'http://api.wunderground.com/api/2ad1a5da2e974bd8/astronomy/q/zmw:00000.3.WMMSL.json'
    def munising():
        return 'http://api.wunderground.com/api/2ad1a5da2e974bd8/astronomy/q/MI/Munising.json'
    def phoenix():
        return 'http://api.wunderground.com/api/2ad1a5da2e974bd8/astronomy/q/AZ/Phoenix.json'
    def naples():
        return 'http://api.wunderground.com/api/2ad1a5da2e974bd8/astronomy/q/zmw:34101.1.99999.json'
    def nowhere():
        return 'nowhere'

    case_dictionary = {
        'tx' : austin,
        'mx' : pescadero,
        'mi' : munising,
        'az' : phoenix,
        'fl' : naples }
    RSS_FEED_URL = case_dictionary.get(station, nowhere)()

else:
    RSS_FEED_URL = 'http://api.wunderground.com/api/2ad1a5da2e974bd8/astronomy/q/MA/Wayland.json'

# error on unimplemented feed

if RSS_FEED_URL == 'nowhere':
   print "\nThis station feed has not been implemented yet."
   print "\n"
   sys.exit(1)

# read in the JSON data

f = urllib2.urlopen(RSS_FEED_URL)
json_string = f.read()
parsed_json = json.loads(json_string)

# start parsing JSON data

moon = parsed_json['moon_phase']['phaseofMoon']
sunrise_hour = parsed_json['sun_phase']['sunrise']['hour']
sunrise_minute = parsed_json['sun_phase']['sunrise']['minute']
sunset_hour = parsed_json['sun_phase']['sunset']['hour']
sunset_minute = parsed_json['sun_phase']['sunset']['minute']

# and print

print "\n    Moon phase is %s " % (moon)
print "    Sunrise: %s:%s" % (sunrise_hour, sunrise_minute)
print "    Sunset: %s:%s" % (sunset_hour, sunset_minute)

print "\n"
f.close()

