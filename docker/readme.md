# docker

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [docker](#docker)
  - [install](#install)
  - [mysql](#mysql)
  - [redis](#redis)
  - [nacos](#nacos)
  - [datahub-ci-core](#datahub-ci-core)
  - [cloud-galaxy](#cloud-galaxy)
  - [datahub](#datahub)

<!-- /code_chunk_output -->

## install

```shell
sudo yum install docker-ce-20.10.6 docker-ce-cli-20.10.6 containerd.io
```

## mysql

```shell
sudo docker run --name mysql -e MYSQL_ROOT_PASSWORD=999999 -d mysql

docker run -it --rm \
    --link mysql:mysql \
    mysql \
    sh -c 'exec mysql -h"$MYSQL_PORT_3306_TCP_ADDR" -P"$MYSQL_PORT_3306_TCP_PORT" -uroot -p"$MYSQL_ENV_MYSQL_ROOT_PASSWORD"'

docker run -d -p 3306:3306 --name mysql -e MYSQL_ROOT_PASSWORD=999999 --restart=always  mysql:5.7
```

## redis

```shell
docker run -d -p 6379:6379 --name redis redis --restart=always
docker update --restart=always redis
```

## nacos

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

## datahub-ci-core

**build-datahub-ci-core**

```shell
sourcedir=/home/aurelius/software/appraisal
builddir=/home/aurelius/software/datahub-ci-core
tag=1.0.0

# clean old containers and images
function clean_docker_containers__images(){
    if [ $# -lt 1 ]
    then
        echo "no args input..."
        exit;
    else
        cids=$(sudo docker ps | grep $1 | awk '{print $1}')
        for cid in ${cids}
        do
            echo "stop container id" ${cid}
            sudo docker stop ${cid}
            echo "remove container id" ${cid}
            sudo docker rm ${cid}
        done

        iids=$(sudo docker images | grep $1 | awk '{print $3}')
        for iid in ${iids}
        do
            echo "remove image id" ${iid}
            sudo docker rmi ${iid}
        done
    fi
}

cd ${sourcedir}
git pull origin master
sudo rm -rf ${builddir}/wwwroot/appraisal/
sudo cp -r ${sourcedir}/ ${builddir}/wwwroot/appraisal/

clean_docker_containers__images datahub-ci-core

cd ${builddir}
echo "build datahub-ci-core"
sudo docker build -t datahub-ci-core:${tag} .

echo "run datahub-ci-core"
sudo docker run --privileged=true -idt -p 5001:80 -v /home/aurelius/software/logs/datahub-ci-core:/app/Log --name datahub-ci-core datahub-ci-core:${tag}
```

## cloud-galaxy

```Dockerfile
FROM openjdk:8
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' >/etc/timezone
WORKDIR /app
COPY . .
CMD ["java", "-jar", "cloud-galaxy-pos-1.0-SNAPSHOT.jar"]
```

**build cloud-galaxy**

```shell
# build cloud-galaxy

sourcedir=/home/aurelius/software/cloud-galaxy
buildver=${buildvers}
builddir=/home/aurelius/software

cd $sourcedir
echo "pull source code from gitlab"
git pull origin master

echo "build project by maven"
mvn clean package -DskipTests

# cd ${sourcedir}/app/cloud-galaxy-pos
# mvn clean package -DskipTests
# cd ${sourcedir}/app/cloud-galaxy-pos-backend
# mvn clean package -DskipTests
# cd ${sourcedir}/app/cloud-galaxy-job
# mvn clean package -DskipTests
# cd ${sourcedir}/infrastructure/cloud-galaxy-gateway
# mvn clean package -DskipTests

cp ${sourcedir}/app/cloud-galaxy-pos/target/cloud-galaxy-pos-${buildver}.jar ${builddir}/cloud-galaxy-pos/cloud-galaxy-pos-${buildver}.jar
cp ${sourcedir}/app/cloud-galaxy-pos-backend/target/cloud-galaxy-pos-backend-${buildver}.jar ${builddir}/cloud-galaxy-pos-backend/cloud-galaxy-pos-backend-${buildver}.jar
cp ${sourcedir}/app/cloud-galaxy-job/target/cloud-galaxy-job-${buildver}.jar ${builddir}/cloud-galaxy-job/cloud-galaxy-job-${buildver}.jar
cp ${sourcedir}/infrastructure/cloud-galaxy-gateway/target/cloud-galaxy-gateway-${buildver}.jar ${builddir}/cloud-galaxy-gateway/cloud-galaxy-gateway-${buildver}.jar
```

**deploy cloud-galaxy**

```shell
# deploy cloud-galaxy

builddir=/home/aurelius/software
tag=${tag}

# clean old containers and images
function clean_docker_containers__images(){
    if [ $# -lt 1 ]
    then
        echo "no args input..."
        exit;
    else
        cids=$(sudo docker ps | grep $1 | awk '{print $1}')
        for cid in ${cids}
        do
            echo "stop container id" ${cid}
            sudo docker stop ${cid}
            echo "remove container id" ${cid}
            sudo docker rm ${cid}
        done

        iids=$(sudo docker images | grep $1 | awk '{print $3}')
        for iid in ${iids}
        do
            echo "remove image id" ${iid}
            sudo docker rmi ${iid}
        done
    fi
}

# deploy cloud-galaxy-pos & cloud-galaxy-pos-backend
clean_docker_containers__images cloud-galaxy-pos

cd ${builddir}/cloud-galaxy-pos
echo "build docker image cloud-galaxy-pos"
sudo docker build -t cloud-galaxy-pos:${tag} .
echo "run docker container cloud-galaxy-pos"
sudo docker run --privileged=true -idt -p 8086:8086 -v ${builddir}/cloud-galaxy-pos/logs:/app/logs --name cloud-galaxy-pos cloud-galaxy-pos:${tag}

cd ${builddir}/cloud-galaxy-pos-backend
echo "build docker image cloud-galaxy-pos-backend"
sudo docker build -t cloud-galaxy-pos-backend:${tag} .
echo "run docker container cloud-galaxy-pos-backend"
sudo docker run --privileged=true -idt -p 8088:8088 -v ${builddir}/cloud-galaxy-pos-backend/logs:/app/logs --name cloud-galaxy-pos-backend cloud-galaxy-pos-backend:${tag}

# deploy cloud-galaxy-job
clean_docker_containers__images cloud-galaxy-job

cd ${builddir}/cloud-galaxy-job
echo "build docker image cloud-galaxy-job"
sudo docker build -t cloud-galaxy-job:${tag} .
echo "run docker container cloud-galaxy-job"
sudo docker run --privileged=true -idt -p 8087:8087 -v ${builddir}/cloud-galaxy-job/logs:/app/logs --name cloud-galaxy-job cloud-galaxy-job:${tag}

# deploy cloud-galaxy-gateway
clean_docker_containers__images cloud-galaxy-gateway

cd ${builddir}/cloud-galaxy-gateway
echo "build docker image cloud-galaxy-gateway"
sudo docker build -t cloud-galaxy-gateway:${tag} .
echo "run docker container cloud-galaxy-gateway"
sudo docker run --privileged=true -idt -p 8085:8085 -v ${builddir}/cloud-galaxy-gateway/logs:/app/logs --name cloud-galaxy-gateway cloud-galaxy-gateway:${tag}
```

## datahub

**每次更新部署，需先将容器删除，重新打镜像，用新的镜像启动新的容器**

**Dockerfile**

```Dockerfile
FROM microsoft/dotnet:2.1-aspnetcore-runtime AS base
WORKDIR /app

COPY . .
ENTRYPOINT ["dotnet", "Kingdee.DataHub.WebApi.dll"]
```

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
