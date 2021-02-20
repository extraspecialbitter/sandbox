#!/usr/bin/python

# This script fetches the weather from the openweathermap.org API site and prints it out.

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

urlbase = 'https://api.openweathermap.org/data/2.5/weather'
api_key = 'c4a0b83ccd51f7b1d44d35419710b2b1'

# parse arguments

if len(sys.argv) != 2:
    print "\nUsage:"
    print "%s [ mi | mx | pr | way | cc | ym | bos | nyc | ca | rb | li ]" % sys.argv[0]
    print "\n"
    sys.exit(1)
elif len(sys.argv) == 2:
    station = sys.argv[1]

    if station == 'cc':
        city_id = '4929771'
    elif station == 'mx':
        city_id = '3985710'
    elif station == 'ym':
        city_id = '4956335'
    elif station == 'mi':
        city_id = '5000947'
    elif station == 'way':
        city_id = '4937230'
    elif station == 'rb':
        city_id = '5386785'
    elif station == 'ca':
        city_id = '5402405'
    elif station == 'li':
        city_id = '5116060'
    elif station == 'bos':
        city_id = '4931972'
    elif station == 'nyc':
        city_id = '5128581'
    elif station == 'pr':
        city_id = '4568127'
    else:
        print "\nThis station feed has not been implemented yet."
        print "\n"
        sys.exit(1)

# read in the longitude and latitude coordinates

url_query = urlbase + '?id=' + city_id + '&appid=' + api_key
f = urllib2.urlopen(url_query)
json_string = f.read()
parsed_json = json.loads(json_string)
f.close()

# print "\njson string: %s" % (json_string)
# print "\nparsed json: %s" % (parsed_json)

# parse for and print location

city = parsed_json['name']
country = parsed_json['sys']['country']
print "\nCurrent weather for %s, %s:" % (city, country)

# parse for weather description and temperature

weather_desc = parsed_json['weather'][0]['main']
# weather_desc2 = parsed_json['weather'][0]['description']
kelvin_temp = parsed_json['main']['temp']
celsius_temp = kelvin_temp - 273.15
fahrenheit_temp = celsius_temp * 1.8 + 32

print " %s, %s" % (weather_desc, fahrenheit_temp)


