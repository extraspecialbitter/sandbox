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
import csv

pburl = 'https://www.powerball.com/api/v1/numbers/powerball/recent10?_format=json'

my_raw_numbers = [1, 8, 16, 28, 44, 8]
my_numbers = my_raw_numbers[0:5]
my_powerball = my_raw_numbers[5]
matches = 0
pb_matches = 0

# read in the JSON data

f = urllib2.urlopen(pburl)
json_string = f.read()
parsed_json = json.loads(json_string)
f.close()

# parse latest numbers

raw_winning_numbers = parsed_json[0]["field_winning_numbers"]
winning_printable = raw_winning_numbers[0:14]
winning_array = raw_winning_numbers.split(",")
winning_numbers = winning_array[0:4]
winning_powerball_number = winning_array[5]
multiplier = parsed_json[0]["field_multiplier"]
draw_date = parsed_json[0]["field_draw_date"]

# and print

print "\nDraw Date:                 %s" % (draw_date)
print "Winning Numbers:           %s" % (winning_printable)
print "Winning Power Ball Number: %s" % (winning_powerball_number)
print "Multiplier:                %s" % (multiplier)

print "\nMy Numbers          :      %s" % (my_numbers)
print "My Power Ball Number:      %s" % (my_powerball)

# but do they match?

for i in winning_numbers:
    for j in range(0, 4):
        int_me = int(i)
	if int_me == my_numbers[j]:
           print "%s is a match" % (i)
           matches += 1
if matches == 0:
    print "\nSorry - no matches"

# how about the power ball?

int_meh = int(winning_powerball_number)
if int_meh == my_powerball:
    print "\nPower Ball %s is a match" % (my_powerball)
    pb_matches += 1
else:
    print "\nSorry - the Power Ball numbers do not match"
print "\n"
