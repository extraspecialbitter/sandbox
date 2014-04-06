import datetime, MySQLdb, os, sys, urllib2, re, time

def open_db(db):
   host = "p2-if-utilsql01.ad.prodcc.net"
   user = "ctctopsread"
   pwd = "gr8Dane"

   conn = MySQLdb.Connection(db=db, host=host, user=user, passwd=pwd)
   mysql = conn.cursor()

   return mysql

