#!/usr/bin/env python
import MySQLdb, sys, time
import commands, os
import commonFunctions
import time
import datetime

cmdOutput = commands.getstatusoutput('hostname -s')
print cmdOutput[1]
