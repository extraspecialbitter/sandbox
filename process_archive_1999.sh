#!/bin/bash

rm -f ./archive_1999.html
./drop_table_1999.rb
for i in `ls -1 /export/haiku_search/archive_1999/[0-9]???.html`
do
  ./extract_haiku.rb ${i}
  cp snippet.txt qwert.txt
  sed  '/^Received\ on/,$d' snippet.txt > qwert.txt
  sed  '/^Paul\ David\ Mena/,$d' qwert.txt > snippet.txt
  sed  '/^========================/,$d' snippet.txt > qwert.txt
  sed  '/^------------------------/,$d' qwert.txt > snippet.txt 
  sed  '/^________________________/,$d' snippet.txt > qwert.txt
  ./insert_haiku_from_file_into_table_1999.rb qwert.txt
done
./haiku_to_html_1999.rb
