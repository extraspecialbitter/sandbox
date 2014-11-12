#!/bin/bash

rm -f results.txt

if [ $# -lt 1 ];
then
   echo "Usage: $0 <env>"
   exit 1
fi

case $1 in
p2)
   ./print_service_name.rb 
   ;;
p2-s1)
   ./print_service_name_stage.rb
   ;;
f1)
   ./print_service_name_f1.rb
   ;;
l1)
   ./print_service_name_l1.rb
   ;;
*)
   echo "You have specified an invalid environment name"
   exit 2
   ;;
esac

sort -u results.txt | egrep "tomee|torquebox"

