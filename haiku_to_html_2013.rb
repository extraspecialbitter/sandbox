#!/usr/bin/ruby

require 'mysql'

@bad_chars = '[],"'

begin
    con = Mysql.new 'localhost', 'root', 'menagerie', 'haiku_archive'

    rs = con.query("SELECT * FROM archive_2013")
    n_rows = rs.num_rows

    n_rows.times do
        begin
            file = File.open("archive.html", "a")
            line = rs.fetch_row.to_s
            line.gsub!(/[\[\]",]/, '')
            file.write(line)
            file.puts "<br>"
        end
    end
end
