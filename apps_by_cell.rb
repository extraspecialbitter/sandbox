#!/usr/bin/ruby

require 'mysql'

begin
    con = Mysql.new 'p2-utilsqlqa101.ad.prodcc.net', 'ctctopsread', 'gr8Dane', 'ctctops'

    rs = con.query("SELECT DISTINCT app_name, hardware_name, svr_group, env FROM apps_servers_mapping a, apps b, hardware c, environment d WHERE a.app_id=b.app_id AND a.hwd_id=c.hwd_id AND c.env_id=d.env_id AND app_name='SimplecardAppConfigServer' AND app_type='JBOSS' AND env='f1' ORDER BY hardware_name")
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

