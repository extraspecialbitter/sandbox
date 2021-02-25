#!/usr/bin/python3

# This script fetches several URLs and checks for content

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

# read in a URL

url_query = 'https://ooinet.oceanobservatories.org'
search_string = 'Research Arrays'

f = urllib.request.urlopen(url_query)
raw_string = f.read()
f.close()
raw_string = str(raw_string)

# print ("\nraw string: %s" % (raw_string))

if search_string in raw_string:
  print ("\nThe website %s returned the expected content\n" % (url_query))
else:
  print ('did not find')
