# docker

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [docker](#docker)
  - [install](#install)
  - [mysql](#mysql)
  - [redis](#redis)
  - [nacos](#nacos)
  - [datahub-core](#datahub-core)
    - [Dockerfile](#dockerfile)
    - [upgrade datahub-core](#upgrade-datahub-core)
    - [build datahub-core](#build-datahub-core)
    - [deploy cloud-galaxy on HW Cloud](#deploy-cloud-galaxy-on-hw-cloud)
  - [cloud-galaxy](#cloud-galaxy)
    - [Dockerfile](#dockerfile-1)
    - [compile cloud-galaxy](#compile-cloud-galaxy)
    - [build cloud-galaxy](#build-cloud-galaxy)
    - [run cloud-galaxy on test](#run-cloud-galaxy-on-test)
    - [deploy cloud-galaxy on HW Cloud](#deploy-cloud-galaxy-on-hw-cloud-1)
    - [message](#message)
  - [pyrubik](#pyrubik)
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

## datahub-core

### Dockerfile

```Dockerfile
FROM microsoft/dotnet:2.1-aspnetcore-runtime AS base
WORKDIR /app

COPY . .
ENTRYPOINT ["dotnet", "Kingdee.DataHub.WebApi.dll"]
```

### upgrade datahub-core

```shell
# upgrade datahub-core
if [ $# -lt 4 ]
then
    echo "------------not enough args(4) input...------------"
    exit;
else
    compile=/kingdee/build/datahub
    module=$1
    tag=1.0.0
    app=$2
    port=$3

    cd ${compile}

    echo "------------update datahub-core------------"
    git pull origin master

    # clean
    dotnet clean

    # build
    dotnet build

    # publish
    dotnet publish ${compile}/Kingdee.DataHub.WebApi/Kingdee.DataHub.WebApi.csproj -o ${compile}/publish

    echo "------------collect datahub-core dlls------------"
    rsync -av ${compile}/publish/* /kingdee/build/${module}/

    cd /kingdee/build/appraisal

    echo "------------updage appraisal static files------------"
    git pull origin master

    echo "------------collect appraisal static files------------"
    rsync -av --exclude appraisal/.git /kingdee/build/appraisal /kingdee/build/${module}/wwwroot/

    cd /kingdee/build/${module}
    echo "------------stop docker container:${app}------------"
    sudo docker stop `sudo docker ps -aq -f name=${app}`

    echo "------------remove container:${app}------------"
    sudo docker rm `sudo docker ps -aq -f name=${app}`

    if [ $4 = true ]
    then
        echo "------------start build ${module}------------"
        echo "------------remove image:${module}------------"
        sudo docker rmi `sudo docker images -q -f reference=${module}:${tag}` -f

        echo "------------build docker images:${module}:${tag}------------"
        sudo docker build -t ${module}:${tag} .
    else
        echo "------------without build ${module}------------"
    fi

    echo "------------run ${app}------------"
    sudo docker run --privileged=true -idt -p ${port}:80 -v /kingdee/logs/${app}/log:/app/Log -v /kingdee/logs/${app}/images:/app/Images --name ${app} ${module}:${tag}
    echo "------------finish upgrade ${app}------------"
fi
```

### build datahub-core

```shell
# build datahub-core
if [ $# -lt 1 ]
then
    echo "------------not enough args(1) input...------------"
    exit;
else
    compile=/kingdee/build/datahub
    repository=kcr.kingdee.com/pos-cloud
    module=$1
    tag=1.0.0

    cd ${compile}

    echo "------------update datahub-core------------"
    git pull origin master

    # clean
    dotnet clean

    # build
    dotnet build

    # publish
    dotnet publish ${compile}/Kingdee.DataHub.WebApi/Kingdee.DataHub.WebApi.csproj -o ${compile}/publish

    echo "------------collect datahub-core dlls------------"
    rsync -av ${compile}/publish/* /kingdee/build/${module}/

    cd /kingdee/build/appraisal

    echo "------------updage appraisal static files------------"
    git pull origin master

    echo "------------collect appraisal static files------------"
    rsync -av --exclude appraisal/.git /kingdee/build/appraisal /kingdee/build/${module}/wwwroot/

    cd /kingdee/build/${module}
    echo "------------start build ${module}------------"
    echo "------------remove image:${module}------------"
    sudo docker rmi `sudo docker images -q -f reference=${module}:${tag}` -f

    echo "------------build docker images:${module}:${tag}------------"
    sudo docker build -t ${module}:${tag} .

    echo "------------push ${app}:${tag}------------"
    sudo docker tag `sudo docker images -q -f reference=${module}:${tag}` ${repository}/${module}:${tag}
    sudo docker push ${repository}/${module}:${tag}
    echo "------------finished build ${module}------------"
fi
```

### deploy cloud-galaxy on HW Cloud

```shell
# deploy cloud-galaxy on HW Cloud

if [ $# -lt 4 ]
then
    echo "not enough args input..."
    exit;
else
    repository=kcr.kingdee.com/pos-cloud
    module=$1
    app=$2
    tag=1.0.0
    port=$3

    echo "------stop container ${app}------"
    # sudo docker stop ${app}
    docker stop `docker ps -aq --filter name=${app}`

    echo "------remove container ${app}------"
    # sudo docker rm ${app}
    docker rm `docker ps -aq --filter name=${app}`

    if [ $4 = true ]
    then
        echo "------remove image ${app}------"
        docker rmi `docker images -q --filter reference=${repository}/${module}:${tag}`

        echo "------pull image ${app} from repository------"
        docker pull ${repository}/${module}:${tag}
    fi

    echo "------run docker container ${app}------"
    docker run --privileged=true -idt -p ${port}:80 -v /kingdee/logs/${app}/log:/app/Log -v /kingdee/logs/${app}/images:/app/Images --name ${app} ${repository}/${module}:${tag}
    # docker run --privileged=true -idt -p ${port}:80 -v /kingdee/logs/${app}/log:/app/Log -v /kingdee/logs/${app}/images:/app/Images --name ${app} ${module}:${tag}
fi
```

```shell
sh deploy-datahub.sh datahub-core datahub-server-core 5000 true
sh deploy-datahub.sh datahub-core datahub-ci-core 5001
```

## cloud-galaxy

### Dockerfile

```Dockerfile
FROM openjdk:8
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' >/etc/timezone
WORKDIR /app
COPY . .
CMD ["java", "-jar", "cloud-galaxy-pos-1.0-SNAPSHOT.jar"]
```

### compile cloud-galaxy

```shell
# compile cloud-galaxy
if [ $# -lt 3 ]
then
    echo "not enough args input..."
    exit;
else
    source=/kingdee/build/cloud-galaxy
    build=/kingdee/build/$1
    layer=$2
    module=$3
    jarver=1.0-SNAPSHOT

    cd $source
    echo "pull source code from gitlab"
    git pull origin master

    echo "compile $1 by maven"
    mvn clean package -DskipTests

    echo "copy module:${module} into ${build}"
    cp ${source}/${layer}/${module}/target/${module}-${jarver}.jar ${build}/${module}-${jarver}.jar

    echo "finish compile $1"
fi
```

### build cloud-galaxy

```shell
# build cloud-galaxy
if [ $# -lt 1 ]
then
    echo "no args input..."
    exit;
else
    build=/kingdee/build/$1
    repository=kcr.kingdee.com/pos-cloud
    app=$1
    tag=1.0.0

    echo "stop container ${app}"
    # sudo docker stop ${app}
    sudo docker stop `sudo docker ps -aq --filter ancestor=${app}:${tag}`

    echo "remove container ${app}"
    # sudo docker rm ${app}
    sudo docker rm `sudo docker ps -aq --filter ancestor=${app}:${tag}`

    echo "remove repository image ${app}"
    sudo docker rmi `sudo docker images -q --filter reference=${repository}/${app}:${tag}`

    echo "remove local image ${app}"
    # sudo docker rmi ${app}
    sudo docker rmi `sudo docker images -q --filter reference=${app}:${tag}` -f

    cd $build
    echo "build docker image ${app}"
    sudo docker build -t ${app}:${tag} .

    echo "push ${app} to repository"
    sudo docker tag `sudo docker images -q --filter reference=${app}` ${repository}/${app}:${tag}
    sudo docker push ${repository}/${app}:${tag}
fi
```

### run cloud-galaxy on test

```shell
# run cloud-galaxy on test
if [ $# -lt 2 ]
then
    echo "not enough args input..."
    exit;
else
    build=/kingdee/build/$1
    app=$1
    tag=1.0.0
    port=$2

    echo "run docker container ${app}"
    sudo docker run --privileged=true -idt -p $port:$port -v ${build}/logs:/app/logs --name ${app} ${app}:${tag}
fi
```

### deploy cloud-galaxy on HW Cloud

```shell
# deploy cloud-galaxy on HW Cloud
# deploy cloud-galaxy

if [ $# -lt 2 ]
then
    echo "------not enough args input...------"
    exit;
else
    repository=kcr.kingdee.com/pos-cloud
    app=$1
    tag=1.0.0
    port=$2

    echo "------stop container ${app}------"
    # sudo docker stop ${app}
    docker stop `docker ps -aq --filter name=${app}`

    echo "------remove container ${app}------"
    # sudo docker rm ${app}
    docker rm `docker ps -aq --filter name=${app}`

    echo "------remove image ${app}------"
    docker rmi `docker images -q --filter reference=${repository}/${app}`

    echo "------pull image ${app} from repository------"
    docker pull ${repository}/${app}:${tag}

    echo "------run docker container ${app}------"
    docker run --privileged=true -idt -p $port:$port -v /kingdee/logs/${app}:/app/logs --name ${app} ${repository}/${app}:${tag}
fi
```

```sh
sh deploy-cloud-galaxy.sh pos 8081
```

### message

```txt
cloud-galaxy-pos-test 升级存在异常，请查阅地铁线与构建服务器上详细日志进行修复后重试

cloud-galaxy-pos-test 升级成功

cloud-galaxy-job 构建异常，请查阅地铁线与构建服务器上详细日志进行修复后重试

cloud-galaxy-pos 构建成功，请使用最新版本升级线上环境
```

## pyrubik

**Dockerfile**

```Dockerfile
FROM python:3.9.5
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' >/etc/timezone
WORKDIR /app
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["python", "bin/manage.py", "janitor"]
```

**deploy pyrubik**

```shell
# deploy pyrubik

builddir=/home/aurelius/software
tag=1.0.0

# clean old containers and images
function clean_docker_containers__images(){
    if [ $# -lt 1 ]
    then
        echo "no args input..."
        exit;
    else
        cids=$(sudo docker ps -a | grep $1 | awk '{print $1}')
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

# deploy pyrubik
clean_docker_containers__images pyrubik

cd ${builddir}/pyrubik
echo "build docker image pyrubik"
sudo docker build -t pyrubik:${tag} .
echo "run docker container pyrubik"
sudo docker run --privileged=true -idt -v ${builddir}/pyrubik/log:/app/log --name pyrubik pyrubik:${tag}
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
