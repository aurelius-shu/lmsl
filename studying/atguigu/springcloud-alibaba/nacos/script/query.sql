


use `nacos.db`;

show tables;



select curtime();
select * from config_info;
select * from config_info_aggr;
select * from config_info_beta;
select * from config_info_tag;
select * from config_tags_relation;
select * from group_capacity;
select * from his_config_info;
select * from permissions;
select * from roles;
select * from tenant_capacity;
select * from tenant_info;
select * from users;


use `galaxy.pos.cloud.tdb`;
show variables like "%time_zone%";
select curtime();

set global time_zone = '+8:00'; 
set time_zone = '+8:00'; 
flush privileges;