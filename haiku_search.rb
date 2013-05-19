#!/usr/bin/ruby

require 'mysql'

begin
    con = Mysql.new 'localhost', 'root', 'menagerie', 'haiku_archive'

    rs = con.query("SELECT * FROM archive_2006 WHERE haiku_text LIKE '%#{ARGV[0]}%' UNION
                    SELECT * FROM archive_2007 WHERE haiku_text LIKE '%#{ARGV[0]}%' UNION
                    SELECT * FROM archive_2008 WHERE haiku_text LIKE '%#{ARGV[0]}%' UNION
                    SELECT * FROM archive_2009 WHERE haiku_text LIKE '%#{ARGV[0]}%' UNION
                    SELECT * FROM archive_2010 WHERE haiku_text LIKE '%#{ARGV[0]}%' UNION
                    SELECT * FROM archive_2011 WHERE haiku_text LIKE '%#{ARGV[0]}%' UNION
                    SELECT * FROM archive_2012 WHERE haiku_text LIKE '%#{ARGV[0]}%' UNION
                    SELECT * FROM archive_2013 WHERE haiku_text LIKE '%#{ARGV[0]}%'")
    n_rows = rs.num_rows

    
    n_rows.times do
        begin
            puts(rs.fetch_row)
            puts "<br>"
        end
    end
    puts "There are #{n_rows} rows in the result set"
end
