#!/usr/bin/ruby

require 'mysql'

begin
    con = Mysql.new 'localhost', 'root', 'menagerie', 'haiku_archive'

    rs = con.query("SELECT * FROM archive_2012 WHERE haiku_text LIKE '%#{ARGV[0]}%'")
    n_rows = rs.num_rows
#   puts n_rows    

    n_rows.times do
        begin
            file = File.open("results.html", "a")
            file.write(rs.fetch_row)
            file.puts "<br>"
        end
    end
end
