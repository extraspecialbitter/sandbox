#!/bin/bash

export search_text=`date +%Y%m%d`

rm -f matches.txt
rm -f results.txt

./search_for_recent_baselines.rb 20130321

for i in `cat results.txt | cut -d',' -f1 | cut -d'"' -f2 | sort -u`
do 
  grep $i results.txt | grep 20130321 >> matches.txt
done

# sort -u matches.txt | wc -l
# sort -u matches.txt | cut -d'.' -f1 | sort -u | wc -l
sort -u matches.txt | cut -d'.' -f1 | egrep -v "Contacts-|Deals|Thumbnail|TrackingSVC|Simplecard|EM|Auth-Platform|Auth-Devportal" | sort -u | wc -l

