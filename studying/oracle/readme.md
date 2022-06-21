<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [用户管理](#用户管理)
  - [创建表空间](#创建表空间)
  - [删掉原有数据库（账号）](#删掉原有数据库账号)
  - [创建用户](#创建用户)
  - [授权给用户](#授权给用户)
- [数据还原](#数据还原)
  - [还原 oracle](#还原-oracle)
  - [删除表空间](#删除表空间)
  - [删除用户](#删除用户)
- [docker](#docker)

<!-- /code_chunk_output -->

# 用户管理

## 创建表空间

## 删掉原有数据库（账号）

```sql
-- 其中clearandinit 是要删掉的用户名，cascade表示强制删掉clearandinit下的所有对象
drop user clearandinit cascade
```

```sql
-- 表空间
create tablespace xxxxxx DATAFILE '/u01/app/oracle/oradata/xxxxxx/tablespace_kdda.dbf' size 100M autoextend on next 10M Maxsize unlimited;

-- 索引空间
create tablespace xxxxxx_IDX DATAFILE '/u01/app/oracle/oradata/xxxxxx/tablespace_kdda_idx.dbf' SIZE 100M AUTOEXTEND ON NEXT 10M MAXSIZE UNLIMITED;

-- 临时表空间
create temporary tablespace user_temp tempfile '/u01/app/oracle/oradata/xxxxxx/tablespace_kdda_idx_ods.dbf' size 100M autoextend on next 10M maxsize 100M;
```

## 创建用户

```sql
-- 默认表空间 users，(临时表空间 users，限制使用空间大小 10）
create user clearandinit identified by sa
default tablespace users(temporary tablespace users sqota 10 users);

-- 这里创建用户 aurelius，密码为 999999，使用的表空间名是 xxxxxx
create USER aurelius IDENTIFIED BY "999999" DEFAULT TABLESPACE xxxxxx;
```

## 授权给用户

```sql
-- 执行该语句给aurelius用户授权，此时aurelius用户就可以登录了。
grant all privileges to aurelius;

grant dba,connect,resource,create table,create view,create session to clearandinit;
```

# 数据还原

```sql
impdp EXCLUDE=STATISTICS remap_tablespace=EAS_D_xxxxxx_STANDARD:users DIRECTORY=DATA_PUMP_DIR DUMPFILE=xxxxxx.dmp remap_schema=xxxxxx:clearandinit table_exists_action=replace logfile=xxxxxx.log parallel=2
```

/var/app/oracle/admin/orcl/dpdump

## 还原 oracle

```sql
impdp Test_j2/sa  dumpfile=xxxxxx.dmp logfile=import1.log remap_schema=Test_j2:sa table_exists_action=replace
```

## 删除表空间

```sql
drop tablespace test_data including contents and datafiles;
```

## 删除用户

```sql
drop user ×× cascade
impdp CMH/xxxxxx directory=DATA_PUMP_DIR  dumpfile=xxxxxx.dmp logfile=cmh.log  table_exists_action=replace remap_schema=xxxxxx:CMH remap_tablespace=EAS_D_xxxxxx_STANDARD:test
```

# docker

1. 搜索 oracle 镜像

```bash
docker search oracle
```

2. 拉取镜像

```bash
docker pull sath89/oracle-12c
```

3. 查看镜像

```bash
docker images
```

4. 运行镜像，建立与宿主的映射

```bash
docker run -d -p 8080:8080 -p 1521:1521 -v /oral/data:/u01/app/oracle sath89/oracle-12c
```

5. 查看运行日志

```bash
docker logs -f ffbeb07058449672c640ddb4e59b8376dae2e3b4dd54142871da7adbc069ee79
```

6. 查看运行的镜像

```bash
docker ps -a
```

7. 进入 container

```bash
docker exec -it 9e893d773494 /bin/bash
```

8. 连接 oracle

```bash
su oracle
```

9. dba 登陆

```bash
$ORACLE_HOME/bin/sqlplus / as sysdba
```

默认密码

```
hostname: localhost
port: 1521
sid: xe
username: system
password: oracle
```

10. docker 操作

启动 docker

```bash
sudo systemctl start docker
```

开机启动 docker

```bash
sudo systemctl enable docker
```

重新启动容器

```bash
docker restart containerid
```

删除容器

```shell
docker rm containerid
```
