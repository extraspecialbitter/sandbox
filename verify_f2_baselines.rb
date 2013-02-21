#!/usr/bin/ruby

require 'mysql'

begin
    con = Mysql.new 'p2-utilsqlqa101.ad.prodcc.net', 'ctctopsread', 'gr8Dane', 'ctctops'

    rs = con.query("SELECT group_concat(distinct app_name order by app_name separator ',') as app, group_concat(distinct concat(rpm_name, '_', rpm_version) order by rpm_name separator ',') as rpm_name, deploy_type, svr_group, hardware_name FROM apps_servers_mapping a, apps b, hardware c, environment d WHERE puppet='y' AND app_type='JBOSS' AND type<>'Camel' AND svr_group<>'4' AND a.app_id=b.app_id AND a.hwd_id=c.hwd_id AND c.env_id=d.env_id  AND env='f2' AND app_name<>'Impression' AND deploy_type<>2 GROUP BY hardware_name, deploy_type ORDER BY deploy_type, app, svr_group")
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

