# 安装

## 关闭 SeLinux 和 firewalld

```shell
vi /etc/selinux/config
# SELINUX=enforcing改为SELINUX=disabled

systemctl stop firewalld
systemctl disable firewalld
```

## 安装需要的软件

1. Apache (1.3.12 或以上）

```shell
yum install -y httpd
# 开机启动
systemctl enable httpd
# 启动 httpd
systemctl start httpd
```

2. PHP

```shell
yum install -y php php-mysql
```

3. mysql

   [安装文档](https://dev.mysql.com/doc/mysql-yum-repo-quick-guide/en/)

## 安装 Zabbix

1. 安装 Zabbix repository

```shell
rpm -Uvh https://repo.zabbix.com/zabbix/4.2/rhel/7/x86_64/zabbix-release-4.2-1.el7.noarch.rpm
yum clean all
```

2. 安装 Zabbix server, frontend, agent, zabbix-get, zabbix-web, zabbix-sender

```shell
yum install -y zabbix-server-mysql zabbix-web-mysql zabbix-agent zabbix-get zabbix-web zabbix-sender
```

## 创建 Zabbix 库

1. 创建 Zabbix 库

```mysql
create database zabbix character set utf8 collate utf8_bin;
grant all privileges on zabbix.* to zabbix@localhost identified by 'password';
flush privileges;
quit;
```

2. 初始化数据库

```shell
zcat /usr/share/doc/zabbix-server-mysql*/create.sql.gz | mysql -uzabbix -p zabbix
```

## 配置 Zabbix 服务端数据库

编辑 zabbix_server.conf

```shell
vi /etc/zabbix/zabbix_server.conf
```

配置如下：

```
1. DBHost=localhost
2. DBUser=zabbix
3. DBName=zabbix
4. DBPassword=password
5. DBSocket=/var/lib/mysql/mysql.sock
```

## 配置 Zabbix 前端（PHP）

编辑 zabbix.conf

```shell
vi /etc/httpd/conf.d/zabbix.conf
```

设置正确的时区

```
php_value date.timezone Asia/Shanghai
```

## 启动 Zabbix 服务和代理

```shell
systemctl restart zabbix-server zabbix-agent httpd
systemctl enable zabbix-server zabbix-agent httpd
```

## 设置时间校准

```shell
yum install ntp
systemctl enable ntpd
service ntpd restart
# 修改系统时区（上海）
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
```

## 中文乱码

使用 windows 中文字体替换 /usr/share/zabbix/fonts 下的字体文件

# Zabbix Agent (Windows)

## 下载(zip)

[官网地址](https://www.zabbix.com/download_agents)

## 配置(主动模式)

1. 日志路径

```conf
LogFile=D:\Program Files (x86)\zabbix_agents_4.2.1\log\zabbix_agentd.log
```

2. StartAgents

```conf
StartAgents=0
```

3. ServerActive

```conf
ServerActive=192.168.100.64
```

4. Hostname

```conf
Hostname=aureliuswindows
```

5. Timeout=30

```conf
Timeout=30
```

6. UserParameter

```conf
UserParameter=saloutstock,"D:\Program Files (x86)\zabbix_agents_4.2.1\items\venv\Scripts\python" "D:\Program Files (x86)\zabbix_agents_4.2.1\items\saloutstock.py"
UserParameter=saloutstock,"/usr/local/zabbixpython/venv/bin/python" "/usr/local/zabbixpython/items/saloutstock.py"
```

## python 环境

```cmd
> virtualenv --no-site-packages venv
> cd venv/Scripts
> activate
> cd ../..
> pip install requests
> pip install pyDes
> pip install cx_oracle
```

## 安装&启动

```cmd
> zabbix_agentd.exe --config <your_configuration_file> --install
> rem eg: zabbix_agentd.exe --config D:\WorkSpace\zabbix-agents-4.2.1\conf\zabbix_agentd.local.conf --install
> zabbix_agentd.exe --config <your_configuration_file> --start
> rem eg: zabbix_agentd.exe --config D:\WorkSpace\zabbix-agents-4.2.1\conf\zabbix_agentd.local.conf --start
```

## 停止&卸载

```cmd
> zabbix_agentd.exe --config <your_configuration_file> --stop
> zabbix_agentd.exe --config <your_configuration_file> --uninstall
```

# Zabbix Agent(Linux)

## python 虚拟环境

```shell
cd /usr/local
mkdir zabbixpython
cd zabbixpython
virtualenv --no-site-package venv
source ./venv/bin/activate
```

## 安装 python 第三方模块

```shell
pip install requests
pip install pyDes
pip install cx_oracle
pip install pymssql
```

## 配置

```shell
mkdir items
cd items
```
