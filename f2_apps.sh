#!/bin/bash

export search_text=`date +%Y%m%d`

rm -f baselines.txt
rm -f filtered_baselines.txt

./verify_f2_baselines.rb

grep -v tapaqa baselines.txt > filtered_baselines.txt

