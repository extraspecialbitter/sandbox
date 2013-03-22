#!/bin/bash

rm -f ./archive.html
./drop_table.rb
for i in `ls -1 /export/www/html/haikupoet/archive/[01]???.html`
do
  ./extract_haiku.rb ${i}
  ./insert_haiku_from_file_into_table.rb snippet.txt
done
./haiku_to_html.rb
