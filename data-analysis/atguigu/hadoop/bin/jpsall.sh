#!/bin/bash

for host in node01 node02 node03
do
    echo =============== $host ===============
    ssh $host jps
done