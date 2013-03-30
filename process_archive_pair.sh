#!/bin/bash

rm -f ./archive.html
./drop_table_pair.rb
for i in `ls -1 /export/www/html/haikupoet/archive/[01]???.html`
do
  ./extract_haiku_2013_pair.rb ${i}
  sed  '/^Received\ on/,$d' snippet.txt > qwert.txt
  ./insert_haiku_from_file_into_table_pair.rb qwert.txt
done
./haiku_to_html_pair.rb
