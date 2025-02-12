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
    print ("%s [ cr | phx | dfw | mi | ts | ofl | cdmx | pvd | pr | vqs | way | cc | wh | bos | nyc | nz | vic | osu | ber | li | pt | gar | nola ]" % sys.argv[0])
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
    elif station == 'ofl':
        lat = 29.1872
        lon = -82.1401
    elif station == 'pme':
        lat = 43.6591
        lon = -70.2568
    elif station == 'cdmx':
        lat = 19.4326
        lon = -99.1332
    elif station == 'pvd':
        lat = 41.7235
        lon = -71.4270
    elif station == 'wh':
        lat = 41.5411
        lon = -70.6486
    elif station == 'cr':
        lat = 9.8715
        lon = -85.4933
    elif station == 'dfw':
        lat = 32.7079
        lon = -96.9209
    elif station == 'phx':
        lat = 33.4352
        lon = -112.0101
    elif station == 'mi':
        lat = 46.4115
        lon = -86.6550
    elif station == 'way':
        lat = 42.3164
        lon = -71.3642
    elif station == 'rb':
        lat = 33.8449
        lon = -118.3872
    elif station == 'nz':
        lat = -41.8833
        lon = 173.6666
    elif station == 'vic':
        lat = 43.6027
        lon = -111.1114
    elif station == 'ber':
        lat = 32.3668 
        lon = -64.6836
    elif station == 'osu':
        lat = 44.5646
        lon = -123.2620
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
        lat = 18.4547
        lon = -66.5384
    elif station == 'vqs':
        lat = 18.0982
        lon = -65.4759
    elif station == 'ky':
        lat = -0.4466
        lon = 39.6518
    elif station == 'pt':
        lat = 42.0547
        lon = -70.1846
    elif station == 'gar':
        lat = 0.4532
        lon = 39.6461
    elif station == 'nola':
        lat = 29.9511
        lon = -90.0715
    else:
        print ("\nThis station feed has not been implemented yet.")
        print ("\n")
        sys.exit(1)

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

# Print current conditions (first day in forecast)
current_day = data[0]
current_weather = current_day["weather"]
current_temp = current_day["temp"]
current_temp = current_temp * 1.8 + 32
current_temp = round(current_temp, 2)

print("\nCurrent weather for %s, %s, %s:" % (city_name, state_code, country_code))
print(" %s, %s" % (current_weather["description"], current_temp))

# Print timezone information
print("\nStation Timezone: %s" % timezone)
tz_date = subprocess.check_output(f'TZ={timezone} date', shell=True).decode('utf-8').strip()
print(f"Local Time: {tz_date}")

# Print forecast
print("\nForecast:")

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
    sunrise_ts = day["sunrise_ts"]
    sunrise_utc = datetime.fromtimestamp(sunrise_ts).strftime('%H:%M:%S')
    sunset_ts = day["sunset_ts"]
    sunset_utc = datetime.fromtimestamp(sunset_ts).strftime('%H:%M:%S')
    print(" %s : %s, low: %s, high: %s" % (date, description, min_temp, max_temp))
    print("              Sunrise: %s, Sunset: %s" % (sunrise_utc, sunset_utc))
print("\n")
