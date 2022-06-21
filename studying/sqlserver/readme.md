<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [常见问题](#常见问题)
  - [新装 SQL 在局域网无法连接的问题](#新装-sql-在局域网无法连接的问题)
  - [sql insert 常见问题](#sql-insert-常见问题)
  - [query 中调用 sum 函数报错：将 expression 转换为数据类型 int 时出现算术溢出错误](#query-中调用-sum-函数报错将-expression-转换为数据类型-int-时出现算术溢出错误)
- [常用操作](#常用操作)
  - [手动清理日志](#手动清理日志)
  - [数据迁移](#数据迁移)
- [常用 sql](#常用-sql)
  - [1. update left join (关联表做 update)](#1-update-left-join-关联表做-update)
  - [2. 表的行数统计](#2-表的行数统计)
  - [3. 表的大小统计](#3-表的大小统计)
  - [4. 查看当前连接数](#4-查看当前连接数)
  - [5. 删除连接](#5-删除连接)
  - [6. 恢复挂起](#6-恢复挂起)
  - [7. 打开 Ad Hoc Distributed Queries](#7-打开-ad-hoc-distributed-queries)
  - [8. 跨库导表](#8-跨库导表)
  - [9. 清理日志](#9-清理日志)
  - [10. 查看锁与解锁](#10-查看锁与解锁)
  - [11. 默认备份压缩](#11-默认备份压缩)
  - [12. 正在还原](#12-正在还原)
  - [13. 清理备份文件](#13-清理备份文件)
  - [14. sa 登录失败](#14-sa-登录失败)
  - [15. 事务隔离级别](#15-事务隔离级别)

<!-- /code_chunk_output -->

# 常见问题

## 新装 SQL 在局域网无法连接的问题

1. 确认服务器 SQL Service 服务是否已启动, 测试方法: 在服务器本地启动 SSMS,连接本地的 SQL 实例.
2. 确认 SQL 参数 remote admin connections 的值是否为 1. 测试方法: sp_configure 'remote admin connections'
3. 确认 SQL 实例是否已启用 SQL 和 Windows 验证. 测试方法: SSMS-->SQL 实例-->右键-->属性-->安全-->验证模式-->应是 SQL 与 Windows 验证.
4. 入站规则中添加端口：1433，5022

## sql insert 常见问题

1. 从 bcp 客户端收到一个对 colid 9 无效的列长度。

> 表示长度超出

2. 来自数据源的 String 类型的给定值不能转换为指定目标列的类型 nvarchar。

> 表示输入的 string 值中包含了单引号， 解决办法： string str = this.FErrorInfo.Replace("'", "''");

3. nvarchar 的长度 1 相当于 2 字节，对应于 varchar 的长度 2，反之 varchar 类型的字段中如果出现了汉字，它的长度会翻倍；

## query 中调用 sum 函数报错：将 expression 转换为数据类型 int 时出现算术溢出错误

|   类型   |  长度   |                范围                 |                    备注                     |
| :------: | :-----: | :---------------------------------: | :-----------------------------------------: |
|  bigint  | 8 bytes | -2<sup>63</sup> 至 2<sup>63</sup>-1 | -9223372036854775808 到 9223372036854775807 |
|   int    | 4 bytes | -2<sup>31</sup> 至 2<sup>31</sup>-1 |       -2,147,483,648 到 2,147,483,647       |
| smallint | 2 bytes | -2<sup>15</sup> 至 2<sup>15</sup>-1 |              -32,768 到 32,767              |
| tinyint  | 1 bytes |        0 至 2<sup>8</sup>-1         |                  0 到 255                   |

sum 操作发生算术溢出，处理方式是在 sum 之前将数据类型转为 bigint：

```sql
cast(colname, bigint)
convert(numeric(20,0), colname)
```

# 常用操作

## 手动清理日志

分离 -> 删除 .log 文件 -> 附加（删除不存在的日志行）

```sql
sp_configure 'remote admin connections', 1;
GO
RECONFIGURE;
GO
sp_configure 'remote admin connections'
```

## 数据迁移

1. select 所需列 into tmp_XXX from XXX;
2. 生成脚本 -> 选择 tmp_XXX;
3. 列出自增长的表，补充语句

```sql
set IDENTITY_INSERT XXX ON;
insert .... ;
set IDENTITY_INSERT XXX ON;
```

# 常用 sql

## 1. update left join (关联表做 update)

```sql
update a set a.number=b.pnumber from aaa a left join ( select provice,sum(number) as pnumber from bbb group by provice)b on a.provice=b.provice
```

## 2. 表的行数统计

```sql
select a.name, b.rows from sysobjects a inner join sysindexes b on a.id = b.id where b.indid in (0,1) and a.type='u' order by b.rows desc
```

## 3. 表的大小统计

```sql
create table #Data(name varchar(100),row varchar(100),reserved varchar(100),data varchar(100),index_size varchar(100),unused varchar(100))

declare @name varchar(100)
declare cur cursor  for
    select name from sysobjects where xtype='u' order by name
open cur
fetch next from cur into @name
while @@fetch_status=0
begin
    insert into #data
    exec sp_spaceused   @name
    print @name

    fetch next from cur into @name
end
close cur
deallocate cur

create table #DataNew(name varchar(100),row int,reserved int,data int,index_size int,unused int)

insert into #dataNew
select name,convert(int,row) as row,convert(int,replace(reserved,'KB','')) as reserved,convert(int,replace(data,'KB','')) as data,
convert(int,replace(index_size,'KB','')) as index_size,convert(int,replace(unused,'KB','')) as unused from #data

select * from #dataNew order by reserved desc
```

## 4. 查看当前连接数

```sql
exec sp_who
```

## 5. 删除连接

```sql
kill [spid]
```

## 6. 恢复挂起

```sql
ALTER DATABASE xxx SET EMERGENCY
GO
alter database xxx set single_user with rollback immediate
go
alter database xxx Rebuild Log on (name=xxx_log,filename='E:\XXX\xxx_log.ldf')
go
alter database xxx set multi_user
go
GO
```

[正在恢复处理方式](https://blog.csdn.net/yenange/article/details/80308566)

## 7. 打开 Ad Hoc Distributed Queries

```sql
exec sp_configure 'show advanced options',1
reconfigure
exec sp_configure 'Ad Hoc Distributed Queries',1
reconfigure
```

## 8. 跨库导表

```sql
insert into openrowset('sqloledb','ip';'user';'pwd',db.dbo.table)
select * from table
```

## 9. 清理日志

```sql
dbcc shrinkfile(N'xxx_log', 1);
dbcc shrinkfile(N'xxx_log_sec', 1);
dbcc shrinkfile(N'xxx_log_thi',1);

ALTER DATABASE xxx SET RECOVERY SIMPLE WITH NO_WAIT
ALTER DATABASE xxx SET RECOVERY SIMPLE   --简单模式
DBCC SHRINKFILE (N'xxx_log' , 1, TRUNCATEONLY)   -- 1 是大小  1M
DBCC SHRINKFILE (N'xxx_log_2' , 1, TRUNCATEONLY)
DBCC SHRINKFILE (N'xxx_log_3' , 1, TRUNCATEONLY)
ALTER DATABASE xxx SET RECOVERY FULL WITH NO_WAIT
ALTER DATABASE xxx SET RECOVERY FULL  --还原为完全模式
```

## 10. 查看锁与解锁

```sql
--查看锁表：
select
	request_session_id as spid
	, OBJECT_NAME(resource_associated_entity_id) as tableName
from sys.dm_tran_locks
where resource_type='OBJECT'


--解锁：
declare @spid  int
Set @spid  = 58 --锁表进程
declare @sql varchar(1000)
set @sql='kill '+cast(@spid as varchar)
exec(@sql)
```

## 11. 默认备份压缩

```sql
EXEC sp_configure 'backup compression default', '1'
RECONFIGURE WITH OVERRIDE
GO
```

## 12. 正在还原

```sql
restore database xxx with recovery
```

## 13. 清理备份文件

1. File Type = 0 for backup files or 1 for report files.
2. Folder Path = The folder to delete files. The path must end with a backslash "\".
3. File Extension = This could be 'BAK' or 'TRN' or whatever you normally use.
4. Date = The cutoff date for what files need to be deleted.
5. Subfolder = 0 to ignore subfolders, 1 to delete files in subfolders.

```sql
-- 清理三天以前的所有 bak 备份文件
DECLARE @OLDDATE DATETIME
SELECT @OLDDATE=GETDATE()-3
EXECUTE master.dbo.xp_delete_file 0 ,N'E:\DB\bak\',N'bak',@OLDDATE,0;
```

## 14. sa 登录失败

1. 启用并授权 sa 账号
2. 启用 Windows 和 账号登录混合模式
3. SQL Server 配置管理工具中的 所有 Named Pipes 的 TCP/IP 协议启用起来
4. 关闭 sa 账号的"强制密码策略"选项

## 15. 事务隔离级别

```sql
-- 查看 isolation
dbcc useroptions

-- read uncommitted
-- read committed
-- repeatable read
-- serialize

-- 设置 isolation
set transaction isolation level read committed
```

## 16. 查看 session id 对应的 SQL

```sql
SELECT
    c.session_id, c.net_transport, c.encrypt_option,
    c.auth_scheme, s.host_name, s.program_name,
    s.client_interface_name, s.login_name, s.nt_domain,
    s.nt_user_name, s.original_login_name, c.connect_time,
    s.login_time,q.text
FROM sys.dm_exec_connections AS c
JOIN sys.dm_exec_sessions AS s
    ON c.session_id = s.session_id
cross apply fn_get_sql(most_recent_sql_handle) q
where c.session_id='70'
```
