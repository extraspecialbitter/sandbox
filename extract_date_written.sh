#!/bin/bash

if [ $# -lt 1 ]; then
   echo "Usage: $0 <html file name>"
   exit 1
fi

date=`grep "<strong>Date:</strong>" $1 | cut -d' ' -f3-5`
echo $date
