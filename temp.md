sudo yum install docker-ce-20.10.6 docker-ce-cli-20.10.6 containerd.io

sudo docker run --name mysql -e MYSQL_ROOT_PASSWORD=999999 -d mysql

docker run -it --rm \
    --link mysql:mysql \
    mysql \
    sh -c 'exec mysql -h"$MYSQL_PORT_3306_TCP_ADDR" -P"$MYSQL_PORT_3306_TCP_PORT" -uroot -p"$MYSQL_ENV_MYSQL_ROOT_PASSWORD"'


docker run -d -p 3306:3306 --name mysql -e MYSQL_ROOT_PASSWORD=999999 --restart=always  mysql:5.7

docker run -d -p 6379:6379 --name redis redis --restart=always
docker update --restart=always redis

docker  run \
    --name nacos -d \
    -p 8848:8848 \
    --privileged=true \
    --restart=always \
    -e JVM_XMS=256m \
    -e JVM_XMX=256m \
    -e MODE=standalone \
    -e PREFER_HOST_MODE=hostname \
    -v /home/aurelius/software/nacos/logs:/home/nacos/logs \
    -v /home/aurelius/software/nacos/init.d/custom.properties:/home/nacos/init.d/custom.properties \
    nacos/nacos-server