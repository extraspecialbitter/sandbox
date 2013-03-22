#!/usr/local/bin/bash

# start out with a sleep to make sure the mailboxes are populated

sleep 60

# first process the year to date
 
export InFile=/usr/home/mena/mail/haiku_archive
export OutFile=/usr/www/users/mena/haikupoet/archive
# export Hype=/usr/home/mena/bin/hypermail
export Hype=/usr/local/bin/hypermail

echo "processing the Haiku Archive mailbox for `date +%Y`" 
$Hype -m $InFile -d $OutFile

echo "Completed processing new haiku into archive"

