#!/usr/bin/ruby

require 'mysql'

begin
    con = Mysql.new 'p2-utilsqlqa101.ad.prodcc.net', 'ctctopsread', 'gr8Dane', 'ctctops'

    rs = con.query("SELECT b.hardware_name, rpm_name, app_name, c.rpm_version, c.last_status_check FROM apps a, hardware b, apps_servers_mapping c, environment d WHERE a.app_id=c.app_id AND b.hwd_id=c.hwd_id AND b.env_id=d.env_id AND env='f2' AND app_name<>'trackingsvc' AND deploy_type<>2 GROUP BY hardware_name, deploy_type ORDER BY deploy_type, app_name, svr_group")
    n_rows = rs.num_rows
    puts n_rows    

    n_rows.times do
        begin
            file = File.open("baselines.txt", "a")
            file.write(rs.fetch_row)
            file.write "\n"
        end
    end
end

