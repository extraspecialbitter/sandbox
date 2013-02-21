#!/usr/bin/ruby

require 'mysql'

begin
    con = Mysql.new 'localhost', 'root', 'menagerie', 'haiku_archive'
    
    con.query("INSERT INTO haiku_archive.haiku(first_line, second_line, third_line, date_written) \
        VALUES('December rain', 'the weekend', 'melts away', 'Dec 10 2012')")
    con.query("INSERT INTO haiku_archive.haiku(first_line, second_line, third_line, date_written) \
        VALUES('winter moths', 'my mother', 'buys an iPhone', 'Dec 10 2012')")
    con.query("INSERT INTO haiku_archive.haiku(first_line, second_line, third_line, date_written) \
        VALUES('alone', 'I win a game', 'of solitaire', 'Dec 11 2012')")
    con.query("INSERT INTO haiku_archive.haiku(first_line, second_line, third_line, date_written) \
        VALUES('the perfect pub', 'where nobody', 'knows my name', 'Dec 11 2012')")
    con.query("INSERT INTO haiku_archive.haiku(first_line, second_line, third_line, date_written) \
        VALUES('hipsters', 'waxing', 'ironic', 'Dec 11 2012')")

rescue Mysql::Error => e
    puts e.errno
    puts e.error
    
ensure
    con.close if con
end
