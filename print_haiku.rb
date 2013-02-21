#!/usr/bin/ruby

require 'mysql'

begin
    con = Mysql.new 'localhost', 'root', 'menagerie', 'haiku_archive'

    rs = con.query("SELECT * FROM haiku")
    n_rows = rs.num_rows
    
    n_rows.times do
        puts rs.fetch_row
    end
    
rescue Mysql::Error => e
    puts e.errno
    puts e.error
    
ensure
    con.close if con
end
