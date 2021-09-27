# interview

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [interview](#interview)
  - [自我介绍](#自我介绍)
  - [向面试官的问题](#向面试官的问题)
  - [向 HR 的问题](#向-hr-的问题)
  - [Tenant - 20210313](#tenant-20210313)
  - [Shopee - 20210911](#shopee-20210911)
  - [Lazada - 20210913](#lazada-20210913)
  - [lazada - 20210915](#lazada-20210915)
  - [Shopee - 20210923](#shopee-20210923)
  - [腾讯 - 20210929](#腾讯-20210929)

<!-- /code_chunk_output -->

## 自我介绍

您好，我是黄超铭，2015 年本科毕业

后就职于金蝶总部星空产品事业部，从事相关技术研发工作，我从事的工作大致可以分为三块：

第一块是在刚进入金蝶的一到两年，主要从事星空基础平台的开发工作，在此期间，参与了星空集成平台、星空健康中心、云巡检、研发过程管理、构建工具等的开发，主要输出在星空业务功能补丁和内部研发过程管理和流程

第二块在入职公司一年多时，专项负责星空产品线大数据专题研发，这个过程，主要负责设计和研发了星空产品端数据的埋点采集框架的两条通道、数据采集代理服务、数据入仓、数仓建设（ods/dim/dwd/adm/tdm）

第三块与第二块耦合，主要是基于数仓中的数据做的应用于运营开发，如运营服务平台（精准吐送、配置服务、监控服务、帮助服务、反馈等）、标签系统、数据分析平台

## 向面试官的问题

1. 面试流程（技术+HR）
2. 团队大小，办公环境，出差或外派
3. 开发周期是什么样子的？瀑布/冲刺/敏捷
4. 会经常出现最后阶段冲刺还是合理安排
5. 团队如何决策
6. 每周要参加多少会议
7. 工作是否便于集中注意力
8. 汇报对象是谁
9. 您喜欢什么，您的工作是做什么
10. 工作生活平衡问题

## 向 HR 的问题

1. 职级体系，晋升通道
2. 薪酬体系，年终什么时候发，公司福利
3. 试用期多久，现在入职今年的年终奖怎么算，薪资算法
4. 人才培养计划，新员工培养体系
5. 办公地点

## Tenant - 20210313

**智慧零售 - 一面**

1. 自我介绍
   毕业学校、就职金蝶、产品介绍、工作简介（业务开发：云服务、微服务、中间件、数据仓库、数据分析方向输出）
2. 金蝶云星空产品业务介绍、技术、角色、承担工作
   星空：saas、erp、财务、供应链、等模块
   属于基础平台部：搭建底层技术框架、数据采集、分析、预测、推送工作
   数据部分框架：（没说清楚，人家问的事框架、技术）
   公有云：中间件、代理节点(内置星空客户端、)采集数据、云服务平台管控节点、通过云服务平台反推客户
   私有云：代理节点(独立的进程)
3. 采集数据的分类：
   性能、用户行为
4. 开发语言
   net、部分 java
5. 代理节点采集的服务器端是否属于你负责
   参与了部分，大致介绍一下，采集的日志等数据输出到：亚马逊 s3、华为云 obs 、京东云的对象存储。在数仓端点部分写微服务进行监控、kafka 集群、flume、
6. 是否有接口
7. 上面描述的整套服务，比较有挑战的地方在哪 1.把代理内置到 erp 服务端、且不影响 erp 产品使用、容错、降级呀 2.对象存储服务导入 kafaka 时保证数据完整性
8. 针对上面两点详细说
   描述的不清不楚，然后描述不下去了 语音时间：在 24 分钟

   kafka 同步数据这块，我们主要采取了类似元数据管理，把每个分区的执行状态记录到数据库中，每一个分区它的文件数量？ 把每个任务抽象成了一个 job，每个 job 里面负责一个区间的文件同步，分区、每个分区映射多个文件、然后说不下去了，不知道怎么描述。面试官说起自己的理解。

9. checkpoint 什么时间介入？
10. kafka 消息可用性、防丢机制
    3 个级别：all、
11. kafka 中 high watermark 机制
12. kafka 集群怎么保证高可用
13. 某些节点挂掉，也能提供服务
14. 代码消费 kafka
15. kafka 分片机制
16. 工作中用到的语言、框架
17. java 的使用地方
18. java 的垃圾回收机制、垃圾回收器有哪些、垃圾回收算法有没有了解过、
19. 常见的 object 方法
20. NIO,BIO
21. redis 内存淘汰策略
22. hive 数据倾斜问题

## Shopee - 20210911

1. 分布式事务的四种模式
2. Redis zset 为何使用跳跃表而非红黑树

## Lazada - 20210913

1. 网络通信协议与序列化协议
2. 分布式调度系统的实现
3. 云服务平台架构介绍，核心功能与重要功能介绍
4. Redis sentinel 模式的部署模式
5. 缓存击穿与雪崩问题的解决
6. 高并发问题的解决方案
7. 说一个体现你解决问题能力的例子
   - 推动数据集成中间件服务迭代
   - 推动特性分析运营

## Lazada - 20210915

1. 带领团队发展走向
   - 客户成功运营，留住并吸纳客户
   - 产品监控、质量评估、体验优化
   - 星空数字化，数据湖环

## Shopee - 20210923

1. 进程间通行方式
2. 进程、线程、协程的理解
3. Redis String 的存储结构
4. Redis ZSET 的存储结构
5. 哪些排序算法、堆排序？

## Shopee - 20210924

## 腾讯 - 20210924

**预备问题**

1. Hive 数据倾斜

```java
public  class Tree{

    private Integer value;
    public Tree left;
    public Tree right;

    public static List<Integer> deepTrace(Tree node, List<Integer> result){
        // List<Integer> result = new List<>();
        if(root == null){
            return result;
        }
        result.add(root.value);
        this.deepTrace(node.left, result);
        this.deepTrace(node.right, result);
        return result;
    }

    public Tree(int val){
        this.value= val;
    }

    public void main(String[] args){
        Tree root = new Tree(1);
        root.left = new Tree(2);
        root.right = new Tree(3);
        root.left.left = new Tree(4);
        List<Integer> result = new
        deepTrace(root, )
    }
}
```

## Lazada - 20210926

-Dnacos.standalone=true -Dnacos.home=D:\WorkSpace\projects\nacos\distribution

## 网易 - 20210927
