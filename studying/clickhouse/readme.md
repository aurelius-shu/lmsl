<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [ClickHouse 的诞生](#clickhouse-的诞生)
  - [OLAP 常见架构](#olap-常见架构)
  - [OLAP 技术演进](#olap-技术演进)
  - [ClickHouse 发展历程](#clickhouse-发展历程)
  - [ClickHouse 不擅长的场景](#clickhouse-不擅长的场景)
- [架构概览](#架构概览)
  - [核心特性](#核心特性)
  - [架构设计](#架构设计)
  - [快的原因](#快的原因)
- [安装部署](#安装部署)
  - [安装方式](#安装方式)
  - [目录结构](#目录结构)
- [数据定义](#数据定义)
  - [数据类型](#数据类型)
  - [定义数据表](#定义数据表)
  - [操作数据表](#操作数据表)
  - [操作数据分区](#操作数据分区)
  - [分布式 DDL](#分布式-ddl)
  - [写入数据](#写入数据)
  - [删除与修改数据](#删除与修改数据)
- [数据字典](#数据字典)
  - [内置字典](#内置字典)
  - [外部扩展字典](#外部扩展字典)
- [MergeTree 原理](#mergetree-原理)
  - [创建方式和存储结构](#创建方式和存储结构)

<!-- /code_chunk_output -->

# ClickHouse 的诞生

## OLAP 常见架构

多维分析（聚合查询）

- 下钻
- 上卷
- 切片
- 切块
- 旋转

1. ROLAP(Relational - 关系型)
2. MOLAP(Multidimensional - 多维型): 预聚合
3. HOLAP(Hybrid - 混合架构)

## OLAP 技术演进

1. 关系型数据库阶段
2. 大数据技术阶段
3. 搜索引擎

## ClickHouse 发展历程

1. MySQL: 采用 MyISAM，单独存储 B+Tree 索引文件和数据文件；随机读写，磁盘碎片
2. Metrage: Key Value 存储模型，LSM 索引，预聚合；维度爆炸，不支持自定义分析
3. OLAPServer: 结合 MyISAM 和 LSM，存储采用关系模型，索引与数据分开存储，列式存储；数据类型单一
4. ClickHouse: 完备的 DBMS 为目标；Click Stream + Data WareHouse

## ClickHouse 不擅长的场景

1. 不支持事务
2. 不擅长根据主键进行行粒度的查询，不应该当做 Key-Value 数据库使用
3. 不擅长按行删除数据

# 架构概览

手动、多主对等网络结构

## 核心特性

1. 完备的 DBMS
   - DDL（数据定义语言）
   - DML（数据操作语言）
   - 权限控制
   - 数据备份与恢复
   - 分布式管理
2. 列式存储与数据压缩
   - 减少查询扫描范围
   - 按列压缩同类数据
3. 向量化执行引擎
   - CPU 的 SIMD 指令（Simple Instruction Multiple Data，单条指令操作多条数据，SSE 4.2 指令集），通过 CPU 寄存器层面实现数据级并行（其他：指令级并行、线程级并行）
4. 关系模型与 SQL 查询
   - 更好的群众基础
   - 更好的可集成性
   - 更好的描述能力
   - OLAP 应用的模型传承（关系模型：星型模型、雪花模型、宽表模型）
5. 多样化表引擎（继承了 MySQL 的思路）
   - 通用于场景化支持的选择
   - 特定的表引擎支持特定的场景
6. 多线程与分布式
   - SIMD 不适用于含有较多分支判断的场景，多线程正好可以与之形成互补
   - 分区（纵向扩展，利用多线程原理）
   - 分片（横向扩展，利用分布式原理） - 计算移动比数据移动更划算
7. 多主架构
   - 所有节点功能相同，规避单点故障
   - 适用于多数据中心，异地多活场景
8. 在线查询
   - 极快的响应，无需预处理
   - 极快又开源
9. 数据分片与分布式查询
   - 一个集群由多个分片组成（一个分片只能对应一个服务节点）
   - Distributed Table（访问代理，类似分库中间件）

## 架构设计

1. Column 与 Field
2. DataType
3. Block 与 Block 流
4. Table
5. Parser 与 Interpreter
6. Functions 与 Aggregate Functions
7. Cluster 与 Replication

## 快的原因

自下而上的设计原则，目的很单纯

1. 着眼硬件，先想后做
   - 硬件效率最大化（内存中 Group By，使用 HashTable 装载数据，注重 CPU L3 级别缓存）
2. 算法在前，抽象在后
   - 面对重复场景，算法性能最优化
3. 用于尝鲜，不行就换
4. 特定场景，特殊优化
5. 持续测试，持续改进

# 安装部署

## 安装方式

1. 源码编译
2. 预编译压缩包
3. Docker 镜像
4. RPM

## 目录结构

# 数据定义

## 数据类型

1. 基础类型
   - 数字（Int/UInt/Float/Decimal）
   - 字符串（String/FixedString/UUID）
   - 时间（DateTime/DateTime64/Date）
2. 复合类型
   - 数组（Array）
   - 元组（Tuple）
   - 枚举（Enum）
   - 嵌套（Nested）
3. 特殊类型
   - Nullable
   - Domain

## 定义数据表

1. 数据库
   - Ordinary（默认库引擎，可以使用任意表引擎）
   - Dictionary（字典引擎，为数据字典创建数据表）
   - Memory（内存引擎，存放临时数据，数据表只会停留在内存中，服务重启数据会丢失）
   - Lazy（日志引擎，只能使用 Log 系列的表引擎）
   - MySQL（MySQL 引擎，为远端 MySQL 表自动创建数据表并拉去数据）
2. 数据表
   - create table ... ENGINE = engine
   - create table as ... ENGINE = engine
   - create table as select ... ENGINE = engine
3. 默认值表达式
   - 定义默认值的字段将不被强制要求定义数据类型，ClickHouse 会根据默认值推断字段数据类型；
   - 如果同时定义了数据类型和默认值，则以定义的数据类型为准
   * DEFAULT（支持 Insert，Select \* 包含，会被持久化）
   * MATERIALIZED（不支持 Insert，Select \* 不包含，会被持久化）
   * ALIAS（不支持 Insert，Select \* 不包含，不会被持久化）
4. 临时表
   - 数据在集群建传播的载体，一般不会被显式创建
   - 生命周期与会话绑定，不需要指定表引擎，只能是 Memory 表引擎
   - 不属于任何数据库，不需要指定库引擎，优先级高于同名的普通表
5. 分区表
   - 针对本地数据而言，纵向切分
   - 只有 MergeTree 表引擎支持
6. 视图
   - 普通视图，Select 的映射，查询代理
   - 物化视图，有独立存储，POPULATE 修饰会将源表已有数据刷入物化视图；不支持删除操作的同步

## 操作数据表

只有 MergeTree、Merge、Distributed 三类表引擎支持 ALERT 操作

1. 追加字段
2. 修改字段类型（默认值）
3. 修改备注
4. 删除字段
5. 移动数据表（只支持单节点内移动）
6. 清空数据表

## 操作数据分区

1. 查询分区信息

```sql
SELECT partition_id, name, table, database FROM system.parts WHERE table = 'tb_name'
```

2. 删除指定分区

```sql
ALTER TABLE tb_name DROP PARTITION partition_expr
```

3. 复制分区数据

```sql
ALTER TABLE B REPLACE PARTITION partition_expr FROM A
```

4. 重置分区数据

```sql
ALTER TABLE tb_name CLEAR COLUMN column_name IN PARTITION partition_expr
```

5. 卸载和装载分区

```sql
-- 卸载
ALTER TABLE tb_name DETACH PARTITION partition_expr
-- 装载
ALTER TABLE tb_name ATTACH PARTITION partition_expr
```

6. 备份和还原分区

## 分布式 DDL

在指定集群的所有节点广播 DDL 语句（需在集群模式下执行）

```sql
on cluster cluster_name
```

## 写入数据

max_insert_block_size = 1048576，在服务端处理数据具备原子性（JDBC/HTTP）

1. insert into [db.]table [(c1, c2, c3…)] values (values), (values)
2. insert into [db.]table [(c1, c2, c3…)] FORMAT format_name data_set
3. insert into [db.]table [(c1, c2, c3…)] SELECT ...

## 删除与修改数据

```sql
-- Delete
ALTER TABLE [db_name.]table_name DELETE WHERE filter_expr
-- 1. 在 mutations 系统表生成执行计划
-- 2. 在数据表根目录上传 mutation_id 文件，记录相关日志信息
-- 3. 数据的删除过程以数据表的分区为单位，将所有目录重写为新的目录，命名规则：system.mutations.block_numbers.number
-- 4. 旧数据目录不会立刻删除，表级为 active=0，在 MergeTree 引擎的下一次合并动作才会在物理意义上删除

-- Update
ALTER TABLE [db_name.]table_name UPDATE column1 = expr1 [, ...] WHERE filter_expr
-- 1. 分区建和主键不支持修改

-- Mutation 记录
SELECT database, table ,mutation_id, block_numbers.number as num ,is_done FROM system.mutations
```

# 数据字典

保存常量或经常使用的维度表数据，避免不必要的 JOIN 查询

## 内置字典

## 外部扩展字典

# MergeTree 原理

支持主键索引、数据分区、数据副本、数据采样、ALTER 相关操作

## 创建方式和存储结构

以数据片段的形式写入磁盘，数据片段不可修改，数据片段定期合并

1. 创建方式

```sql
CREATE TABLE [IF NOT EXISTS] [db_name.]table_name ( name1 [type] [DEFAULT|MATERIALIZED|ALIAS expr], name2 [type] [DEFAULT|MATERIALIZED|ALIAS expr], 省略...
) ENGINE = MergeTree()
[PARTITION BY expr] -- [选填] 分区键
[ORDER BY expr]     -- [必填] 排序键
[PRIMARY KEY expr]  -- [选填] 主键，默认由 ORDER BY 代指
[SAMPLE BY expr]    -- [选填] 抽样表达式
[SETTINGS name=value, 省略...] -- [选填]
    -- index_granularity 索引间隔粒度，默认 8192
    -- index_granularity_bytes 索引间隔自适应，默认 10 MB，0 表示不启用
    -- enable_mixed_granularity_parts 是否开启自适应索引间隔功能，默认开启
    -- merge_with_ttl_timeout 数据 TTL
    -- storage_policy 多路径存储策略
```

2. 存储结构
   - partition: 分区目
   - checksums.txt: 校验文件（二进制格式），保存余下各类文件 size 和 size 的哈希值，用于快速校验文件的完整性和正确性
   - columns.txt: 列信息文件（明文存储）
   - count.txt: 计数文件（明文存储）
   - primary.idx: 一级索引文件（二进制格式），用于存放稀疏索引
   - [Column].bin: 数据文件（压缩格式，默认 LZ4），用于存储某一列的数据
   - [Column].mrk: 列字段标记文件（二进制格式），存储 .bin 文件中数据的偏移量信息，与稀疏索引对齐，用于给 primary.idx 稀疏索引和 .bin 数据建立映射关系
   - [Column].mrk2: 使用自适应索引间隔时，标记文件以 mrk2 命名
   - partition.dat 与 minmax\_[Column].idx: 分区表达式最终生成的值和分区字段的最大最小值（二进制格式）
   - skp*idx*[Column].idx 与 skp*idx*[Column].mrk: 二级索引与其标记文件（二进制格式）
3. 数据分区
