1. 数据采集
    1. OSS日志采集通道 - 数据流向：ERP App -> OBS/S3/JDCloud -> Kafka -> flume -> HDFS
    2. Janitor (Python) - 一种百万级跨平台异构数据迁移代理服务（已申请专利）

2. 数据分析（ETL：Hive、Azkaban、DataX；应用端: .Net Core + MySQL/SqlServer + Redis + Vue）
    1. 客户画像、用户画像
    2. 用户行为分析
    3. 产品质量分析
    4. 新特性分析
    5. 客户成功

3. 云服务平台 (Spring Boot + MySQL + Redis + Vue)
    1. 云资讯 - 主要功能精准推送 (基于数据分析+标签系统)
    2. 云评价 - 主要功能全方位收集用户评价信息
    3. 云管理中心 - 主要功能是，通过在线 Web 管理界面，实现 ERP 系统、Janitor代理服务、其他异构系统等的远程配置管理（在线服务管理）

4. 标签系统 (Python) - 基于数据分析，对任意对象实现自定义规则的标签，并自动化生成标签，提供发布、订阅、调用标签的功能

5. ERP 产品（金蝶云星空）
    1. 管理中心 - 用来管理业务站点、业务账套、License 等
    2. 健康中心 - 集群软硬件参数监控与展示（后以 Zabbix 替代）
    3. 数据结转 - 备份并清理 ERP 业务账套中的过期数据
    4. 集成平台 - 同步异构 ERP 系统的业务数据，促成客户更换本 ERP 系统
    5. 报表 - ERP 相关报表

6. 数仓治理
    1. 根据数据来源、数据所处业务阶段、数据纬度共性、数据应用场景等，通过 Hive 库表，将 HDFS 的所有数据分层，搭建严密逻辑体系；
    2. 通过 Azkaban 实现数据处理流任务调度;
    3. 通过 DataX 打通数仓与各应用端的同步通道，将应用数据导入各应用系统
    4. 数据字典
