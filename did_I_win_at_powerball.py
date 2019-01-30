#!/usr/bin/python

# This script fetches the most recent Powerball winning numbers from the Powerball RSS feed and prints it out.

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

pburl = 'https://www.powerball.com/api/v1/numbers/powerball/recent10?_format=json'

my_numbers = [1, 8, 16, 28, 44, 8]
my_powerball = my_numbers[5]

# read in the JSON data

f = urllib2.urlopen(pburl)
json_string = f.read()
parsed_json = json.loads(json_string)

# parse latest numbers

winning_numbers = parsed_json[0]["field_winning_numbers"]
winning_powerball_number = winning_numbers[15:17]
multiplier = parsed_json[0]["field_multiplier"]
draw_date = parsed_json[0]["field_draw_date"]

# and print

print "\nDraw Date:       %s" % (draw_date)
print "Winning Numbers: %s" % (winning_numbers)
print "Multiplier:      %s" % (multiplier)

print "\nMy Numbers          :      %s" % (my_numbers)
print "\nMy Power Ball Number:      %s" % (my_powerball)
print "\nWinning Power Ball Number: %s" % (winning_powerball_number)
print "\n"
f.close()

