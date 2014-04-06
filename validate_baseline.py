#!/usr/bin/env python

#Author: Khurram Malik
#Date:	 09-29-2011
#Purpose: This script will compare the deployed artifacts with whatever is in YUM repo

import MySQLdb, sys, time
import commands, os, socket, subprocess
import commonFunctions
import time
import datetime
import getopt
import func.overlord.client as fc

#Script Usage
def script_usage():
    print "Usage:"
    print "%s -e <env> -g <group> -a <apps>" %sys.argv[0]
    print "\nOptions:"
    print "-e, --env   \n\t f1, f2, l1, p2-s1, p2 (Note: Env is a must)"
    print "-g, --group \n\t 0, 1, 2, 3 (Note: default=all)"
    print "-a, --apps  \n\t app1:app2:app3 (Note: default=all)"
    print "-d, --debug \n\t Run script in debug mode"
    print "-h, --help  \n\t Display Help" 
    print "\n"
    print "Note: Run this script as root or sudo"

if len(sys.argv) < 3:
    script_usage()
    sys.exit(1)    

CWD=os.getcwd()
TEMP_RPM_FILE = "%s/rpms_in_yum.txt" % CWD
TEMP_RPM_FILE_TEST = "%s/rpms_in_yum_test.txt" % CWD
EXCLUDE_APP_TYPE = '("ThirdParty")' # This should be comma separated list e.g JBOSS, Batch, OfflineBatch, Sched
EXCLUDE_RPM_NAME = '("sso-rpm","thumbnail-rpm","trackingsvc-rpm","sso952-rpm")' #e.g '("webservices-rpm", "visitor-rpm")'
EXCLUDE_APP_NAME = '("trackingsvc")'
EXCLUDE_RPM_VERSION = '("None")'
REPO = ""
ENV=""
INCLUDE_SERVER_GROUP=""
APP_LIST=""
DEBUG=False
problemMessages = []
warningMessage = []
exitStatus = 0
print TEMP_RPM_FILE
cmdOutput = commands.getstatusoutput('hostname -s')
hostname = cmdOutput[1]

#Script Options
letters = 'e:g:a:d:h'
keywords = ['env=', 'group=', 'apps=', 'debug', 'help']

options, remainder =  getopt.getopt(sys.argv[1:], letters, keywords)

for opt, arg in options:
  if opt in ('-e', '--env'):
    ENV = arg
  elif opt in ('-g', '--group'):
    INCLUDE_SERVER_GROUP = '(%s)' % arg
  elif opt in ('-a', '--apps'):
    temp = arg.split(":")
    APP_LIST = '(' + ",".join('"%s"' % i for i in temp) + ')'
  elif opt in ('-d', '--debug'):
    DEBUG = True
  else:
    script_usage
    sys.exit(0)

if (INCLUDE_SERVER_GROUP == "(0)"):
  INCLUDE_SERVER_GROUP=""

print "Options passed to script"
print "ENV:", ENV
print "Server Group:", INCLUDE_SERVER_GROUP
print "APPs:", APP_LIST
print "DEBUG: ", DEBUG

if hostname == 'p2-qautil101':
  if ENV == 'f1':
    REPO = ['f100', 'f151']
  elif ENV == 'f2':
    REPO = ['f200', 'f251']
  elif ENV == 'l1':
    REPO = ['l100', 'l151']
  else:
    print "Wrong env entered, it should be f1, f2, l1, p2-s1 or p2"
    sys.exit(1)    
elif hostname == 'p2-utils01':
  REPO = ['ctctrpms2']
elif hostname == 'p2-util01':
  REPO = ['production']
else:
  print "Only Util servers can run this script"
  sys.exit(1)

print "REPO :", REPO

currentTime = datetime.datetime.now()
print str(currentTime) + " - Running 'yum clean all'"
cmd = "yum clean all"
client = fc.Client(hostname)
info = client.command.run(cmd)
for (host,details) in info.iteritems():
  print details

#Pull rpm versions from CTCTOPS Database and then compare the RPM versions extracted from above step
mysql = commonFunctions.open_db("ctctops")

