# docker env

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [docker env](#docker-env)
  - [install docker](#install-docker)
  - [run container](#run-container)
    - [mysql](#mysql)
    - [redis](#redis)
    - [nacos](#nacos)

<!-- /code_chunk_output -->

## install docker

```shell
sudo yum install docker-ce-20.10.6 docker-ce-cli-20.10.6 containerd.io
```

## run container

### mysql

```shell
sudo docker run --name mysql -e MYSQL_ROOT_PASSWORD=999999 -d mysql

docker run -it --rm \
    --link mysql:mysql \
    mysql \
    sh -c 'exec mysql -h"$MYSQL_PORT_3306_TCP_ADDR" -P"$MYSQL_PORT_3306_TCP_PORT" -uroot -p"$MYSQL_ENV_MYSQL_ROOT_PASSWORD"'

docker run -d -p 3306:3306 --name mysql -e MYSQL_ROOT_PASSWORD=999999 --restart=always  mysql:5.7
```

### redis

```shell
docker run -d -p 6379:6379 --name redis redis --restart=always
docker update --restart=always redis
```

### nacos

```shell
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
```

### 容器化部署 datahub 步骤

**每次更新部署，需先将容器删除，重新打镜像，用新的镜像启动新的容器**

1. 删除容器

```shell
# 查看容器
docker ps

# 停止容器
docker stop CONTAINER ID(容器对应标识)

#删除容器
docker rm CONTAINER ID(容器对应标识)
```

2. 删除镜像

```shell
# 查看镜像
docker images

# 删除镜像
docker rmi IMAGE ID(镜像对应标识)
```

3. 制作镜像

```shell
# 进入工程目录(首先将需要更新的文件上传到响应目录，替换现有文件)
# /cdp/datahub-ci-core
# /cdp/datahub-server-core
# 在工程根目录下(与 Dockerfile 同级目录)，执行命令：
docker build -t datahub-server-core:1.0.0 .
docker build -t datahub-ci-core:1.0.0 .
```

4. 启动容器

```shell
docker run --privileged=true -idt -p 5000:80 -v /datahub_logs/server:/app/Log --name datahub-server-core datahub-server-core:1.0.0
docker run --privileged=true -idt -p 5001:80 -v /datahub_logs/ci:/app/Log --name datahub-ci-core datahub-ci-core:1.0.0
```
