#!/bin/bash

export search_text=`date +%Y%m%d`

rm -f baselines.txt
rm -f filtered_baselines.txt

./verify_f2_baselines.rb

grep -v tapaqa baselines.txt > filtered_baselines.txt

for i in `cat filtered_baselines.txt`
do
  SERVER=`echo $i | awk '{print $1}'`
  RPM_NAME=`echo $i | awk '{print $2}'`
  APP_NAME=`echo $i | awk '{print $3}'`
  RPM_VERSION=`echo $i | awk '{print $4}'`
# echo "${SERVER} ${RPM_NAME} ${APP_NAME} ${RPM_VERSION}"
  echo "${SERVER}"
done
