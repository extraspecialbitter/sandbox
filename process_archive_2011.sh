#!/bin/bash

rm -f ./archive_2011.html
./drop_table_2011.rb
for i in `ls -1 /export/haiku_search/archive_2011/[0-9]???.html`
do
  ./extract_haiku_2011.rb ${i}
  sed  '/^Received\ on/,$d' snippet.txt > qwert.txt
# sed  '/^Paul\ David\ Mena/,$d' snippet.txt > qwert.txt
  ./insert_haiku_from_file_into_table_2011.rb qwert.txt
done
./haiku_to_html_2011.rb
rm -rf snippet.txt qwert.txt
