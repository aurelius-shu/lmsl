


node01:
- jdk
- zk
- kafka
- redis

- NN
- DN
- NM

node02:
- jdk
- zk
- kafka

- DN
- RM
- NM

node03:
- jdk
- zk
- kafka

- SNN
- DN
- NM


hadoop
spark
hive
kafka
------
zookeeper
activemq
flink
flume

jvm
mysql
redis

spring boot
spring cloud
spring cloud alibaba
------
nio/netty



三只鱼:
【中国平安】亲爱的黄超铭：欢迎参加<平安寿险-架构师>招聘测评。同时，为了更好地了解您，请在测评开始前完善及确认您的简历信息。您可点击 http://talent.pingan.com/web/index.html 进入测评中心，链接将在 2021-05-17 17:25到期，请务必按时完成。感谢您的参与！

三只鱼:
【中国平安】亲爱的黄超铭：邀请您参加[平安寿险-架构师]职位的移动视频面试，面试安排为2021-05-13 19:30，请提前下载HR-X APP参与面试，详情请查看邮件。期待与您见面！ 如有任何疑问，请联系：邱先生-188564。

工作职责
1.负责大数据平台工程平台相关后台的技术选型、架构设计、系统编码等。
2.设计后台系统要求具备高稳定性，高性能，扩展性，易维护性，基于微服务架构优化系统平台。
3.负责核心技术问题的研究攻关和重要应用的性能调优。
任职资格
1.本科以上学历， 5年以上工作经验。
2.编程功底扎实，熟悉网络协议栈，数据结构与算法，数据库调优，操作系统原理等。
3.丰富的研发经验，宽广的技术视野。
4.精通java或c++，熟练掌握python。
5.掌握Impala/ClickHouse/ElasticSearch/Kylin一种或多种等，理解其技术要害。
6.熟悉常用分布式框架、缓存技术，具备一定高并发架构设计能力； 
7.对技术有着强烈的兴趣，追求极致的性能优化，善于研究底层技术。
8.具备产品化思维，责任心强，抗压，好学，喜欢钻研新技术，能进行跨团队沟通、协调。 
9.具有自我驱动能力和良好的沟通协作能力。
10.有大型互联网项目高并发经验或业务中台经验者优先。

sc.textFile("data/word.txt").flatMap(_.split(" ")).map((_,1)).reduceByKey(_+_).collect


bin/spark-submit \
--class org.apache.spark.examples.SparkPi \
--master spark://node01:7077 \
./examples/jars/spark-examples_2.12-3.0.2.jar \
10