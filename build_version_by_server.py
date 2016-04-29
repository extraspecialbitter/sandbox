#!/usr/bin/python

# This script fetches an application build version from its JSON healthcheck

from sys import argv
import urllib2
import getopt
import json
import sys

# construct healthcheck URL

if len(sys.argv) != 2:
    print "\nUsage:"
    print "%s [ server_name ]" % sys.argv[0]
    print "\n"
    sys.exit(1)
elif len(sys.argv) == 2:
    server_name = sys.argv[1]
    hc_url = 'http://' + server_name + '/healthcheck'

# read in the JSON healtcheck data

f = urllib2.urlopen(hc_url)
json_string = f.read()
parsed_json = json.loads(json_string)

# parse for the build version

build_version = parsed_json['version']

# and print

print "\nThe build version for %s is %s " % (server_name, build_version)
print "\n"
f.close()

