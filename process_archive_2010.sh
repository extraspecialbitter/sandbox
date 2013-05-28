#!/bin/bash

rm -f ./archive_2010.html
./drop_table_2010.rb
for i in `ls -1 /export/haiku_search/archive_2010/[0-9]???.html`
do
  ./extract_haiku.rb ${i}
  sed  '/^Received\ on/,$d' snippet.txt > qwert.txt
  sed  '/^Paul\ David\ Mena/,$d' snippet.txt > qwert.txt
  ./insert_haiku_from_file_into_table_2010.rb qwert.txt
done
./haiku_to_html_2010.rb
