#!/usr/bin/ruby

require 'mysql'

begin
    con = Mysql.new 'localhost', 'root', 'menagerie', 'haiku_archive'

    rs = con.query("SELECT * FROM archive_1999")
    n_rows = rs.num_rows
    
    n_rows.times do
        puts rs.fetch_row.join("\s")
    end
    
    puts "There are #{n_rows} rows in the result set"
    
rescue Mysql::Error => e
    puts e.errno
    puts e.error
    
ensure
    con.close if con
end
