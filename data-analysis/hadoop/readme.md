<!-- # Hadoop 权威指南 -->

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [一、内容简介](#一-内容简介)
- [二、初识 Hadoop](#二-初识-hadoop)
- [三、关于 MapReduce](#三-关于-mapreduce)
  - [Hadoop 数据分析示例](#hadoop-数据分析示例)
    - [1. map 和 reduce](#1-map-和-reduce)
      - [map 阶段](#map-阶段)
      - [reduce 阶段](#reduce-阶段)
    - [2. Java MapReduce](#2-java-mapreduce)
      - [map 函数](#map-函数)
      - [reduce 函数](#reduce-函数)
      - [MapReduce Job](#mapreduce-job)
      - [运行 MapReduce](#运行-mapreduce)
  - [横向扩展](#横向扩展)
    - [1. 数据流](#1-数据流)
      - [MapReduce Job](#mapreduce-job-1)
      - [map task](#map-task)
      - [reduce task](#reduce-task)
    - [2. combiner 函数](#2-combiner-函数)
    - [3. 分布式作业](#3-分布式作业)
  - [Hadoop Streaming](#hadoop-streaming)
    - [1. Ruby 版本](#1-ruby-版本)
    - [2. Python 版本](#2-python-版本)
- [四、HDFS](#四-hdfs)
  - [HDFS 的设计](#hdfs-的设计)
  - [HDFS 的概念](#hdfs-的概念)
    - [1. 数据块](#1-数据块)
    - [2. namenode 和 datanode](#2-namenode-和-datanode)
    - [3. 块缓存](#3-块缓存)
    - [4. 联邦 HDFS](#4-联邦-hdfs)
    - [5. HDFS 的高可用性](#5-hdfs-的高可用性)
  - [命令行接口](#命令行接口)
    - [1. 文件系统的基本操作](#1-文件系统的基本操作)
  - [Hadoop 文件系统](#hadoop-文件系统)
    - [1. 接口](#1-接口)
  - [Java 接口](#java-接口)
    - [1. 从 Hadoop URL 读取数据](#1-从-hadoop-url-读取数据)
    - [2. FileSystem API 读取数据](#2-filesystem-api-读取数据)
    - [3. 写入数据](#3-写入数据)
    - [4. 目录](#4-目录)
    - [5. 查询文件系统](#5-查询文件系统)
      - [1. 文件元数据(FileStatus)](#1-文件元数据filestatus)
      - [2. 列出文件(listStatus)](#2-列出文件liststatus)
      - [3. 文件模式"通配"](#3-文件模式通配)
      - [4. PathFilter 对象](#4-pathfilter-对象)
    - [6. 删除数据](#6-删除数据)
  - [数据流](#数据流)
    - [1. 剖析文件读取](#1-剖析文件读取)
    - [2. 剖析文件写入](#2-剖析文件写入)
    - [3. 一致模型(coherency model)](#3-一致模型coherency-model)
  - [distcp 并行复制](#distcp-并行复制)
- [五、YARN](#五-yarn)
  - [剖析 YARN 应用运行机制](#剖析-yarn-应用运行机制)
    - [1. 资源请求](#1-资源请求)
    - [2. 应用生命期](#2-应用生命期)
    - [3. 构建 YARN 应用](#3-构建-yarn-应用)
  - [YARN 与 MR 1 相比](#yarn-与-mr-1-相比)
  - [YARN 中的调度](#yarn-中的调度)
    - [1. 调度选项](#1-调度选项)
    - [2. Capacity Scheduler 配置](#2-capacity-scheduler-配置)
    - [3. Fair Scheduler 配置](#3-fair-scheduler-配置)
    - [4. 延迟调度](#4-延迟调度)
    - [5. 主导资源公平性](#5-主导资源公平性)
  - [延伸](#延伸)
- [六、Hadoop 的 I/O 操作](#六-hadoop-的-io-操作)
  - [数据完整性](#数据完整性)
    - [1. HDFS 的数据完整性](#1-hdfs-的数据完整性)
    - [2. LocalFileSystem](#2-localfilesystem)
  - [压缩](#压缩)
  - [序列化](#序列化)
  - [基于文件的数据结构](#基于文件的数据结构)
- [七、MapReduce 应用开发](#七-mapreduce-应用开发)
  - [用于配置的 API](#用于配置的-api)
  - [配置开发环境](#配置开发环境)
  - [用 MRUnit 写单元测试](#用-mrunit-写单元测试)
  - [本地运行测试数据](#本地运行测试数据)
  - [在集群上运行](#在集群上运行)
  - [作业调优](#作业调优)
  - [MapReduce 工作流](#mapreduce-工作流)

<!-- /code_chunk_output -->

# 一、内容简介

1. Hadoop 基础组件

   1. Hadoop 宏观介绍
   2. MapReduce 简要
   3. 深入剖析 Hadoop 文件系统 HDFS
   4. Hadoop 集群资源管理系统 YARN
   5. Hadoop 的 I/O 构建模块（数据完整性、压缩、序列化及记于文件的数据结构）

2. MapReduce 深度剖析

   1. MapReduce 应用开发
   2. MapReduce 工作机制
   3. MapReduce 编程模型和使用的数据格式
   4. MapReduce 高级主题（排序和数据连接）

3. Hadoop 操作

   1. 构建集群
   2. 管理集群

4. Hadoop 相关项目

   1. 数据格式 Avro - 跨语言数据序列化库
   2. 数据格式 Parquet - 嵌套式数据的列式存储格式
   3. 数据摄入 Flume - 流数据的大批量摄入
   4. 数据摄入 Sqoop - 结构化数据存储和 HDFS 之间高效批量传输数据
   5. 数据处理 Pig - 用于大数据集的数据流开发语言
   6. 数据处理 Hive - 数据仓库 管理 HDFS 中的数据 并提供基于 SQL 的查询语言
   7. 数据处理 Crunch - MapReduce 或 Spark 上数据处理管线程序的高层次 Java API
   8. 数据处理 Spark - 面向大规模数据处理的集群计算框架，有向无环图引擎
   
   9. 数据存储 HBase - 分布式的面向列的实时数据库
   10. 协调服务 ZooKeeper - 分布式高可用协调服务， 提供用于构建分布式应用的原语集

5. 应用实例

   1. Cerner 的可聚合数据
   2. 生命数据科学
   3. Cascading

# 二、初识 Hadoop

1. 数据量很大
2. 存储 -> 硬件故障 -> replication
   分析 -> 不同来源 -> MapReduce
3. 针对整个数据集查询
4. 不仅仅是批处理（MR）
   在线读写：HBase
   资源管理：YARN
   交互式 SQL：Hive
   迭代处理：Spark
   流处理：Storm，Spark Streaming 或 Samza
   搜索：Solr
5. 优势
   1. RDBMS：磁盘的寻址速度（磁盘带宽）远远不如传输速率（磁头移速）
   2. 网络计算：网络带宽是数据中心最珍贵的资源，每个任务间彼此独立，顺序无关紧要
   3. 志愿计算：内部高速网络连接的数据中心
6. 发展史
7. 本书内容

# 三、关于 MapReduce

## Hadoop 数据分析示例

​ 获取全球气温每年的最高记录，原始数据如下：

![org](.\images\02\org.jpg)

### 1. map 和 reduce

​ MapReduce 任务过程分为两个处理阶段： map 阶段和 reduce 阶段。每个阶段都以键值对输入和输出，其类型由程序员决定。程序员还要写两个函数：map 函数和 reduce 函数。

#### map 阶段

​ map 阶段的输入是原始数据。比如以数据集的每一行作为文本输入，键则是行起始位置相对文件起始位置的偏移量。

![map 输入](.\images\02\map-input.jpg)

​ map 是数据的准备阶段，提取感兴趣的数据，除去已损记录，筛掉缺失可疑或错误的数据，map 输出如下：

![map 输出](.\images\02\map-output.jpg)

#### reduce 阶段

​ map 输出的数据由 MapReduce 框架基于键做排序分组处理，再发送给 reduce 函数。reduce 最终接受到的数据如下：

![reduce 输入](.\images\02\reduce-input.jpg)

​ reduce 函数遍历整个列表并找出最大数。reduce 输出如下：

![reduce 输出](.\images\02\reduce-output.jpg)

### 2. Java MapReduce

#### map 函数

```java
import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class MaxTemperatureMapper
    // Mapper 类是一个泛型类，有四个形参类型，分别对应 map 函数的输入键、输入值、输出键、输出值的类型
    // 这些类型由Hadoop 本身提供或自定义，便于优化网络序列化传输 ，而不直接使用 Java 内置类型
    extends MapReduceBase implements Mapper<LongWritable, Text, Text, IntWritable>{
	    private static final int MISSING = 9999;

	    @Override
	    public void map(LongWritable key, Text value, Context context)
	    	throws IOException, InterruptedException
        {

        	String line = value.toString();
            String year = line.substring(15, 19);
            int airTemperature;
           	if (line.charAt(87) == '+'){
               	airTemperature = Integer.parseInt(line.substring(88, 92));
            }
            else{
                airTemperature = Integer.parseInt(line.substring(87, 92));
            }

            String quality = line.substring(92, 93);
            if (airTemperature != MISSING && quality.matches("[01459]")){
		        context.write(new Text(year), new IntWritable(airTemperature));
            }
        }
    }
```

#### reduce 函数

```java
import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class MaxTemperatureReducer
    // Reducer 类也是泛型类，四个形参类型，对应reduce 函数的输入输出类型
    // reduce 函数的输入类型必须匹配 map 函数的输出类型。
    extends Reducer<Text, IntWritable, Text, IntWritable>{

    @Override
    public void reduce(Text key, Iterable<IntWritable> values, Context context)
        throws IOException, InterruptedException{

        int maxValue = Integer.MIN_VALUE;
        for (IntWritable value : values){
            maxValue = Math.max(maxValue, value.get());
        }
        context.write(key, new IntWritable(maxValue));
    }
}
```

#### MapReduce Job

```java
import java.io.IOException;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.input.FileOutputFormat;

public class MaxxTemperature{

    public static void main(String[] args) throws Exception{
        if (args.length != 2){
            System.err.println("Usage: MaxTemperature <input path> <output path>");
            System.exit(-1);
        }
        // 指定作业的执行范围
        Job job = new Job();
        // 将代码打包成 Jar 文件，在 Job 对象的setJarByClass()指定类，Hadoop 利用类查找包含它的Jar 文件
        job.setJarByClass(MaxTemperature.class);
        job.setJobName("Max temperature");
        // 定义输入数据路径，可以是一个文件，一个目录（目录下所有文件当做输入）或符合特定文件模式的一系列文件
        // 可以多次添加，实现多路径输入
        FileInputFormat.addInputPath(job, new Path(args[0]));
        // 指定输出路径，只能有一个
        // 在运行作业前这个路径应该是不存在的，否则 Hadoop 会报错并拒绝作业，以防数据覆盖而丢失
        FileOutputFormat.setOutputPath(job, new Path(args[1]));
        // 指定 map 类和 reduce 类
        job.setMapperClass(MaxTemperatureMapper.class);
        job.setReducerClass(MaxTemperatureReducer.class);
        // 控制 reduce 函数的输出类型，必须和 Reduce 类中定义的输出相匹配
        // 如果 map 和 reduce 的输出类型不同，则需要通过 setMapOutputKeyClass() 和 setMapOutputValueClass() 方法来单独设置 map 函数的输出类型
        // 输入的类型默认是 TextInputFormat，
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);
        // waitForCompletion 提交作业并等待执行完成
        // waitForCompletion 参数指示是否生成详细输出，将进度信息写入控制台
        // waitForCompletion 返回值表示执行的成(true)败(false)
        System.exit(job.waitForCompletion(ture) ? 0 : 1);
    }
}
```

#### 运行 MapReduce

```bash
# 命令的运行需在 jar 所在的文件夹下进行
$ export HADOOP_CLASSPATH=hadoop-examples.jar
$ MaxTemperature input/ncdc/sample.txt output
```

## 横向扩展

​ 把数据存储在分布式文件系统（HDFS），使用 Hadoop 资源管理系统 YARN，将 MapReduce 计算转移到存储有部分数据的各台机器上。

### 1. 数据流

#### MapReduce Job

​ Job 是客户端执行的一个工作单元，包含输入数据，MapReduce 的程序和配置信息。job 会被分成 map task 和 reduce task 来执行，这些 task 运行在集群的结点上，通过 YARN 进行调度。如果一个 task 失败，将会在另一个不同节点自动重新调度运行。

#### map task

​ Hadoop 将 MapReduce 的输入数据划分成等长的输入分片(input split)，为每个 split 构建一个 map task，以运行用户自定义的 map 函数处理分片中每一条记录。

​ 分片较小可以获得更好的负载均衡，但太小会增长管理分片的总时间和构建 map 任务的总时间。对大多数作业来说，分片大小趋近于一个 HDFS 的块大小（默认 128MB）比较合适，这样可以保证数据存储在单个节点上，而不会跨节点造成 map 任务的数据网络传输。

​ 在存储有输入数据的节点上运行 map 任务，可以避免集群宽带资源损耗，会获得最佳性能。调用其他机架中的节点运行 map 任务会导致机架与机架间的网络传输。

​ map 任务将输出写入本地硬盘而非 HDFS。一旦作业完成，map 的输出就可以删除。如果 map 任务在将中间结果传给 reduce 任务之前失败，Hadoop 会在另一个节点上重新运行这个 map 任务，再次构建 map 中间结果。

![map-task](.\images\02\map-task.jpg)

#### reduce task

​ reduce 任务不具备数据本地化属性，单个 reduce 的输入通常来自于所有 mapper 的输出，排序后的 map 输出通过网络传输到运行 reduce 任务的节点。数据在 reduce 端合并，然后由 用户定义的 reduce 函数处理。

​ reduce 的输出通常在 HDFS 上，以复本形式实现可靠存储。第一个复本存储在本地节点，其他复本处于可靠性考虑，通过网络带宽存储到其他机架节点中。

![reduce-task](.\images\02\reduce-task.jpg)

​ 如果有多个 reduce 任务，每个 map 任务会针对输出进行分区（partition），每个 reduce 任务建立一个分区，一个分区对应多个键。分区可以由用户定义的分区函数控制，但通常用默认 partitioner 通过哈希函数分区，很高效。map 任务和 reduce 任务之间的数据流称为混洗（shuffle）。

![reduce-task](.\images\02\shuffle.jpg)

​ reduce 任务的数量不由输入的数据大小决定，而是独立指定的。

​ 当数据处理可以完全并行而无需混洗时，可能会无 reduce 任务，此时唯一的非本地数据传输是 map 任务结果写入 HDFS。

![no-reduce-job](.\images\02\no-reduce-job.jpg)

### 2. combiner 函数

​ 为避免 map 和 reduce 任务之间的网络数据传输，Hadoop 允许用户针对 map 任务的输出指定一个 combiner 函数，将 combiner 函数的输出作为 reduce 函数的输入。combiner 的调用对 reducer 的输出结果没有影响。

```java
// 适用场景
max(0,20,10,25,15) = max(max(0,20,10), max(25,15)) = max(20,25) = 25;
// 不适用方式
mean(0,20,10,25,15) = 14;
mean(mean(0,20,10), mean(25,15))=mean(10,20)=15;
```

​ combiner 通常用于处理相同 map 输出中相同键的记录，仍需 reducer 用于处理不同 map 输出中具有相同键的记录。combiner 旨在帮助减少 map 和 reduce 间的数据传输，而非替代 reduce。

​ combiner 通过 Reducer 类来定义，可以直接将 Reducer 的实现指定到 CombinerClass 中，如下：

```java
public class MaxTemperatureWithCombiner{
    public static void main(String[] args) throws Exception{
        if (args.length != 2){
            System.err.println("Usage: MaxTemperatureWithCombiner <input path> "+ "<output path>");
            System.exit(-1);
        }

        Job job = new Job();
        job.setJarByClass(MaxTemperatureWithCombiner.class);
        job.setJobName("Max temperature");

        FileInputFormat.addInputPath(job, new Paht(args[0]));
        FileOutputFormat.setOutputPath(job, new Paht(args[1]));

        job.setMapperClass(MaxTemperatureMapper.class);
        // Combiner 实现与 Reducer 相同，可直接使用 Reducer
        job.setCombinerClass(MaxTemeratureReducer.class);
        job.setReducerClass(MaxTemperatureReducer.class);

        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);

        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
```

### 3. 分布式作业

​ 详见第六章 MapReduce 应用开发

## Hadoop Streaming

### 1. Ruby 版本

map 函数：

​ Java API 中的 map 函数一次只处理一条记录（“推”记录方式，可通过重载 cleanup() 实现多行汇聚同时处理）；而 Streaming 中，map 程序可以轻松读取并同时处理若干行，可以自己决定如何处理输入数据。

```ruby
#!/usr/bin/env ruby

# 读取STDIN中每一行，迭代执行标准输入中的每一行
STDIN.each_line do |line|
    val = line
    year, temp, q = val[15,4], val[87,5], val[92,1]
    # 如果气温有效，就将年份和气温以制表符\t隔开写为标准输出(puts)
    puts "#{year}\t#{temp}" if (temp != "+9999" && q =~ /[01459]/)
end
```

测试 ruby map 函数：

```bash
$ cat input/ncdc/sample.txt | ch02-mr-intro/src/main/ruby/max_temperaature_map.rb
```

reduce 函数：

​ Java API 的 reduce 函数是针对每个键组的迭代；而 Streaming 中，reduce 程序需要自己找出键组的边界，MapReduce 框架保证了键的有序性，如果读到一个键与前一个键不同，说明新的键组开始了。

```ruby
#!/usr/bin/env ruby

last_key, max_val = nil, -1000000
STDIN.each_line do |line|
    key, val = line.split("\t")
    # 新的键组开始
    if last_key && last_key != key
        puts "#{last_key}\t#{max_val}"
        last_key, max_val = key, val.to_i
    else
        last_key, max_val = key, [max_val, val.to_i].max
    end
    puts "#{last_key}\t#{max_val}" if last_key
```

测试 ruby MapReduce：

```bash
$ cat input/ncdc/sample.txt | \
ch02-mr-intro/src/main/ruby/max_temperature_map.rb | \
sort | ch02-mr-intro/src/main/ruby/max_temperature_reduce.rb
```

Hadoop 运行：

​ hadoop 命令不支持 Streaming，需指定 Streaming JAR 文件流与 jar 选项时指定输入和输出路径以及 map 和 reduce 脚本：

```bash
# 本地（单机）测试
$ hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-input input/ncdc/sample.txt \
-output output \
-mapper ch02-mr-intro/src/main/ruby/max_temperature_map.rb \
-reducer ch02-mr-intro/src/main/ruby/max_temperature_reduce.rb
```

```bash
# 集群测试
$ hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
# 集群运行需使用 -files 将脚本传输到集群
-files ch02-mr-intro/src/main/ruby/max_temperature_map.rb, \
ch02-mr-intro/src/main/ruby/max_temperature_reduce.rb \
-input input/ncdc/all \
-output output \
-mapper ch02-mr-intro/src/main/ruby/max_temperature_map.rb \
# 庞大数据集应该使用 -combiner 选项优化
-combiner ch02-mr-intro/src/main/ruby/max_temperature_reduce.rb \
-reducer ch02-mr-intro/src/main/ruby/max_temperature_reduce.rb
```

### 2. Python 版本

```python
#!/usr/bin/env python

# 用于查找最高气温的 map 函数（python 版）

import re
import sys

for line in sys.stdin:
    val = line.strip()
    (year, temp, q) = (val[15:19], val[87:92], val[92:93])
    if (temp != "+9999" and re.match("[01459]", q)):
        print "%s\t%s" % (year, temp)
```

```python
#!/usr/bin/env python

# 用于查找最高气温的 reduce 函数（python 版）

import sys
(last_key, max_val) = (None, -sys.maxint)
for line in sys.stdin:
    (key, val) = line.strip().split('\t')
    if last_key and last_key != key:
        print "%s\t%s" % (last_key, max_val)
        (last_key, max_val) = (key, int(val))
    else:
        (last_key, max_val) = (key, max(max_val, int(val)))
if last_key:
    print "%s\t%s" % (last_key, max_val)
```

```bash
# 像 ruby 程序一样测试 python 程序
$ cat input/ncdc/sample.txt | \
ch02-mr-intro/src/main/python/max_temperature_map.py | \
sort | ch02-mr-intro/src/main/python/max_temperature_reduce.py
```

# 四、HDFS

​ 当数据集的大小超过一台独立物理机的存储能力时，就需要对它分区存储到若干台单独的计算机上。管理网络中跨计算机存储的文件系统称为分布式文件系统（distributed filesystem）。

## HDFS 的设计

- 超大文件：指具有几百 MB、几百 GB、几百 TB 大小的文件。
- 流式数据访问：一次写入、多次读取是最高效的访问模式。数据集通常由数据源生成或复制而来，接着长时间在此数据集进行各种分析。读取整个数据集的时间延迟比读取第一条记录的时间延迟更重要。
- 商用硬件：不需昂贵的高可靠硬件，商用硬件指各种零售店可买到的普通硬件。HDFS 遇到节点故障时仍可继续运行且不让用户察觉明显中断。也存在不适合 HDFS 的应用。
- 低时间延迟的数据访问：要求低时间延迟（几十毫秒以内）的应用不适合 HDFS 上运行。HDFS 为高数据吞吐量应用优化，可能以提高时间延迟为代价。目前的较佳方案是 HBase。
- 大量的小文件：文件系统的元数据由 namenode 存储在内存中，而每个文件、目录和数据块的存储信息大约 150 字节，当文件数过大，元数据大小会超出 namenode 内存容量。
- 多用户写入，任意修改文件：HDFS 中的文件只支持单个写入者，写操作只能是在文件末尾“添加”数据。不支持多个写入者，不支持任意位置修改。

## HDFS 的概念

### 1. 数据块

​ 数据块是磁盘进行数据读写的最小单位。文件系统通过磁盘块来管理该文件系统中的块，文件系统 的块是磁盘块的整数倍。磁盘块一般为 512 bytes，文件系统块一般为数千 bytes。

​ HDFS 的块（block）比较大，默认是 128 MB，方便最小化寻址开销。文件被划分为块大小的多个分块（chunk）作为独立的存储单元。与单一磁盘的文件系统不同的是，HDFS 中小于块大小的文件不会占整个块的空间，只占用它实际的大小。

​ 分块的好处

- 一、可以将超出磁盘容量的文件分块存储到集群的任意磁盘中去；
- 二、使用块抽象存储单元，而非整个文件，有利于简化存储子系统的设计，如简化存储管理，撇开元数据信息等
- 三、块适用于数据备份操作，以块为单位对已损或丢失的块数据做复本还原。

### 2. namenode 和 datanode

​ HDFS 以管理节点-工作节点模式运行，即一个 namenode（管理节点）和多个 datanode（工作节点）。

​ namenode 管理文件系统的命名空间，维护文件系统树及整棵树内所有的文件和目录。这些信息以两个文件形式永久保存在本地磁盘：命名空间镜像文件（fsimage）和编辑日志文件（edits）。namenode 还记录每个文件所在块的节点信息，但不会永久保存，而是在系统启动时根据数据节点信息重建。namenode 的毁坏会导致 datanode 的块无法重建文件，所有文件将会丢失。

​ datanode 文件系统的工作节点，根据需要（客户端或 namenode 调度）存储和索引数据块，并定期向 namenode 发送他们所存储块的列表。

​ 客户端（client）提供一个类似 POSIX（可移植操作系统界面）的文件系统接口，通过与 namenode 和 datanode 交互来访问整个文件系统。

​ Hadoop 对 namenode 容错提供了 两种机制：

- 一、将组成文件系统元数据持久状态的文件同步到一个远程挂载的网络文件系统（NFS），备份的写操作需是实时同步且具原子性的。

- 二、在另一台单独的物理机上运行一个辅助 namenode，定期合并 edits 和 fsimage（这占用大量 CPU 时间和与 namenode 相同的内存空间）。在 namenode 故障时辅助 namenode 会启动。由于同步的滞后性，主节点全部失效时，会丢失部分数据，此时可以将 NFS 上的 namenode 元数据复制到辅助 namenode。（也可以运行热备份 namenode 以替。）

### 3. 块缓存

​ datanode 中被频繁访问的文件，会被显式缓存在 datanode 的内存，以堆外块缓存（off-heap block cache）的形式存在。作业调度器（MapReduce、Spark 等）通过在缓存块的 datanode 上运行任务，可以提高读操作的性能。（eg：join 操作中左表就是块缓存的存在，小的查询表会是一个很好的候选。）

​ 缓存池（cache pool）是一个用于管理缓存权限和资源使用的管理性分组。应用通过在 cache pool 中添加 cache directive 来告诉 namenode 需缓存哪些文件及存多久。

### 4. 联邦 HDFS

​ namenode 的内存保存着文件系统中每个文件和每个数据块的引用关系，这意味着对于一个超大集群，内存将限制文件系统的横向扩展。在 2.x 版本系列引入了联邦 HDFS 运行系统添加 namenode 实现扩展。每个 namenode 管理文件系统命名空间的一部分，如一个管理 /user 目录，一个管理 /share 目录。

​ 每个 namenode 维护一个命名空间卷（namespace volume），其中包含命名空间的元数据和一个数据块池（block pool），数据块池包含该命名空间下文件的所有数据块。namespace volume 之间是相互独立互不通信互不影响的。集群中 datanode 需要注册到每个 namenode ，并存储这来自多个数据块池的数据块。（namespace volume 与 datanode 是交叉存在的，这样使得 namenode 管理的元数据量可以切分，同时保证对 datanode 的控制是均衡的。）

​ 访问联邦 HDFS 集群，需挂载数据表将文件路径映射到 namenode 。通过 ViewFileSystem 和 viewfs: //URI 进行配置和管理。

### 5. HDFS 的高可用性

​ namenode 是唯一存储元数据和文件到数据块映射的地方，如果 namenode 失效，所有客户端和作业都无法读写或列举文件。联合使用多个文件系统的 namenode 和通过备用 namenode 创建检测点能防止数据丢失，无法提供新的 namenode 上线，无法实现文件系统的高可用性。

- 冷启动新的 namenode 需满足一下条件才能响应服务（这个过程可能需要 30 分钟以上）

  - 将命名空间的映像导入内存
  - 重演 edits 编辑日志
  - 接收到足够多的来自 datanode 的数据块报告并退出安全模式

- HDFS HA 支持下的 active-standby namenode 模式（切换过程不会有明显中断）：

  - namenode 之间通过高可用共享存储实现 edits 的共享。standby 接管工作后，会通读 edits 直至末尾，以实现 namenode 状态同步，并继续读取由 active 写入的新条目。
  - datanode 需同时向两个 namenode 发送数据块处理报告，因为数据块的映射信息需要存储在 namenode 的内存而非磁盘。
  - 客户端需要特定机制处理 namenode 的失效问题。
  - standby namenode 角色包含了 辅助 namenode 功能（设置周期性检查点）。

- 两种高可用共享存储：

  - NFS 过滤器
  - QJM 群体日志管理器（quorum journalmanager），每一次编辑日志会写入多数日志节点（journal node），系统能够忍受其中任意一个的丢失。类似 Zookeeper，但并没有使用 Zookeeper。（HDFS HA 在选取活动的 namenode 时使用了 Zookeeper 技术。）

​ 在 active 和 standby 都失效的情况下，管理员可以声明一个备用 namenode 并实行冷启动（相当于 non-HA），这是一个标准的处理过程。

- 故障切换

  - 故障转移控制器（failover controller），默认使用 Zookeeper 的 DFSZKFailoverController，管理将 active namenode 转移为 standby namenode 的过程。每个 namenode 运行一个轻量级 FC 监控宿主 namenode 是否失效，并在确认失效时进行故障切换。
  - 平稳故障转移（graceful failover），管理员在日常维护时用故障转移器组织两个 namenode 有序切换角色，手动故障转移。

- 规避（fencing）
  - 非平稳故障转移时，可能无法确认失效的 namenode 是否已经停止运行（如网络原因造成的故障转移，失效的 namenode 还是活动的），为确保失效的 namenode 不执行危害系统的操作，应做进一步“规避”优化。
  - QJM 仅允许一个 namenode 想 edits 写入数据，而先前 active 可能仍有响应客户端过时的读请求，此时 SSH 规避命令用于杀死该 namenode。NFS 无法实现单写入的控制，通常通过撤销 namenode 访问权限，远程管理命令屏蔽相应接口，甚至通过特定供电单元对相应主机进行断电操作（“一枪爆头” STONITH，shoot the other node in the head）等来实现规避。

​ 客户端的故障转移通过客户端类库实现透明处理。通常通过客户端配置文件实现控制。HDFS URI 使用一个逻辑主机名映射一对 namenode 地址，客户端类库会访问每个 namenode 地址。

## 命令行接口

​ 单机模式的两个配置：

- fs.defaultFS 设置为 hdfs://localhost/ 用于设置 Hadoop 的默认文件系统为 HDFS。HDFS 的守护进程会通过该属性项确定 HDFS namenode 的主机及端口（默认 8020）
- dfs.replication 设置为 1（默认为 3），在单 datanode 上运行时无法复制块到 3 个 datanode 上，会提示块复本不足的警告，设置为 1 可以避免该问题。

### 1. 文件系统的基本操作

```bash
# 单机模式

# 从本地文件系统将一个文件复制到 HDFS
# 调用 hadoop 文件系统的 shell 命令 fs 的子命令 -copyFromLocal
$ hadoop fs -copyFromLocal input/docs/quangle.txt \ hdfs://localhost/user/tom/quangle.txt
# 默认主机的 URI 可以省略，简化为：
$ hadoop fs -copyFromLocal input/docs/quangle.txt /user/tom/quangle.txt
# 使用相对路径，复制到 HDFS 的 home 目录中：
$ hadoop fs -copyFromLocal input/docs/quangle.txt quangle.txt
# 把文件复制回本地文件系统，并检查一致性：
$ hadoop fs -copyToLocal quangle.txt input/docs/quangle.copy.txt
$ md5 input/docs/quangle.txt input/docs/quangle.copy.txt
# 可验证结构相同

# 在 HDFS 下创建目录，查看文件列表
$ hadoop fs -mkdir books
$ hadoop fs -ls .
```

​ 默认情况下 Hadoop 运行的安全措施处于停用模式，客户端身份是没有经过认证的，启用权限控制参见 dfs.permissions.enabled 属性。namenode 进程是一个超级用户（super-user），系统不会执行任何权限检查。

## Hadoop 文件系统

​ Hadoop 文件系统是一个抽象概念，HDFS 只是其中一个实现。org.apache.headoop.fs.FileSystem 定义了其客户端接口，以下是其几个具体实现：

![hadoop-fs-01](.\images\03\hadoop-fs-01.jpg)

![hadoop-fs-02](.\images\03\hadoop-fs-02.jpg)

```bash
# 访问文件系统的命令示例
# 访问本地文件系统的根目录
$ hadoop fs -ls file:///
```

### 1. 接口

- HTTP 接口，由 WebHDFS 协议提供的 HTTP REST API，扩展了 HDFS Java API 的语言限制，不过 HTTP 接口比原生 Java 客户端要慢，所以特大数据的传输选择 Java 接口更合适
  - 直接访问，HDFS 守护进程直接服务于客户端的 HTTP 请求。
  - 代理访问，客户端使用 DistributedFileSystem API 访问 HDFS

![hdfs-http](.\images\03\hdfs-http.jpg)

​ HttpFS 代理提供和 WebHDFS 相同的 HTTP/HTTPS 接口，这样客户端可以通过 webhdfs/swebhdfs URI 访问这两类接口。（使用 httpfs.sh 启动，默认端口 14000。）

- C 语言库(libhdfs)，是 Java FileSystem 接口类的一个镜像，他使用 Java 原生接口（JNI，Java Native Interface）调用 Java 文件系统客户端。（还有一个 libwebhdfs 库，使用了 WebHDFS 接口。）
- NFS，使用 NFSv3 网关将 HDFS 挂载为本地客户端的文件系统，然后直接使用 Unix 程序（ls/cat 等）与该文件系统交互。
- FUSE，用户控件文件系统（FUSE，Filesystem in Userspace）。允许将用户控件实现的文件系统作为 Unix 文件系统进行集成，使用 Fuse-DFS 功能模块，将 HDFS（或其他 Hadoop 文件系统）作为一个标准的本地文件系统进行挂载。Fuse-DFS 使用了 libhdfs 访问 HDFS 的接口，在写操作的健壮性不如 NFS 的挂载方案。

## Java 接口

### 1. 从 Hadoop URL 读取数据

```java
// 实现以标准方式显示 Hadoop 文件系统的文件，类似 Unix 的 cat 命令
public class URLCat{
    static{
        // java.net.URL 的实例 URL 调用 setURLStreamHandlerFactory() 方法设置 hdfs URL
        // 每个 Java 虚拟机只能调用一次该方法，若其他组件（如第三方）已经声明，可能无法通过该方法读取到数据
        URL.setURLStreamHandlerFactory(new FsUrlStreamHandlerFactory());
    }

    public static void main(String[] args) throws Exception{
        InputStream in = null;
		try{
            // 使用 java.net.URL 对象打开数据流，从中读取数据
    		// in = new URL("hdfs://host/path").openStream();
            in = new URL(args[0]).openStream();
            // 4096 是 copy 的缓冲区大小，false 是 copy 结束后是否关闭数据流
    		IOUtils.copyBytes(in, System.out, 4096, false);
		} finally{
    		IOUtils.closeStream(in);
		}
    }
}
```

```bash
# 运行示例
$ export HADOOP_CLASSPATH=hadoop-examples.jar
$ hadoop URLCat hdfs://localhost/user/tom/quangle.txt
```

### 2. FileSystem API 读取数据

​ 当无法在应用中设置 URLStreamHandlerFactory 实例，就需要用 FileSystem API 来打开一个文件的输入流。

​ 获取 FileSystem 实例的几个静态工厂方法：

```java
// Configuration 对象用于封装客户端或服务端的配置
// 返回默认文件系统
public static FileSystem get(Configuration conf) throws IOException
// 通过 URI 方案和权限来确定要使用的文件系统
public static FileSystem get(URI uri, Configuration conf) throws IOException
// 给定用户来访问文件系统，更安全
public static FileSystem get(URI uri, Configuration conf, String user) throws IOException
// 获取本地文件系统运行实例的便捷方式
public static LocalFileSystem getLocal(Configuration conf) throws IOException
```

```java
// FileSystem 实例的 open 函数可以打开文件的输入流
// 返回的 FSDataInputStream 实例提供了可以指定偏移读取文件的 read 方法，这些方法是线程安全的
// 默认缓冲区大小 4KB
public FSDataInputStream open(Path f) throws IOException
public abstract FSDataInputStream open(Path f, int bufferSize) throws IOException
```

```java
// 使用 FileSystem 实现标准输出格式文件显示
public class FileSystemCat{
    public static void main(String[] args) throws Exception{
        String uri = args[0];
        Configuration conf = new Configuration();
        // 获取文件系统实例
        FileSystem fs = FileSystem.get(URI.create(uri), conf);
        InputStream in = null;
        try{
            // 打开文件输入流
            in = fs.open(new Path(uri));
            IOUtils.copyBytes(in, System.out, 4096, false);
            // go back to the start of the file
            // seek 方法的开销较大，建议用流数据构建应用的访问模型（比如 MapReduce）
            in.seek(0);
            IOUtils.copyBytes(in, System.out, 4096, false);
        } finally{
            IOUtils.closeStream(in);
        }
    }
}
```

```bash
# 运行程序
$ hadoop FileSystemCat hdfs://localhost/user/tom/quangle.txt
```

### 3. 写入数据

```java
// FileSystem 类用于创建写数据（输出流）的方法，exists() 可以检查目录是否存在
// 与 FSDataInputStream 类似，FSDataOutputStream 实例也有 getPos() 方法，可以查询当前文件位置，但它不支持文件中定位，因为 HDFS 只允许文件的顺序写入或末尾追加。
public FSDataOutputStream create(Path f) throws IOException
// 追加操作，HDFS 支持， S3 不支持
public FSDataOutputStream append(Path f) throws IOException
```

```java
// 将本地文件复制到 Hadoop 文件系统，并显示进度
public class FileCopyWithProgress{
    public static void main(String[] args) throws Exception{
        String localStr = args[0];
        String dst = args[1];
        InputStream in = new BufferedInputStream(new FileInputStream(localStr));

        Configuration conf = new Configuration();
        FileSystem fs = FileSystem.get(URI.create(dst), conf);
        OutputStream OUT = fs.create(new Paht(dst), ne Progressable(){
            public void progress(){
                System.out.print(".");
            }
        });

        IOUtils.copyBytes(in, out, 4096, true);
    }
}
```

```bash
# 运行
$ hadoop FileCopyWithProgress input/docs/1400-8.txt hdfs://localhost/user/tom/1400-8.txt
```

### 4. 目录

```java
// 用于创建所有必要但还没有的父目录
// 通常需要显示创建一个目录，而 create() 方法写入文件时是会自动创建父目录的
public boolen mkdirs(Path f) throws IOException
```

### 5. 查询文件系统

#### 1. 文件元数据(FileStatus)

​ FileStatus 类封装了文件系统中文件和目录的元数据，包括文件长度，块大小，复本，修改时间，所有者及其权限信息。

```java
public class ShowFileStatusTest{
    // an in-process HDFS cluster for testing
    private MiniDFSCluster cluster;
    private FileSystem fs;

    @Before
    public void setUp() throws IOException{
        Configuration conf = new Configuration();
        if (System.getProperty("test.build.data") == null){
            System.setProperty("test.build.data", "/tmp");
        }
        cluster = new MiniDFSCluster.Builder(conf).build();
        fs = cluster.getFileSystem();
        OutputStream out = fs.create(new Path("/dir/file"));
        out.write("content".getBytes("UTF-8"));
        out.close();
    }

    @After
    public void tearDown() throws IOException{
        if (fs != null) { fs.close(); }
        if (cluster != null) { cluster.shutdown(); }
    }

    @Test(expected = FileNotFoundException.class)
    public void throwsFileNotFoundForNonExistentFile() throws IOException{
        fs.getFileStatus(new Path("no-such-file"));
    }

    @Test
    public void fileStatusForFile() throws IOException{
        Path file = new Path("/dir/file");
        FileStatus stat = fs.getFileStatus(file);
        assertThat(stat.getPath().toUri().getPath(), is("/dir/file"));
        assertThat(stat.isDirectory(), is(false));
        assertThat(stat.getLen(), is(7L));
        assertThat(stat.getModificationTime(), is(lessThanOrEqualTo(System.currentTimeMillis())));
        assertThat(stat.getReplication(), is((short)1));
        assertThat(stat.getBlockSize(), is(128 * 1024 * 1024L));
        assertThat(stat.getOwner(), is(System.getProperty("user.name")));
        assertThat(stat.getGroup(), is("supergroup"));
        assertThat(stat.getPermission().toString(), is("rw-r--r--"));
    }

    @Test
    public void fileStatusForDirectory() throws IOException{
        Path dir = new Path("/dir");
        FileStatus stat = fs.getFileStatus(dir);
        assertThat(stat.getPath().toUri().getPath(), is("/dir"));
        assertThat(stat.isDirectory(), is(true));
        assertThat(stat.getLen(), is(0L));
        assertThat(stat.getModificationTime(), is(lessThanOrEqualTo(System.currentTimeMillis())));
        assertThat(stat.getReplication(), is((short)0));
        assertThat(stat.getBlockSize(), is(0L));
        assertThat(stat.getOwner(), is(System.getProperty("user.name")));
        assertThat(stat.getGroup(), is("supergroup"));
        assertThat(stat.getPermission().toString(), is("rwxr-xr-x"));
    }
}
```

```java
// FileSystem 用于判断文件或目录存在的方法
public boolen exists(Path f) throws IOException
```

#### 2. 列出文件(listStatus)

```java
public FileStatus[] listStatus(Path f) throws IOException
public FileStatus[] listStatus(Path f, PathFilter filter) throws IOException
public FileStatus[] listStatus(Path[] files) throws IOException
public FileStatus[] listStatus(Path[] files, PathFilter filter) throws IOException
```

```java
// stat2Paths() 方法可以将一个 FileStatus 对象数组转换成一个 Path 对象数组
Path[] listedPaths = FileUtil.stat2Paths(status);
```

#### 3. 文件模式"通配"

```java
public FileStatus[] globStatus(Path pathPattern) throws IOException
public FileStatus[] globStatus(Path pathPattern, PathFilter filter) throws IOException
```

![path-pattern](.\images\03\path-pattern.jpg)

![file-pattern-extend](.\images\03\file-pattern-extend.jpg)

#### 4. PathFilter 对象

```java
public class RegexExcludePathFilter implements PathFilter{
    private final String regex;

    public RegexExcludePathFilter(String regex){
        this.regex = regex;
    }

    public boolean accept(Path path){
        return !path.toString().matches(regex);
    }
}
```

```java
fs.globStatus(new Path("/2007/*/*"), new RegexExcludePathFilter("^.*/2007/12/31$"));
```

### 6. 删除数据

```java
// 永久删除文件或目录
// 只有 recrusive 为 true 时，非空目录及其内容才会被删除，否则抛异常
public boolean delete(Path f, boolean recursive) throws IOException
```

## 数据流

### 1. 剖析文件读取

客户端及与之交互的 HDFS、namenode、datanode 之间的数据流：

- 一、客户端通过 FileSystem 对象的 open() 打开希望读取的文件（对于 HDFS 来说，就是 DistributedFileSystem 的一个实例）。
- 二、DistributedFileSystem 通过 RPC 调用 namenode，以确认文件起始块位置，namenode 返回每个块复本所在 datanode 的地址，datanode 将根据它与客户端的距离（集群的网络拓扑）排序，DistributedFileSystem 返回一个支持文件定位的输入流 FSDataInputStream 对象给客户端，FSDataInputStream 封装了 DFSInputStream 对象，用于管理 datanode 和 namenode 的 I/O。
- 三、客户端对这个输入流（FSDataInputStream ）调用 read() 方法。
- 四、存储着文件起始几个块的 datanode 的 DFSInputStream 随即连接最近的文件中第一个块所在的 datanode，通过对数据流的反复 read()，将数据从 datanode 传输给客户端。
- 五、达到块末端是，DFSInputStream 关闭与该 datanode 的连接，然后寻找下一块的最佳 datanode，在客户端看来，整个输入流是一个连续的流。客户端读取数据的顺序是 DFSInputStream 连接 datanode 的顺序，其间会根据需要访问 namenode 检索下一批数据块的 datanode 位置。
- 六、客户端读取数据完成，FSDataInputStream 调用 close()。

![client-read](.\images\03\client-read.jpg)

​ 当 DFSInputStream 在与 datanode 通信失败，或读取到损坏的块时，会尝试从这个快的另一个最邻近 datanode 读取数据，并向 namenode 汇报已损块位置，记住故障 datanode，以保证不会反复读取节点上后续的块。

​ client node 可以直接连接 datanode 检索数据，namenode 告知客户端每个块的最佳 datanode。这有利于使 HDFS 扩展到大量并发客户端。namenode 只需要响应块位置的请求，无需响应数据请求。

![network-distance](.\images\03\network-distance.jpg)

### 2. 剖析文件写入

​ 新建一个文件，把数据写入该文件，最后关闭该文件：

- 一、客户端通过 DistributedFileSystem 对象调用 create() 新建一个文件。
- 二、DistributedFileSystem 对 namenode 创建一个 RPC 调用，在文件系统的命名空间新建一个文件。namenode 负责检查文件不存在，以及客户端新建该文件的权限。DistributedFileSystem 向客户端返回一个 FSDataOutputStream 对象，FSDataOutputStream 封装了一个 DFSOutputStream 对象，该对象负责 datanode 和 namenode 之间的通信。
- 三、客户端写入数据，DFSOutputStream 将数据分成一个个数据包写入内部队列（data queue）。
- 四、DataStreamer 负责挑选出适合存储数据复本的一组 datanode，并据此要求 namenode 分配新的数据块，这一组 datanode 构成一个管线（Pipeline of datanodes）。DataStreamer 将数据包流式传输到管线的第 1 个 datanode，该 datanode 存储数据并将数据发送给他的下游 datanode，下游 datanode 再发送给其下游（知道存储足够份数的复本）。
- 五、DFSOutputStream 维护一个 data queue 来等待 datanode 的确认收到回执（确认队列-ack queue），收到管道中所有 datanode 的确认信息后，删除该数据包。
- 六、客户端在完成数据的写入后，对数据流（FSDataOutputStream ）调用 close()。
- 七、close() 操作将所有剩余数据包写入 datanode 管线，并告知 namenode 等待文件写入完成的确认。namenode 知道文件的组成块，所有只需要等待数据块最小量复制的完成。

![client-write](.\images\03\client-write.jpg)

​ 任何 datanode 在数据写入其间故障，首先关闭管线，并将所有数据包添加回数据队列的最前端，为正常 datanode 中已存储的数据块指定一个标识，并告知 namenode 以便故障 datanode 恢复后删除这些数据块。从管线删除故障 datanode，并基于正常 datanode 构建新管线。余下的数据块写入新的管线。namenode 发现块复本量不足时，会在另一个节点构建新的复本。

​ Hadoop 默认数据布局策略：第 1 个复本方客户端所在节点，若客户端在集群之外，则随机选择；第 2 个复本离架（与第一个不同机架的随机机架中的节点）存储；第 3 个复本在第 2 个复本同机架的随机节点上；其他复本在集群上随机选择。

![copys-select](.\images\03\copys-select.jpg)

​ 数据布局策略需同时考虑：稳定性，负载均衡，带宽资源，读取性能，块的均匀分布等。

### 3. 一致模型(coherency model)

​ HDFS 的性能牺牲了一些 POSIX 要求，如写入文件的内容并不保证立即可见。

​ FSDataOutputStream 的 flush() 可以强制将所有缓存刷新到 datanode 的内存，fsync() 可以保证数据写入磁盘。

```java
Path p = new Path("p");
FSDataOutputStream out = fs.craete(p);
out.write("content".getBytes("UTF-8"));
out.hflush();
assertThat(fs.getFileStatus(p).getLen(), is((long)"content".length()));
```

```java
FileOutputStream out = new FileOutputStream(localFile);
out.write("content".getBytes("UTF-8"));
out.flush(); // flush to operating system
out.getFD().sync(); // sync to disk
assertThat(localFile.length(), is((long)"content".length()));
```

​ 如果不调用 hflush() 或 hsync() 方法，就可能在客户端或系统发生故障时丢失数据。

## distcp 并行复制

```bash
# 将文件复制到另一个文件中
$ hadoop distcp file1 file2
# 目录复制 此例结果是：dir2/dir1， 使用 -overwrite 可以保持同样目录结构并强制覆盖原有文件
$ hadoop distcp dir1 dir2
# 仅更新变化的文件
$ hadoop distcp -update dir1 dir2
# 两个 HDFS 集群间的数据传输
# -delete 删除目标路径中任意没有在源路径出现的文件和目录
# -p 保留文件状态属性如权限、块大小、复本数
$ hadoop distcp -update -delete -p hdfs://namenode1/foo hdfs://namenode2/foo
# 使用 webhdfs 协议，避免两个不兼容的 HDFS 版本的传输异常。还可以是用 HttpFs 代理（权限控制更佳）
$ hadoop distcp webhdfs://namenode1:50070/foo webhdfs://namenode2:50070/foo
```

​ distcp 实际使用 MapReduce 作业实现，每个文件通过一个 map 进行复制，没有 reducer，distcp 将文件划分成大致相等的块，每个节点默认启动 20 个 map，可以通过 -m 修改 map 数目。如果指定 -m 为 1，每个块的第一个复本将会存储到运行 map 的结点上，直至磁盘被填满，之后会分散在集群中。

​ distcp 与 insert overwrite(hive) 在应用中的不同在于，insert overwrite 会重组元数据，而 distcp 只是单纯拷贝。

# 五、YARN

​ YARN 提供了请求和使用集群资源的 API。一些分布式计算框架（MapReduce，Spark 等）作为 YARN 应用运行在集群计算层（YARN）和集群存储层（HDFS 和 HBase）上。还有更高一层的应用，如 Pig，Hive，Crunch 等运行在 MapReduce、Spark 或 Tez 之上。

![yarn](.\images\04\yarn.jpg)

## 剖析 YARN 应用运行机制

![yarn-application](.\images\04\yarn-application.jpg)

- 一、客户端请求运行一个 application master 进程。
- 二、ResourceManager 找到一个能在容器中启动 application master 的 NodeManager。
- 三、application master 依赖应用本身运行一个计算，或是向 ResourceManager 请求更多的容器。
- 四、运行一个分布式计算（MapReduce YARN）。

### 1. 资源请求

​ YARN 有一个灵活的资源请求模型。当请求多个容器时，可以指定每个容器需要的计算机资源（内存和 CPU），还可以指定对容器的本地限制要求。

​ 本地限制要求用于申请位于指定节点或机架，或集群任意位置（机架外）的容器，本地化有利于确保分布式数据处理算法高效实用集群带宽。

​ 通常启动一个容器处理 HDFS 数据块时，应用将先向数据块复本所在节点或所在机架的一个节点申请容器，若失败，则想集群中任意节点申请。

​ Spark 在集群上启动固定数量的执行器。MapReduce 则分两步，在最开始时申请 map 任务容器，reduce 任务容器放在后期。任何任务失败，将会另外申请容器以重新运行失败的任务。

### 2. 应用生命期

- 一个用户作业对应一个应用(MapReduce)
- 作业的每个工作流或每个用户对话对应一个应用(Spark)，容器可以在作业之间重用，缓冲作业间数据，效率更高。
- 多个用户共享一个长期运行的应用。这通常是一种协调者，如 Apache Slider 就是用于启动集群的其他应用。一个总是开启的 application master 意味着用户将获得非常低延迟的查询响应。

### 3. 构建 YARN 应用

​ 现成的 YARN 应用：Spark 或 Tez 用于运行一个作业的邮箱无环图；Spark、Samza 或 Storm 用于流处理。

​ Apache Slider 简化了构建 YARN 应用的过程，它提供了应用运行的相关控制（暂停、恢复、版本、数量等）。

​ Apache Twill 与 Slider 类似，且额外提供了简单的编程模型，用于开发 YARN 上分布式应用。

​ YARN 自身还有 distributed shell 应用，演示了如何使用 YARN 客户端 API 处理客户端或 application master 与 YARN 守护进程间的通信。

## YARN 与 MR 1 相比

![YARN-MR1](.\images\04\YARN-MR1.jpg)

- 可扩展性(Scalability)

  ​ MR 1 受限 jobtracker 必须同时管理作业和任务，可扩展性瓶颈在 4000 结点和 40000 任务；而 YARN 分离了 ResourceManager 和 application master，可扩展到将近 10000 节点和 100000 任务。

  ​ 每个应用的实例（MR Job）都对应了一个专门的 application master，该管理进程协调运行一系列工作（worker）上的 map 和 reduce 任务。

- 可用性(Availability)

  ​ 服务的守护进程失败时，启动另一个守护进程复制接管工作的状态以继续提供服务，成为服务的高可用。jobtracker 内存中存在大量快速变化的复杂状态，服务的高可用维护非常困难。在 YARN 中 jobtracker 的职责分为 ResourceManager 和 application master，分而治之为两者提供高可用的服务，使得 YARN 中的失败恢复更加容易。

- 利用率(Utilization)

  ​ MR 1 中，每个 tasktracker 会静态分配若干固定长度的 slot，并划分为 map slot 和 reduce slot，互不可替。这导致请求的资源不可分割，特定任务可能太大或太小而失败。而 YARN 中，一个 NodeManager 管理一个资源池，能精细化管理资源，按需求情资源。

- 多租户(Multitenancy)

  ​ YARN 最大的优点是向 MR 以为的其他类型分布式应用开放了 Hadoop。

## YARN 中的调度

​ 通常资源有限，在一个繁忙的集群上，一个应用经常需要等待才能得到请求的资源，YARN 调度器提供了分配资源的策略调度。

### 1. 调度选项

![3-schedulers](.\images\04\3-schedulers.jpg)

- FIFO Scheduler(FIFO 调度器)

  ​ 将应用放置在一个队列中，先满足队首应用的资源请求，之后才依次分配其他应用的资源，简单无需配置。但不适合共享集群，会造成作业阻塞。

- Capacity Scheduler(容量调度器)

  ​ 保留一个专门队列，保证小作业提交后能立即启动，降低了整个集群的 利用率。

- Fair Scheduler(公平调度器)

  ​ 不需预留资源，第一个作业启动时，享有集群的所有资源，第二个作业启动后，会被分配集群一半的资源，一个作业完成后，剩下的作业再次享有全部资源。注意第二个作业获取资源有一定时间延迟，因为必须等待第一个作业使用的容器用完并释放。

### 2. Capacity Scheduler 配置

​ CS 运行多个组织共享一个 Hadoop 集群，每个组织分配全部集群资源的一部分，每个组织被配置一个专门的队列，每个队列使用一定的集群资源。队列资源不够用，而集群仍有空闲资源时（不会强行终止来抢占容器），可能会将空闲资源分配给队列中的作业，以致超出队列容量（弹性对了 queue elasticity）。可以为队列设置一个最大容量限制，这样队列就不会过多侵占其他队列的容量。

​ 应用放置在哪个队列取决于应用本身， MR 中，可以设置 mapreduce.job.queuename，不指定队列，则被放在名为 “default” 的默认队列中。

### 3. Fair Scheduler 配置

![fair-scheduler](.\images\04\fair-scheduler.jpg)

​ 如上图，A 和 B 用户分别拥有自己的队列，A 启动第一个 Job 占用全部资源，B 启动第二个 Job 后，慢慢与 A 平分资源，这时 B 启动第三个 Job，Job 2 和 Job 3 将平分 B 队列的一半资源。最终结果是资源在用户之间实现公平共享。

- 启动 FS

  ​ 将 yarn-site.xml 中的 yarn.resourcemanager.scheduler.class 设置为：org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.FairScheduler。

- 队列配置

  ​ 配置 fair-scheduler.xml（位于类路径下，可以通过设置 yarn.scheduler.fair.allocation.file 修改文件名）

- 队列放置

  ​ 通过 queuePlacementPolicy 元素指定定义队列，否则必要时会以用户名为队列名创建队列。或者将所有用户放入一个 default 队列，这样就是应用之间的公平共享，而非用户间的共享。

  ​ 设置 yarn.scheduler.fair.user-as-default-queue 为 false 应用就会被放入 default 队列，yarn.scheduler.fair.user-as-default-queue 为 false 可以禁止用户创建队列。

- 抢占

  ​ 允许调度器终止哪些占用资源超过了其公平共享份额的队列的容器，这些容器资源释放后会分配给资源数量低于应得份额的队列。被终止的容器需要重新执行，因此会降低集群的效率。

  ​ yarn.scheduler.fair.preemption 设置为 true 全面启用抢占。

### 4. 延迟调度

​ 在 YARN 调度器试图请求本地容器而不得，显而易见的处理是在同机架分配容器，然而通常，此时等待一小段时间可以增加在本地请求到容器的机会，从而提高集群的效率，这个特性称为延迟调度（CS 和 FS 都支持）。

​ 调度器不会简单的使用第一个调度机会（NodeManager 向 ResourceManager 发送的心跳，汇报正在运行的容器、新容器可用资源等信息），而是可以通过配置设置最大容忍。

​ yarn.scheduler.capacity.node-locality-delay 配置可以错过的调度机会数量（正整数）。

​ yarn.scheduler.fair.locality.threshold.node 设置集群中给过调度机会的结点的占比（0-1 的小数）。

​ yarn.scheduler.fair.locality.threshold.rack 设置接受另一机架前所需等待的时间。

### 5. 主导资源公平性

​ 当多种资源同时需要调度，YARN 中调度器会观察每个用户的主导资源，并将之作为对集群资源使用的一个度量，这种方法称为“主导资源公平性”（Dominant Resource Fairness, DRF）。

​ 默认情况不使用 DRF，一次只需要考虑内存，不考虑 CPU。

## 延伸

​ 《Apache Hadoop YARN》 - Arun C. Murthy （http://yarn-book.com/）

# 六、Hadoop 的 I/O 操作

​ Hadoop 自带一套原子操作用于数据 I/O 操作。

## 数据完整性

​ 检测数据是否损坏的常用措施是在数据第一次引入系统时计算校验和（checksum），并在数据通过一个不可靠通道进行传输时再次计算校验和。

### 1. HDFS 的数据完整性

​ datanode 在收到数据后存储数据及其校验和之前，对数据进行校验。客户端从 datanode 读取数据时，也会验证校验和，将他们与 datanode 中的校验和进行比较。每个 datanode 会在一个后台线程中运行一个 DataBlockScanner，从而定期校验存储在这个 datanode 上的所有数据块。

​ HDFS 可以通过数据副本来修复损坏的数据块，客户端读取数据块时，如果检测到错误，首先向 namenode 报告已损坏数据块以及其正在尝试读取的 datanode ，并抛出 ChecksumException 异常。namenode 将这个数据块复本标记为已损坏，防止再次将客户端处理请求发送到这个节点，或将这个复本复制到他处。之后 namenode 安排这个数据块的一个复本复制到另一个 datanode ，让数据的复本因子（replication factor）回到期望水平。最后删除已损坏数据块复本。

​ 使用 open() 读取数据前，将 false 传给 FileSystem 对象的 setVerifyChecksum() 可以禁用校验和校验。这可以打开一个已损文件。

​ fs -checksum 命令可以检查一个文件的校验和。distcp 命令也具有类似的功能。

### 2. LocalFileSystem

## 压缩

## 序列化

## 基于文件的数据结构

# 七、MapReduce 应用开发

​ MapReduce 编程遵循一个特定流程。首先编写 map 函数和 reduce 函数，并使用单元测试保证函数的运行符合预期。然后写一个程序运行作业，从本地 IDE 用一个小的数据集运行它。可以用本地 IDE 调试器调试。

## 用于配置的 API

## 配置开发环境

## 用 MRUnit 写单元测试

## 本地运行测试数据

## 在集群上运行

## 作业调优

## MapReduce 工作流
