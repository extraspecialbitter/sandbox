#!/bin/bash

rm -f ./archive_2007.html
./drop_table_2007.rb
for i in `ls -1 /export/www/html/haikupoet/archive_2007/[01]???.html`
do
  ./extract_haiku.rb ${i}
  sed  '/^Received\ on/,$d' snippet.txt > qwert.txt
  sed  '/^Paul\ David\ Mena/,$d' snippet.txt > qwert.txt
  ./insert_haiku_from_file_into_table_2007.rb qwert.txt
done
./haiku_to_html_2007.rb
