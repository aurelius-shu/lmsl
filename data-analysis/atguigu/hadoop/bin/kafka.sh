#!/bin/bash

for node in node01 node02 node03
do
    echo "====== $node ======"
    ssh $node '/home/aurelius/software/kafka_2.13-2.7.0/bin/kafka-server-start.sh -daemon /home/aurelius/software/kafka_2.13-2.7.0/config/server.properties'
done