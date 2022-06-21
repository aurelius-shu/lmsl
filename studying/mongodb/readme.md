# MongoDB

<!-- @import "[TOC]" {shell="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [MongoDB](#mongodb)
  - [NoSql](#nosql)
    - [RDBMS vs NoSQL](#rdbms-vs-nosql)
    - [NoSQL 的优点/缺点](#nosql的优点缺点)
    - [NoSQL 数据库分类](#nosql数据库分类)
  - [MongoDB 基本介绍&&下载安装](#mongodb基本介绍下载安装)
    - [基本介绍](#基本介绍)
    - [sql&&MongoDB 概念比对](#sqlmongodb概念比对)
    - [下载安装](#下载安装)
  - [MongoDB 脚本](#mongodb脚本)
    - [基本增删改查](#基本增删改查)
    - [高级](#高级)
  - [副本集设置、分片存储](#副本集设置-分片存储)
  - [数据备份与恢复](#数据备份与恢复)
  - [MongoDB 监控](#mongodb-监控)
  - [.Net&&MongoDB](#netmongodbhttpswwwcnblogscompasorakup9634946html)

<!-- /code_chunk_output -->

## NoSql

非关系型的数据库

### RDBMS vs NoSQL

- RDBMS
  - 高度组织化结构化数据
  - 结构化查询语言（SQL） (SQL)
  - 数据和关系都存储在单独的表中。
  - 数据操纵语言，数据定义语言
  - 严格的一致性
  - 基础事务
- NoSQL
  - 代表着不仅仅是 SQL
  - 没有声明性查询语言
  - 没有预定义的模式
  - 键 - 值对存储，列存储，文档存储，图形数据库
  - 最终一致性，而非 ACID 属性
  - 非结构化和不可预知的数据
  - CAP 定理
  - 高性能，高可用性和可伸缩性

### NoSQL 的优点/缺点

- 优点:
  - 高可扩展性
  - 分布式计算
  - 低成本
  - 架构的灵活性，半结构化数据
  - 没有复杂的关系
- 缺点:
  - 没有标准化
  - 有限的查询功能（到目前为止）
  - 最终一致是不直观的程序

### NoSQL 数据库分类

- 列存储
- 文档存储
- key-value 存储
- 图存储
- 对象存储
- xml 数据库

## MongoDB 基本介绍&&下载安装

### 基本介绍

- 介绍：MongoDB 是一个基于分布式文件存储的数据库。由 C++语言编写。旨在为 WEB 应用提供可扩展的高性能数据存储解决方案。
- 特点：高性能、易部署、易使用，存储数据非常方便。
- 主要功能特性有：
  面向集合存储，易存储对象类型的数据
  模式自由
  支持动态查询
  支持完全索引，包含内部对象
  支持查询
  支持复制和故障恢复
  使用高效的二进制数据存储，包括大型对象（如视频等）
  自动处理碎片，以支持云计算层次的扩展性
  支持 RUBY，PYTHON，JAVA，C++，PHP 等多种语言
  文件存储格式为 BSON（一种 JSON 的扩展）
  可通过网络访问
- [与关系型数据库相比，MongoDB 的优缺点](http://blog.sina.com.cn/s/blog_966e430001019s8v.html)

  - 优点
    弱一致性（最终一致），更能保证用户的访问速度
    文档结构的存储方式，能够更便捷的获取数据
    内置 GridFS。GridFS 是一个出色的分布式文件系统，可以支持海量的数据存储。
    内置 Sharding。
    第三方支持丰富
    性能优越
  - 缺点
    mongodb 不支持事务操作
    mongodb 占用空间过大
    MongoDB 没有如 MySQL 那样成熟的维护工具

- 使用原理
  所谓“面向集合”（Collenction-Oriented），意思是数据被分组存储在数据集中，被称为一个集合（Collenction)。每个集合在数据库中都有一个唯一的标识名，并且可以包含无限数目的文档。集合的概念类似关系型数据库（RDBMS）里的表（table），不同的是它不需要定义任何模式（schema)。
  模式自由（schema-free)，意味着对于存储在 mongodb 数据库中的文件，我们不需要知道它的任何结构定义。如果需要的话，你完全可以把不同结构的文件存储在同一个数据库里。存储在集合中的文档，被存储为键-值对的形式。键用于唯一标识一个文档，为字符串类型，而值则可以是各种复杂的文件类型。我们称这种存储形式为 BSON（Binary JSON）。

### sql&&MongoDB 概念比对

| sql    | MongoDB   |
| ------ | --------- |
| 数据库 | 数据库    |
| 表     | 集合      |
| 行     | 文档      |
| 列     | 字段      |
| 索引   | 索引      |
| 表连接 | 嵌入文档  |
| 主键   | \_id 字段 |

![sql和MongoDB基本概念对比](https://www.runoob.com/wp-content/uploads/2013/10/Figure-1-Mapping-Table-to-Collection-1.png)

### 下载安装

- [下载地址](https://www.mongodb.com/download-center/community)，win7 下载 mongodb-win32-x86_64-2008plus-3.4.24-signed.msi
- 创建数据目录：E:\Mangodb\data\db
- 启动 MongoDB 服务器

```shell
#以管理员身份启动命令行，并运行
d:\mongodb\bin\mongod --dbpath E:\Mangodb\data\db
```

- 连接 MongoDB 数据库

```shell
D:\MongoDB\bin\mongo.exe
```

- [MongoDB 客户端下载地址](https://downloads.mongodb.com/compass/mongodb-compass-1.28.1-win32-x64.zip)

  - 标准 URI 连接语法:
    mongodb://[username:password@]host1[:port1],host2[:port2],...[,hostN[:portN]]][/[database][?options]]

  - mongodb:// 这是固定的格式，必须要指定。
  - username:password@ 可选项，如果设置，在连接数据库服务器之后，驱动都会尝试登录这个数据库
  - host1 必须的指定至少一个 host, host1 是这个 URI 唯一要填写的。它指定了要连接服务器的地址。如果要连接复制集，请指定多个主机地址。
  - portX 可选的指定端口，如果不填，默认为 27017
  - /database 如果指定 username:password@，连接并验证登录指定数据库。若不指定，默认打开 test 数据库。
  - ?options 是连接选项。如果不使用/database，则前面需要加上/。所有连接选项都是键值对 name=value，键值对之间通过&或;（分号）隔开

## MongoDB 脚本

### 基本增删改查

```shell
#如果数据库不存在，则创建数据库，否则切换到指定数据库
use DATABASE_NAME

#查看所有数据库
show dbs

#删除数据库
use DATABASE_NAME
db.dropDatabase()

#创建集合
use DATABASE_NAME
db.createCollection("CollectionName",options)
#创建固定集合，整个集合空间大小 6142800 B, 文档最大个数为 10000 个。
db.createCollection("CollectionName", { capped : true, autoIndexId : true, size : 6142800, max : 10000 } )

#查询集合
show collections

#删除集合
use DATABASE_NAME
db.CollectionName.drop()

#插入文档
db.CollectionName.insert({title: 'MongoDB 教程',
                    description: 'MongoDB 是一个 Nosql 数据库',
                    url: 'http://www.runoob.com',
                    tags: ['mongodb', 'database', 'NoSQL'],
                    likes: 100
                    })

#查看文档
db.CollectionName.find()
db.CollectionName.find().pretty() #以易读的方式来读取数据
db.CollectionName.find({"key1":"MongoDB"}).pretty()  #where key1 = 'MongoDB'
db.CollectionName.find({"key1":{$lt:50}}).pretty() #where key1 < 50
db.CollectionName.find({"key1":{$lte:50}}).pretty() #where key1 <= 50
db.CollectionName.find({"key1":{$gt:50}}).pretty() #where key1 > 50
db.CollectionName.find({"key1":{$gte:50}}).pretty() #where key1 >= 50
db.CollectionName.find({"key1":{$ne:50}}).pretty() #where key1 != 50
db.CollectionName.find({key1:value1, key2:value2}).pretty() #where key1=value1 and key2=value2
db.CollectionName.find({$or:[{"key1":"value1"},{"key2": "value2"}]}).pretty() #where key1=value1 or key2=value2
db.CollectionName.find({"key1" : {$type : 2}}) #获取集合中key1为string类型的数据
db.CollectionName.find({"key1" : {$type : 'string'}}) #获取集合中key1为string类型的数据
db.CollectionName.find().limit(NUMBER)
db.CollectionName.find().limit(NUMBER).skip(NUMBER2)
db.CollectionName.find().sort({KEY:1}) #1 为升序排列，而 -1 是用于降序排列。

#聚合
$project：修改输入文档的结构。可以用来重命名、增加或删除域，也可以用于创建计算结果以及嵌套文档。
$match：用于过滤数据，只输出符合条件的文档。$match使用MongoDB的标准查询操作。
$limit：用来限制MongoDB聚合管道返回的文档数。
$skip：在聚合管道中跳过指定数量的文档，并返回余下的文档。
$unwind：将文档中的某一个数组类型字段拆分成多条，每条包含数组中的一个值。
$group：将集合中的文档分组，可用于统计结果。
$sort：将输入文档排序后输出。
$geoNear：输出接近某一地理位置的有序文档。
db.CollectionName.aggregate([{$group : {_id : "$by_user", num_tutorial : {$sum : 1}}}]) #计算每个作者所写的文章数
db.CollectionName.aggregate([{$group : {_id : "$by_user", num_tutorial : {$sum : "$likes"}}}])
db.CollectionName.aggregate([{$group : {_id : "$by_user", num_tutorial : {$avg : "$likes"}}}])
db.CollectionName.aggregate([{$group : {_id : "$by_user", num_tutorial : {$min : "$likes"}}}])
db.CollectionName.aggregate([{$group : {_id : "$by_user", num_tutorial : {$max : "$likes"}}}])
db.CollectionName.aggregate([{$group : {_id : "$by_user", url : {$push: "$url"}}}])
db.CollectionName.aggregate([{$group : {_id : "$by_user", url : {$addToSet : "$url"}}}])
db.CollectionName.aggregate([{$group : {_id : "$by_user", first_url : {$first : "$url"}}}])
db.CollectionName.aggregate([{$group : {_id : "$by_user", last_url : {$last : "$url"}}}])


#更新文档
#只更新第一条记录
db.CollectionName.update( { "count" : { $gt : 1 } } , { $set : { "test2" : "OK"} } );
#全部更新：
db.CollectionName.update( { "count" : { $gt : 3 } } , { $set : { "test2" : "OK"} },false,true );
#只添加第一条：
db.CollectionName.update( { "count" : { $gt : 4 } } , { $set : { "test5" : "OK"} },true,false );
#全部添加进去:
db.CollectionName.update( { "count" : { $gt : 5 } } , { $set : { "test5" : "OK"} },true,true );

#删除文档
db.CollectionName.remove({'title':'MongoDB 教程'})
db.CollectionName.remove({}) #删除所有文档

#创建索引
db.CollectionName.createIndex(keys, options)
db.CollectionName.createIndex({"title":1})
db.CollectionName.createIndex({"title":1,"description":-1})
#创建子文档字段索引
db.CollectionName.ensureIndex({"address.city":1,"address.state":1,"address.pincode":1})
#explain 操作提供了查询信息，使用索引及查询统计等。有利于对索引的优化。
db.CollectionName.find({title:"MongoDB"},{description:"xxx"}).explain()
#hint()指定查询使用某个索引
db.CollectionName.find({gender:"M"},{user_name:1,_id:0}).hint({gender:1,user_name:1})
```

### 高级

- 文档关系
  - 嵌入式关系
  ```
      {
          "_id":ObjectId("52ffc33cd85242f436000001"),
          "name": "Tom Benzamin",
          "address": [
              {
                  "city": "Los Angeles",
                  "state": "California"
              },
              {
                  "city": "Chicago",
                  "state": "Illinois"
              }]
          }
  ```
  - 引用式关系
  ```
      {
          "_id":ObjectId("52ffc33cd85242f436000001"),
          "contact": "987654321",
          "dob": "01-01-1991",
          "name": "Tom Benzamin",
          "address_ids": [
              ObjectId("52ffc4a5d85242602e000000"),
              ObjectId("52ffc4a5d85242602e000001")
          ]
      }
  ```
  - 引用别的数据库或集合中的文档
  ```
      {
          "_id":ObjectId("53402597d852426020000002"),
          "address":
          {
              "$ref": "address_home",
              "$id": ObjectId("534009e4d852427820000002"),
              "$db": "runoob"
          },
          "contact": "987654321",
          "dob": "01-01-1991",
          "name": "Tom Benzamin"
      }
  ```

## 副本集设置、分片存储

```shell
mongod --port "PORT" --dbpath "YOUR_DB_DATA_PATH" --replSet "REPLICA_SET_INSTANCE_NAME"
#启动一个名为rs0的MongoDB实例，其端口号为27017。
mongod --port 27017 --dbpath "D:\set up\mongodb\data" --replSet rs0
#启动一个新的副本集
rs.initiate()
#副本集添加成员
rs.add(HOST_NAME:PORT)
#查看副本集状态
rs.status()
查看副本集的配置
rs.conf()
#判断当前运行的Mongo服务是否为主节点
db.isMaster()
```

## 数据备份与恢复

- 备份

```shell
#进入MongoDB安装目录的bin目录输入:
mongodump -h dbhost -d dbname -o dbdirectory
-h：MongoDB 所在服务器地址
-d：需要备份的数据库实例，例如：test
-o：备份的数据存放位置
```

- 恢复

```shell
mongorestore -h <hostname><:port> -d dbname <path>
```

## MongoDB 监控

mongostat 是 mongodb 自带的状态检测工具，在命令行下使用。它会间隔固定时间获取 mongodb 的当前运行状态，并输出。
mongotop 提供了一个方法，用来跟踪一个 MongoDB 的实例，查看哪些大量的时间花费在读取和写入数据。
mongotop 提供每个集合的水平的统计数据。默认情况下，mongotop 返回值的每一秒。

## [.Net&&MongoDB](https://www.cnblogs.com/pasoraku/p/9634946.html)

```c#
using MongoDB.Bson;
using MongoDB.Driver;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MongoDBDemo
{
    public class Program
    {
        static void Main(string[] args)
        {
            var client = new MongoClient("mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb");
            var database = client.GetDatabase("test");
            var collection = database.GetCollection<BsonDocument>("student");
            //添加文档
            AddData(collection);
            //查找文档
            FindData(collection);
            //更新文档
            UpdateData(collection);
            //删除文档
            DeleteData(collection);
            Console.ReadLine();
        }

        static void AddData(IMongoCollection<BsonDocument> collection)
        {
            BsonDocument student = new BsonDocument();
            student.Add("name", "小红");
            student.Add("age", 26);
            collection.InsertOne(student);
        }

        static void FindData(IMongoCollection<BsonDocument> collection)
        {
            var result =collection.Find(Builders<BsonDocument>.Filter.Eq("name", "小红"));
            Console.WriteLine(result.ToJson());
        }

        static void UpdateData(IMongoCollection<BsonDocument> collection)
        {
            collection.UpdateMany(Builders<BsonDocument>.Filter.Eq("name", "小红"), Builders<BsonDocument>.Update.Set("age", 30));
        }

        static void DeleteData(IMongoCollection<BsonDocument> collection)
        {
            collection.DeleteOne(Builders<BsonDocument>.Filter.Eq("name", "小红"));
        }
    }
}

```
