#!/bin/bash

rm -f matches.txt
rm -f results.txt

./print_service_name.rb 

sort -u results.txt | grep tomee

