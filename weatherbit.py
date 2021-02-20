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
    print ("%s [ mi | mx | pr | way | cc | ym | bos | nyc | ca | rb | li ]" % sys.argv[0])
    print ("\n")
    sys.exit(1)
elif len(sys.argv) == 2:
    station = sys.argv[1]

    if station == 'cc':
        lat = 41.6483
        lon = -70.3366
#   elif station == 'mx':
#       city_id = '3985710'
#   elif station == 'ym':
#       city_id = '4956335'
#   elif station == 'mi':
#       city_id = '5000947'
#   elif station == 'way':
#       city_id = '4937230'
#   elif station == 'rb':
#       city_id = '5386785'
#   elif station == 'ca':
#       city_id = '5402405'
#   elif station == 'li':
#       city_id = '5116060'
#   elif station == 'bos':
#       city_id = '4931972'
#   elif station == 'nyc':
#       city_id = '5128581'
#   elif station == 'pr':
#       city_id = '4568127'
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

for i in range(0, 6):
    day = data[i]
    date = day["valid_date"]
    weather = day["weather"]
    description = weather["description"]
    min_temp = day["min_temp"]
    min_temp = min_temp * 1.8 + 32
    max_temp = day["max_temp"]
    max_temp = max_temp * 1.8 + 32
    print (" %s : %s, low: %s, high: %s" % (date, description, min_temp, max_temp))
print ("\n")

