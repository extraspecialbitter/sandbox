#!/bin/bash

rm -f ./archive_2009.html
./drop_table_2009.rb
for i in `ls -1 ~/git/haiku_search/archive_2009/[0-9]???.html`
do
  ./extract_haiku.rb ${i}
  sed  '/^Received\ on/,$d' snippet.txt > qwert.txt
  sed  '/^Paul\ David\ Mena/,$d' snippet.txt > qwert.txt
  ./insert_haiku_from_file_into_table_2009.rb qwert.txt
done
./haiku_to_html_2009.rb
rm -rf snippet.txt qwert.txt
