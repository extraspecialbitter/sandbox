#!/usr/bin/python3

# This script fetches the weather from the weatherbit.io API site and prints it out.

import urllib3
import urllib.request
from datetime import datetime, timedelta
from sys import argv
from os.path import join
import os, socket, subprocess
import time
import getopt
import sys 
import os
import json

urlbase = 'https://api.weatherbit.io/v2.0/'
api_key = "91b2e05a9ef84a5586b4a42d49c0d7ac"

# parse arguments

if len(sys.argv) != 2:
    print ("\nUsage:")
    print ("%s [ tx | mi | ts | gj | scc | pr | way | cc | wh | bos | nyc | ca | rb | li ]" % sys.argv[0])
    print ("\n")
    sys.exit(1)
elif len(sys.argv) == 2:
    station = sys.argv[1]

    if station == 'cc':
        lat = 41.6483
        lon = -70.3366
    elif station == 'ts':
        lat = 23.4653
        lon = -110.2569
    elif station == 'gj':
        lat = 20.6597
        lon = -103.3496
    elif station == 'scc':
        lat = 16.7370
        lon = -92.6376
    elif station == 'wh':
        lat = 41.5411
        lon = -70.6486
    elif station == 'tx':
        lat = 29.4241
        lon = -98.4936
    elif station == 'mi':
        lat = 46.4115
        lon = -86.6550
    elif station == 'way':
        lat = 42.3164
        lon = -71.3642
    elif station == 'rb':
        lat = 33.8449
        lon = -118.3872
    elif station == 'ca':
        lat = 34.1513
        lon = -118.8187
    elif station == 'li':
        lat = 40.9091
        lon = -73.0169
    elif station == 'bos':
        lat = 42.3657
        lon = -71.0096
    elif station == 'nyc':
        lat = 40.7033
        lon = -73.9421
    elif station == 'pr':
        lat = 18.0961
        lon = -65.4866
    elif station == 'ky':
        lat = -0.4466
        lon = 39.6518
    else:
        print ("\nThis station feed has not been implemented yet.")
        print ("\n")
        sys.exit(1)

# read in the current weather JSON

lat = str(lat)
lon = str(lon)
current_url_query = urlbase + 'current?lat=' + lat + '&lon=' + lon + '&key=' + api_key 
f = urllib.request.urlopen(current_url_query)
json_string = f.read()
parsed_json = json.loads(json_string)
f.close()

# print ("\njson string: %s" % (json_string))
# print ("\nparsed json: %s" % (parsed_json))

# parse for and print location

data = parsed_json["data"]
# print ("\ndata: %s" % (data))

country = data[0]["country_code"]
city = data[0]["city_name"]
state = data[0]["state_code"]
print ("\nCurrent weather for %s, %s, %s:" % (city, state, country))

# parse for weather description and temperature

weather = data[0]["weather"]
# print ("\nweather: %s" % (weather))
weather_desc = weather["description"]
celsius_temp = data[0]["temp"]
fahrenheit_temp = celsius_temp * 1.8 + 32
fahrenheit_temp = round(fahrenheit_temp, 2)
print (" %s, %s" % (weather_desc, fahrenheit_temp))

# read in the forecast JSON

forecast_url_query = urlbase + 'forecast/daily?lat=' + lat + '&lon=' + lon + '&key=' + api_key
g = urllib.request.urlopen(forecast_url_query)
json_string = g.read()
parsed_json = json.loads(json_string)
g.close()

# print ("\njson string: %s" % (json_string))
# print ("\nparsed json: %s" % (parsed_json))

# parse for and print forecast

data = parsed_json["data"]

print ("\nForecast:")

for i in range(0, 7):
    day = data[i]
    date = day["valid_date"]
    weather = day["weather"]
    description = weather["description"]
    min_temp = day["min_temp"]
    min_temp = min_temp * 1.8 + 32
    min_temp = round(min_temp, 2)
    max_temp = day["max_temp"]
    max_temp = max_temp * 1.8 + 32
    max_temp = round(max_temp, 2)
    print (" %s : %s, low: %s, high: %s" % (date, description, min_temp, max_temp))
print ("\n")

