#!/bin/bash

if [ $# -lt 1 ]
then
    echo "No Args Input..."
    exit ;
fi

case $1 in
    "start")
        echo " =================== 启动 hadoop 集群 ==================="
        echo " ------------------- 启动 hdfs -------------------"
        ssh node01 "/home/aurelius/software/hadoop-3.2.2/sbin/start-dfs.sh"
        echo " ------------------- 启动 yarn -------------------"
        ssh node02 "/home/aurelius/software/hadoop-3.2.2/sbin/start-yarn.sh"
        echo " ------------------- 启动 historyserver -------------------"
        ssh node01 "/home/aurelius/software/hadoop-3.2.2/bin/mapred --daemon start historyserver"
    ;;
    "stop")
        echo " =================== 关闭 hadoop 集群 ==================="
        echo " ------------------- 关闭 historyserver -------------------"
        ssh node01 "/home/aurelius/software/hadoop-3.2.2/bin/mapred --daemon stop historyserver"
        echo " ------------------- 关闭 yarn -------------------"
        ssh node02 "/home/aurelius/software/hadoop-3.2.2/sbin/stop-yarn.sh"
        echo " ------------------- 关闭 hdfs -------------------"
        ssh node01 "/home/aurelius/software/hadoop-3.2.2/sbin/stop-dfs.sh"
        
    ;;
    *)
        echo "Input Args Error..."
    ;;
esac