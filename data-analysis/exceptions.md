

## 20200817
```html
hdfsjps 查看进程有datanode，hdfs 管理界面查看不到 datanode 和可用磁盘空间
hdfs-site.xml 和 core-site.xml 中指向的 data、tmp 路径在各个节点上不一致导致

解决办法：删掉配置文件中指定的 data、tmp 路径，并执行

hdfs namenode -format
最后重新启动 hdfs 和 yarn 即可
```

## 20200821
```html
hive Exception in thread "main" java.lang.NoSuchMethodError: com.google.common.base.Preconditions.checkArgument(ZLjava/lang/String;Ljava/lang/Object;)V
This is like HIVE-22718 and many other similar issues: You have 2 incompatible versions of guava on your classpath. Maybe the Hadoop/Spark version or something else you're using is not compatible with this Hive version.
rm /opt/shared/apache-hive-3.1.2-bin/lib/guava-19.0.jar
cp /opt/shared/hadoop-3.2.1/share/hadoop/hdfs/lib/guava-27.0-jre.jar /opt/shared/apache-hive-3.1.2-bin/lib/
```