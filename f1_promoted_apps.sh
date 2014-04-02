#!/bin/bash

date_string=`date +%Y%m%d`
search_text=`expr ${date_string} - 1`
# search_text=`date +%Y%m%d`

rm -f matches.txt
rm -f results.txt

./search_for_f1.rb ${search_text}

for i in `cat results.txt | cut -d',' -f1 | cut -d'"' -f2 | sort -u`
do 
  grep $i results.txt | grep ${search_text} >> matches.txt
done

# sort -u matches.txt | wc -l
# sort -u matches.txt | cut -d'.' -f1 | sort -u | wc -l
sort -u matches.txt | cut -d'.' -f1 | egrep -v "Contacts-|Deals|Thumbnail|TrackingSVC|Simplecard|EM|Auth-Platform|Auth-Devportal" | sort -u | wc -l

