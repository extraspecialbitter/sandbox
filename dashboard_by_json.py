#!/usr/bin/python3

# This script parses a JSON file consisting of website URLs and their expected content

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

# read in the JSON file

# f = open("/home/pablo/tmp/dashboard.json", "r")
f = open("./dashboard.json", "r")
json_string = f.read()
parsed_json = json.loads(json_string)
f.close()

# print ("\njson string: %s" % (json_string))
# print ("\nparsed json: %s" % (parsed_json))

# parse for and print data

data = parsed_json["data"]
# print ("\ndata: %s" % (data))

# print ("\nraw html: %s " % (raw_html))

for i in range(0, 3):
   j = data[i]
   desc = j["page_desc"]
   purl = j["page_url"]
   sstr = j["search_str"]

   g = urllib.request.urlopen(purl)
   raw_html = g.read()
   g.close()

   if sstr in str(raw_html):
      print ("\n %s returned the expected content" % (desc))
   else:
      print ("\n investigate %s" % (purl))
print("\n")

