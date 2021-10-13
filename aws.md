# 数据湖环

    对象存储 -> S3 -> Athena(SQL 查询)
    关系数据库 -> Aurora
    大数据处理 -> EMR
    日志分析 -> ES -> 数据热度分成（冷、暖、热）
    数据仓库 -> Redshift
    机器学习 -> SageMaker
    非关系数据库 -> DynamoDB

    流处理 -> Kinesis Data Streams(Kafka)
          -> Kinesis Data Anlysis(Flink)
    数据服务 -> Glue(数据集成，ETL 流，数据目录)
    数据安全 -> Lake Formation(安全规则)
    数据质量

# 丰田互联

    S3 -> EMR(Hadoop + Spark)

1. 为什么替换

   无限扩容
   技术兼容
   费用节省

# Framework

    Source - OLTP ERP CRM
    Ingestion - Glue
    Storage - S3
    Gatalog -
    Processing - EMR
    Consumer -

# 用户画像

- 标签

  - 社会属性
  - 规则类标签（条件符合）
  - 机器学习标签

# 运营分析

运算资源
存储资源（4\*3/1）

# 日志分析

异构数据集成
数据链路（即系查询）

CAPEX -> OPEX

# Salesforce CDP

速度 50W RPS / Cluster
多样性 -> One ID
体量
一致性
价值

# 云数仓 Redshift

## 场景

1. 欣和
2. 李宁
3. 纳斯达克

## 架构

Redshift -> S3 外部表
Concurrency Scaling -> RDS 镜像复制
RA3 -> 计算存储分离 -> 高速缓存
Data Sharing -> 跨集群数据共享（Producer -> Consumer）

# EMR 最佳实践

## S3 架构

list:get 1:1000

按需算力相对节省程度（相对自建-小规模）
Dataworks/DGC 相对优势
费用优势

1. RDS 性能压力
2. 运行时数据
