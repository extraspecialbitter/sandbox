#!/usr/bin/env python3

# This script fetches the weather from the openweathermap.org API site and prints it out.

from datetime import datetime, timedelta
from sys import argv
from os.path import join
import urllib.request
import time
import getopt
import sys 
import os
import json

urlbase = 'https://api.openweathermap.org/data/2.5/weather'
api_key = 'c4a0b83ccd51f7b1d44d35419710b2b1'
city_id = '4929771'

# read in the longitude and latitude coordinates

url_query = urlbase + '?id=' + city_id + '&appid=' + api_key
with urllib.request.urlopen(url_query) as f:
    json_string = f.read().decode('utf-8')
    parsed_json = json.loads(json_string)

# print("\njson string: %s" % (json_string))
# print("\nparsed json: %s" % (parsed_json))

# parse for and print location

city = parsed_json['name']
country = parsed_json['sys']['country']
print(f"\nCurrent weather for {city}, {country}:")

# parse for weather description and temperature

weather_desc = parsed_json['weather'][0]['main']
# weather_desc2 = parsed_json['weather'][0]['description']
kelvin_temp = parsed_json['main']['temp']
celsius_temp = kelvin_temp - 273.15
fahrenheit_temp = celsius_temp * 1.8 + 32

print(f"      {weather_desc}, {fahrenheit_temp:.1f}°F")
