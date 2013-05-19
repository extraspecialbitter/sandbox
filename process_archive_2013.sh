#!/bin/bash

rm -f ./archive.html
./drop_table_2013.rb
for i in `ls -1 /export/haiku_search/archive/[01]???.html`
do
  ./extract_haiku_2013.rb ${i}
  sed  '/^Received\ on/,$d' snippet.txt > qwert.txt
  ./insert_haiku_from_file_into_table_2013.rb qwert.txt
done
./haiku_to_html_2013.rb
