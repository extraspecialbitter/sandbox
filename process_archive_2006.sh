#!/bin/bash

rm -f ./archive_2006.html
./drop_table_2006.rb
for i in `ls -1 /export/haiku_search/archive_2006/[01]???.html`
do
  ./extract_haiku.rb ${i}
  sed  '/^Received\ on/,$d' snippet.txt > qwert.txt
  sed  '/^Paul\ David\ Mena/,$d' snippet.txt > qwert.txt
  sed  '/^========================/,$d' snippet.txt > qwert.txt
  ./insert_haiku_from_file_into_table_2006.rb qwert.txt
done
./haiku_to_html_2006.rb
