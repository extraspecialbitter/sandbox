#!/usr/bin/ruby

require 'mysql'

begin
    con = Mysql.new 'p2-utilsqlqa101.ad.prodcc.net', 'ctctopsread', 'gr8Dane', 'ctctops'

    rs = con.query("SELECT DISTINCT app_name, rpm_version, env FROM apps_servers_mapping a, apps b, environment WHERE a.app_id=b.app_id AND rpm_version IS NOT NULL AND app_type='JBOSS' AND env='l1' ORDER BY app_name")
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