sql =  'SELECT b.hardware_name, app_type, rpm_name, app_name, c.rpm_version, c.last_status_check '
sql += 'FROM apps a, hardware b, apps_servers_mapping c, environment d '
sql += 'WHERE a.app_id=c.app_id '
sql += 'AND b.hwd_id=c.hwd_id '
sql += 'AND b.env_id=d.env_id ' 
sql += 'AND env="%s" '              % ENV
sql += 'AND app_type NOT IN %s '    % EXCLUDE_APP_TYPE
sql += 'AND rpm_name NOT IN %s '    % EXCLUDE_RPM_NAME
sql += 'AND rpm_version NOT IN %s ' % EXCLUDE_RPM_VERSION
sql += 'AND app_name NOT IN %s '    % EXCLUDE_APP_NAME
if INCLUDE_SERVER_GROUP != "":
  sql += 'AND b.svr_group IN %s '     % INCLUDE_SERVER_GROUP

if APP_LIST != "":
  sql += 'AND a.app_name IN %s '     % APP_LIST

sql += 'ORDER BY rpm_name' 

#print "SQL INFO: %s" % sql

mysql.execute(sql)
fields=mysql.fetchall()


for repo in REPO:
  #Dump all RPMs from YUM env specific repo to a temp file, which will be deleted after script execution
  currentTime = datetime.datetime.now()
  print str(currentTime) + " - Getting list of rpms from yum"
  cmd = "yum list --disablerepo=* --enablerepo=" + repo + " | grep -e '-rpm.noarch' >> %s " % TEMP_RPM_FILE
  
  if DEBUG:
    print "DEBUG - ", cmd

  #proc = subprocess.Popen(cmd, shell=True,stderr=subprocess.PIPE, stdout=subprocess.PIPE)
  os.popen(cmd)

#Calculate current time in the same format as CTCTAppPoller saved in CTCTOPS DB for Last Updated Status Check, Adding 30 sec to current time to avoid any time conflicts on app servers Vs Util Server
currentTime = datetime.datetime.now() + datetime.timedelta(seconds=30)

for field in fields:
  server = field[0]
  rpmName =  field[2]
  rpmVersion = field[4]
  lastStatusCheck = field[5]

  timeDiff = (currentTime - lastStatusCheck).seconds #Time Difference in seconds
    
  cmd = "grep -w '^" + rpmName + "' " + TEMP_RPM_FILE + " | grep " + rpmVersion  + " | awk '{print $2}'"
  result = os.popen(cmd).readline() 

  cmd = "grep -w '^" + rpmName + "' " + TEMP_RPM_FILE + " | awk '{print $2}'"
  rpm_in_yum = os.popen(cmd).readline()

  msg = "RPM: " + rpmName + " on server " + server + " and RPM in yum repo is " + rpm_in_yum
  print msg.rstrip()
  
  if ( result.find (rpmVersion.strip()) and timeDiff < 300):
    currentTime = datetime.datetime.now()
    print str(currentTime) + " - ERROR: RPM " + rpmName + " on " + server + " is different than what we have in the " + ENV + " YUM Repo. ( " + rpmVersion + " vs. " + rpm_in_yum + " )"
    exitStatus = 1
  elif (rpmVersion.strip() != result.strip() or timeDiff > 300):
    currentTime = datetime.datetime.now()
    print str(currentTime) + " - WARN: RPM " + rpmName + " on " + server + " is different than what we have in the " + ENV + " YUM Repo and/or OpsDash Poller is not running. ( " + rpmVersion + " vs. " + rpm_in_yum + " )"
      
    if exitStatus != 1:
      exitStatus = 2

#Emptying Temp file
if DEBUG: 
  print "Removing TEMP File %s and created a copy under %s" % (TEMP_RPM_FILE, TEMP_RPM_FILE_TEST)
  cmd = "cat %s > %s" % (TEMP_RPM_FILE, TEMP_RPM_FILE_TEST)
  os.popen(cmd)

cmd = 'rm -f  %s' % TEMP_RPM_FILE
os.popen(cmd)

if exitStatus == 0:
  print "Script finished, NO ERRORS/WARNINGS"
  sys.exit(exitStatus)
else:
  print "Script finished, There are ERRORS or WARNINGS"
  sys.exit(exitStatus)
