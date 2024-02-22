#!/usr/bin/python

# This script fetches the most recent Powerball winning numbers from the Powerball RSS feed and prints it out.

from datetime import datetime, timedelta
from sys import argv
from os.path import join
import urllib.request
import os, socket, subprocess
import time
import getopt
import sys 
import os
import json

pburl = 'https://www.powerball.com/api/v1/numbers/powerball/recent10?_format=json'

# read in the JSON data

f = urllib.request.urlopen(pburl)
json_string = f.read()
parsed_json = json.loads(json_string)
f.close()

# debug stuff
print ("json string: {json_string}")
# print ("\nparsed json: %s" % (parsed_json))

# parse latest numbers

winning_numbers = parsed_json[0]["field_winning_numbers"]
multiplier = parsed_json[0]["field_multiplier"]
draw_date = parsed_json[0]["field_draw_date"]

# and print

# print "\nDraw Date:       %s" % (draw_date)
# print "Winning Numbers: %s" % (winning_numbers)
# print "Multiplier:      %s" % (multiplier)
print ("Draw Date: {draw_date}")
print ("Winning Numbers: {winning_numbers}")
print ("Multiplier:      {multiplier}")

# print "\n"

