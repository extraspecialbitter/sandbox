#!/bin/bash

rm ./archive.html
./drop_table_2012.rb
for i in `ls -1 /export/www/html/haikupoet/archive_2012/[01]???.html`
do
  ./extract_haiku.rb ${i}
  ./insert_haiku_from_file_into_table_2012.rb snippet.txt
done
./haiku_to_html_2012.rb
