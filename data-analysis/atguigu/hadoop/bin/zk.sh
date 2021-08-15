#!/bin/bash

case $1 in 
"start"){
    for node in node01 node02 node03
    do
        echo ------ zookeeper $node 启动 ------
        ssh $node "/home/aurelius/software/apache-zookeeper-3.7.0-bin/zkServer.sh start"
    done
};;
"stop"){
    for node in node01 node02 node03
    do
        echo ------ zookeeper $node 停止 ------
        ssh $node "/home/aurelius/software/apache-zookeeper-3.7.0-bin/zkServer.sh stop"
    done
};;
"status"){
    for node in node01 node02 node03
    do
        echo ------ zookeeper $node 状态 ------
        ssh $node "/home/aurelius/software/apache-zookeeper-3.7.0-bin/zkServer.sh status"
    done
};;
esac