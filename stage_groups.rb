#!/usr/bin/ruby

require 'mysql'

begin
    con = Mysql.new 'p2-sif-utilsql01.ad.prodcc.net', 'ctctopsread', 'gr8Dane', 'ctctops'

    rs = con.query("SELECT DISTINCT hardware_name, svr_group FROM hardware WHERE hardware_name LIKE 'p2-jbsynload%'")
    n_rows = rs.num_rows
#   puts n_rows    

    n_rows.times do
        begin
            file = File.open("results.txt", "a")
            file.write(rs.fetch_row)
            file.write "\n"
        end
    end
end

