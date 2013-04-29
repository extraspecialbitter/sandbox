#!/usr/bin/ruby

require 'mysql'

begin
    con = Mysql.new 'localhost', 'root', 'menagerie', 'haiku_archive'

    con.query("DROP TABLE IF EXISTS archive_2010")

rescue Mysql::Error => e
    puts e.errno
    puts e.error
    
ensure
    con.close if con
end
