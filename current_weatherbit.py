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
import pytz
import ephem

urlbase = 'https://api.weatherbit.io/v2.0/'
api_key = "91b2e05a9ef84a5586b4a42d49c0d7ac"

# parse arguments

station = 'cc'
lat = 41.6483
lon = -70.3366

# Make single API call to get both current conditions and forecast
lat = str(lat)
lon = str(lon)
forecast_url_query = urlbase + 'forecast/daily?lat=' + lat + '&lon=' + lon + '&key=' + api_key
f = urllib.request.urlopen(forecast_url_query)
json_string = f.read()
parsed_json = json.loads(json_string)
f.close()

data = parsed_json["data"]
city_name = parsed_json["city_name"]
state_code = parsed_json["state_code"]
country_code = parsed_json["country_code"]
timezone = parsed_json["timezone"]

# Create timezone object for conversions
local_tz = pytz.timezone(timezone)

# Print current conditions (first day in forecast)
current_day = data[0]
current_weather = current_day["weather"]
current_temp = current_day["temp"]
current_temp = current_temp * 1.8 + 32
current_temp = round(current_temp, 2)

print("\nCurrent weather for %s, %s, %s:" % (city_name, state_code, country_code))
print(" %s, %s" % (current_weather["description"], current_temp))

print("\n")
