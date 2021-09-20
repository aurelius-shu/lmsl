<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [MySQL 安装](#mysql-安装)
  - [MySQL on Linux](#mysql-on-linux)
  - [MySQL on Windows](#mysql-on-windows)
  - [MySQL on Windows +](#mysql-on-windows-1)
  - [MySQL on Docker](#mysql-on-docker)
  - [MySQL Client](#mysql-client)
- [MySQL 管理](#mysql-管理)
  - [命令行远程登陆](#命令行远程登陆)
  - [用户](#用户)
  - [建库](#建库)
  - [建表](#建表)
  - [修改时区](#修改时区)
- [索引](#索引)
  - [B+ Tree](#b-tree)
- [explain](#explain)
- [函数](#函数)
- [存储过程](#存储过程)
- [游标](#游标)

<!-- /code_chunk_output -->

# MySQL 安装

[官方文档](https://dev.mysql.com/doc/refman/5.7/en/linux-installation-yum-repo.html)

## MySQL on Linux

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

## MySQL on Windows

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

## MySQL on Windows +

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

## MySQL on Docker

```shell
# 启动
sudo docker run --name mysql -e MYSQL_ROOT_PASSWORD=999999 -p 3306:3306 -d mysql
```

## MySQL Client

```shell
wget http://mirrors.sohu.com/mysql/MySQL-5.7/mysql-community-client-5.7.23-1.el7.x86_64.rpm
rpm -ivh mysql/MySQL-5.7/mysql-community-client-5.7.23-1.el7.x86_64.rpm --force --nodeps
```

# MySQL 管理

## 命令行远程登陆

```powershell
mysql -h port -u user -p
```

## 用户

```sql
CREATE USER 'aure'@'localhost' IDENTIFIED BY 'some_pass';
GRANT ALL PRIVILEGES ON *.* TO 'aure'@'localhost' WITH GRANT OPTION;
CREATE USER 'aure'@'%' IDENTIFIED BY 'some_pass';
GRANT ALL PRIVILEGES ON *.* TO 'aure'@'%' WITH GRANT OPTION;
-- V8.X
create user 'aurelius'@'%' identified with mysql_native_password by '999999';
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

## 修改时区

```sql
-- 查看当前时间
select curtime();

-- 修改mysql全局时区为北京时间，即我们所在的东8区
set global time_zone = '+8:00';
-- 修改当前会话时区
set time_zone = '+8:00';
-- 立即生效
flush privileges;
```

# 索引

MySQL 高效获取数据的数据结构，排好序的快速查找（B+ 树）

1. 减少了 I/O 次数，随机 I/O 变为顺序 I/O
2. 减少了分组排序时临时表创建

## B+ Tree

### 数据结构

`B Tree` Balance Tree，平衡树，查找树，且所有叶子节点位于同一层
`B+ Tree` 基于 B Tree 和叶子节点顺序访问指针实现，提高了区间查询性能

### 操作

查找：从根节点开始递归地二分查找，找到叶子节点中指定 key 对应的 data
插入删除：会破坏树的平衡，因此在插入删除之后，需要进行分裂、合并、旋转等操作来维护平衡性

### vs. 红黑树

B+ Tree 访问磁盘数据的性能更高

1. B+ Tree 有更低的树高；O(h) = O(logdN)，d 是节点出度，红黑树出度为 2
2. 数据库索引一个节点大小与磁盘交换页大小相同，即一次 I/O 可完成一个索引节点的载入
3. 不同磁盘块通常需要磁盘通过寻道完成完整数据读取，寻道效率低下
4. 磁盘寻道时间与树高成正比，所以 B+ Tree 更适合磁盘数据读取
5. 磁盘预读特性，不严格按需读取，B+ Tree 的相邻节点可以高效预先载入

## MySQL 索引

在存储引擎层实现，与存储引擎有关

### B+ Tree 索引

大多数存储引擎的默认索引类型，对树搜索，速度很快，有序（可用于排序、分组）
可有多列组合
适用于全键值、键值范围、键前缀查找（最左前缀查找）

#### InnoDB B+ Tree 分类

1. 聚簇索引 叶子节点 data 域记录了完整的数据记录，因为数据不能存放在两个地方，所以一个表只能有一个聚簇索引
2. 辅助索引 叶子节点 data 域记录了主键的值，使用辅助索引查找时，需要先查找主键值，再到聚簇索引查找数据记录

### 哈希索引

以 O(1)时间进行精准查找，但无序（无法使用分组、排序、范围查找）
InnoDB 的自适应哈希索引，在 B+ Tree 的基础上，给被使用频繁的索引创建哈希索引

### 全文索引

MyISAM 支持全文索引，InnoDB 在 5.6.4 也开始支持
用于查找文本中的关键字，使用 match against 查找
使用倒排索引实现，记录着关键词到文档的映射

### 空间数据索引（R-Tree）

MyISAM 支持 R-Tree
用于地理位置的存储和查找，必须使用 GIS 函数来维护数据

## 索引优化

1. 不在索引列做计算，等号左边无计算，等号右边无类型转换
2. 需要时使用多列索引
3. 最左前缀法则，不能跳过中间列，选择性强的列在前
4. 前缀索引，blob，text，varchar 等使用前缀索引
5. 覆盖索引，避免回表，减小数据读取量，对于只缓存索引的存储引擎，可以避免多余的系统调用

## 使用场景

1. 小表直接全表扫描优于索引维护
2. 中大型表使用索引非常有效
3. 特大型表，需要使用分区技术，建立和维护索引的代价较大

# explain/desc

- id 数字大的优先级高
- select_type 查询类型，如简单，联合，子查询
- table
- type 查询的访问类型，如 system，const，eq_ref，ref，range 等
- possible_keys
- key 使用的索引
- key_len
- ref
- rows 检索的行数
- Extra 如 using filesort，using index，using where 等

## 优化查询

1. 减少请求的数据量（必要行、必要列、缓存）
2. 减少服务器 I/O（索引）
3. 切分大查询
4. 分解大连接查询

# 函数

1. soundex()

# 存储过程

# 游标
