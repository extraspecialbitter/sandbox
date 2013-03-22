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

# then process the new haiku

if [ -f /usr/home/mena/mail/new_haiku ];
then 
  export InFile=/usr/home/mena/mail/new_haiku
  export OutFile=/usr/www/users/mena/haikupoet/new_haiku
  echo "processing the latest haiku"
  $Hype -m $InFile -d $OutFile
else
  echo "no new haiku to process"
  exit 1
fi

# More Initializations in preparation for appending the new haiku

BINDIR=/usr/www/users/mena/haikupoet/bin
ARCHIVE="results.txt"
RESULTS="results_new.txt"
TEMP="tempfile.txt"
SEARCH_STRING0="deleted"
SEARCH_STRING1="body="
SEARCH_STRING2="<pre>"
SEARCH_STRING3="<p>="
SEARCH_STRING4="<br>"
SEARCH_STRING5="<p>"

cd $BINDIR
rm -f $RESULTS
rm -f $TEMP
touch $TEMP

# Do this for every new HTML file

for NEW in `find $OutFile -name "[0-9][0-9][0-9][0-9].html"`
do

# Initialize for each file

LINE_INDEX=1
SCRATCH_INDEX=0
NUMBER_OF_LINES=`cat /usr/www/users/mena/haikupoet/new_haiku/0000.html | awk '{print $2}' | wc -l`
TOGGLE=0

# Open the input file and start processing

while [ $LINE_INDEX -lt  $NUMBER_OF_LINES ]
do
   LINE=`tail -${NUMBER_OF_LINES} $NEW | head -1`
   if [ `echo $LINE | grep -c $SEARCH_STRING1` -eq 1 ];
   then
      if [ $TOGGLE -eq 0 ];
      then
         TOGGLE=1
      else
         TOGGLE=2
      fi
   elif [ $TOGGLE -eq 1 ];
   then
      if [ `echo $LINE | grep -c $SEARCH_STRING0` -eq 1 ];
      then
         cat /dev/null > $TEMP
         TOGGLE=2
      elif [ `echo $LINE | grep -c $SEARCH_STRING2` -eq 0 ];
      then
         if [ `echo $LINE | grep -c $SEARCH_STRING3` -eq 1 ];
         then
            TOGGLE=2
         elif [ `echo $LINE | grep -c $SEARCH_STRING4` -eq 0 ];
         then
            echo -n "${LINE}<br>" >> $TEMP
         fi
      else
          TOGGLE=2
      fi
   fi
   NUMBER_OF_LINES=`expr $NUMBER_OF_LINES - 1`

done
echo "" >> $TEMP

# Copy the processed HTML file into the text file

cat $TEMP >> $RESULTS
cat /dev/null > $TEMP

done

# Post processing

sed -i "" 's/^<p>//' $RESULTS
sed -i "" 's/&nbsp;//g' $RESULTS
sed -i "" 's/<p>_.*//g' $RESULTS
sed -i "" 's/<br>===.*//g' $RESULTS
sed -i "" 's/Fidelity.*//g' $RESULTS
sed -i "" 's/FeB.*//g' $RESULTS
sed -i "" 's/<a href.*//g' $RESULTS
sed -i "" 's/----.*//g' $RESULTS
sed -i "" 's/____.*//g' $RESULTS

# Append newly processed text to the archive

cat $RESULTS >> $ARCHIVE
cp $ARCHIVE /usr/www/users/mena/haikupoet/archive.txt

# Delete processed new haiku files

rm /usr/www/users/mena/haikupoet/new_haiku/*.html
rm /usr/home/mena/mail/new_haiku

echo "Completed processing new haiku into archive"

