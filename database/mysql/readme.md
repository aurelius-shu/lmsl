<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [MySQL 安装](#mysql-安装)
  - [MySQL On Linux](#mysql-on-linux)
  - [MySQL On Windows](#mysql-on-windows)
  - [MySQL On Windows +](#mysql-on-windows-1)
- [MySQL 管理](#mysql-管理)
  - [用户](#用户)
  - [建库](#建库)
  - [建表](#建表)
- [登陆](#登陆)
  - [命令行远程登陆](#命令行远程登陆)
- [docker](#docker)

<!-- /code_chunk_output -->

# MySQL 安装

[官网地址](https://dev.mysql.com/downloads/mysql)

## MySQL On Linux

1. 下载 yum repository

```shell
wget https://dev.mysql.com/get/mysql80-community-release-el7-3.noarch.rpm
```

2. 安装 yum repository

```shell
sudo rpm -Uvh mysql80-community-release-el7-3.noarch.rpm
```

3. 配置 mysql repository，改为安装 mysql5.7

```shell
# 查看全部 mysql repository
yum repolist all | grep mysql
# yum-config-manager 配置(not dnf-enabled)
sudo yum -y install yum-utils
sudo yum-config-manager --disable mysql80-community
sudo yum-config-manager --enable mysql57-community
# dnf config-manager 配置(dnf-enabled platforms)
sudo dnf config-manager --disable mysql80-community
sudo dnf config-manager --enable mysql57-community
# 查看enable mysql repository
yum repolist enabled | grep mysql
```

4. 安装 mysql server

```shell
sudo yum -y install mysql-community-server
```

5. 启动 mysql server

```shell
sudo service mysqld start
# 或者 EL7-based platforms
sudo systemctl start mysqld.service
```

6. 检查 mysql server 状态

```shell
sudo service mysqld status
# 或者 EL7-based platforms
sudo systemctl status mysqld.service
```

7. 修改初始密码

```shell
# 查看初始密码
sudo grep 'temporary password' /var/log/mysqld.log
# 登录mysql
mysql -uroot -p
# 修改密码
alter user 'root'@'localhost' identified by '********';
```

8. 授权非 localhost 的连接

```sql
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'password' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```

## MySQL On Windows

1. 解压到安装路径

```txt
eg: D:\Program Files (x86)\mysql-5.7.23-winx64
```

2. 创建 my.ini（./data/my.ini） 文件

```txt
[Client]
port = 3306

[mysqld]
#设置3306端口
port = 3306
# 设置mysql的安装目录
basedir=D:\Program Files (x86)\mysql-5.7.23-winx64
# 设置mysql数据库的数据的存放目录
datadir=D:\Program Files (x86)\mysql-5.7.23-winx64
# 允许最大连接数
max_connections=200
# 服务端使用的字符集默认为8比特编码的latin1字符集
character-set-server=utf8
# 创建新表时将使用的默认存储引擎
default-storage-engine=INNODB

[mysql]
# 设置mysql客户端默认字符集
default-character-set=utf8
```

3. 初始化 mysql

```powershell
# 管理员身份运行，此处会返回 mysql 初始密码
mysqld --initialize --user=mysql --console
```

4. 安装 mysql server

```powershell
# 如果存在旧的 mysql server，可以使用 -remove 删除
mysqld --install mysql
```

5. 启动 mysql server

```powershell
net start mysql
```

6. 登录 mysql

```powershell
# 此处输入步骤 3 中返回的初始密码
mysql -uroot -p
Enter password: ******
```

7. 修改密码

```sql
set password=password('999999');
```

8. 环境变量

```txt
MYSQL_HOME=D:\Program Files (x86)\mysql-5.7.23-winx64
PATH=$PATH;$MYSQL_HOME\bin;
```

9. 授权非 localhost 远程连接

```sql
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'password' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```

## MySQL On Windows +

1. 解压到安装路径

```txt
eg: D:\Program Files (x86)\mysql-5.7.23-winx64
```

2. 环境变量

```txt
MYSQL_HOME=D:\Program Files (x86)\mysql-5.7.23-winx64
PATH=$PATH;$MYSQL_HOME\bin;
```

3. 生成 data 文件

```powershell
# 管理员身份运行
# mysqld --initialize --user=mysql --console
mysqld --initialize-insecure --user=mysql
```

4. 解决启动服务失败

```powershell
# 如果存在旧的 mysql server，可以使用 -remove 删除
# mysqld --install mysql
mysqld -install
```

5. 启动 mysql server

```powershell
net start mysql
```

6. 登录 mysql

```powershell
# 此处无需密码
mysql -uroot -p
Enter password: ******
```

7. 修改密码

```sql
set password=password('999999');
```

8. 授权非 localhost 远程连接

```sql
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'password' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```

# MySQL 管理

## 用户

```sql
CREATE USER 'aure'@'localhost' IDENTIFIED BY 'some_pass';
GRANT ALL PRIVILEGES ON *.* TO 'aure'@'localhost' WITH GRANT OPTION;
CREATE USER 'aure'@'%' IDENTIFIED BY 'some_pass';
GRANT ALL PRIVILEGES ON *.* TO 'aure'@'%' WITH GRANT OPTION;
-- V8.X
create user 'aurelius'@'%' identified with mysql_native_password by 'some_pass';
grant all on *.* to 'aurelius'@'%';
```

## 建库

```sql
create database dw
-- 数据库默认字符集
default charset utf8
-- 数据库校对规则
collate utf8_romanian_ci;

create database dw
default charset utf8mb4
collate utf8mb4_romanian_ci;
```

## 建表

```sql
create table bas_users(id int, name varchar(30), email varchar(30));
```

# 登陆

## 命令行远程登陆

```powershell
mysql -h port -u user -p
```

# docker

```shell
# 启动
sudo docker run --name mysql -e MYSQL_ROOT_PASSWORD=999999 -p 3306:3306 -d mysql
```
