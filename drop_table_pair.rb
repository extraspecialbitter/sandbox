#!/usr//local/bin/ruby

require 'mysql'

begin
    con = Mysql.new 'db147d.pair.com', 'mena', '8FdXSLfr', 'mena_haiku'

    con.query("DROP TABLE IF EXISTS archive_2013")

rescue Mysql::Error => e
    puts e.errno
    puts e.error
    
ensure
    con.close if con
end
