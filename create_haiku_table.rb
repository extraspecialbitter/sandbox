#!/usr/bin/ruby

require 'mysql'

begin
    con = Mysql.new 'localhost', 'root', 'menagerie', 'haiku_archive'

    con.query("DROP TABLE haiku")
    con.query("CREATE TABLE \
        haiku(first_line VARCHAR(50) not null, second_line VARCHAR(50), third_line VARCHAR(50), date_written CHAR(12) not null)")

rescue Mysql::Error => e
    puts e.errno
    puts e.error
    
ensure
    con.close if con
end
