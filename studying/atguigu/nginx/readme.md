# Nginx

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Nginx](#nginx)
  - [安装](#安装)
  - [反向代理](#反向代理)
  - [动静分离](#动静分离)
  - [负载均衡](#负载均衡)
  - [访问日志文件](#访问日志文件)

<!-- /code_chunk_output -->

## 安装

```shell
# 添加 nginx 的yum repro库
rpm -ivh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm

# 查看 nginx 信息
yum info nginx

# 安装 nginx
yum install -y nginx

# 启动 nginx
systemctl start nginx.service
```

## 反向代理

- `反向代理` `Reverse Proxy` 方式是指以代理服务器来接受 internet 上的连接请求，然后将请求转发给内部网络上的服务器，并将从服务器上得到的结果返回给 internet 上请求连接的客户端，此时代理服务器对外就表现为一个服务器。

[参考](https://www.cnblogs.com/jianxie/p/3990377.html)

```conf
server {
    listen       80;
    # nginx所在服务器的主机名
    server_name  nginx-01.edu.cn;

    #反向代理的配置
    # 拦截所有请求
    location / {
        root html;
        #这里是代理走向的目标服务器：tomcat
        proxy_pass http://192.168.0.21:8080;
    }
}
```

## 动静分离

```conf
# 动态资源 index.jsp
location ~ .*\.(jsp|do|action)$ {
    proxy_pass http://tomcat-01.itcast.cn:8080;
}

# 静态资源
location ~ .*\.(html|js|css|gif|jpg|jpeg|png)$ {
    expires 3d;
}
```

## 负载均衡

- `负载均衡` `Load Balance` 指建立在现有网络结构之上，并提供了一种廉价有效透明的方法扩展网络设备和服务器的带宽、增加吞吐量、加强网络数据处理能力、提高网络的灵活性和可用性。其原理就是数据流量分摊到多个服务器上执行，减轻每台服务器的压力，多台服务器共同完成工作任务，从而提高了数据的吞吐量。

```conf
# 在 http 这个节下面配置一个叫upstream的，后面的名字可以随意取，但是要和location下的proxy_pass http://后的保持一致
http {
    # 是在http里面的, 已有http, 不是在server里,在server外面
    upstream tomcats {
        server shizhan02:8080 weight=1;#weight表示多少个
        server shizhan03:8080 weight=1;
        server shizhan04:8080 weight=1;
    }

    #卸载server里
    location ~ .*\.(jsp|do|action) {
        #tomcats是后面的tomcat服务器组的逻辑组号
        proxy_pass http://tomcats;
    }
}
```

## 访问日志文件

1. 添加对 log 文件的浏览器查看

```txt
# 修改nginx mime.types，为text/plain 添加log类型文件
types{
    text/plain txt log;
}
```

2. 添加服务监听路径

```txt
server {
    listen       80;
    server_name  localhost;
    location /logs/ {
        #log日志存放目录
        alias /home/logs/;

        #打开目录浏览功能
        autoindex on;

        #默认为on，显示出文件的确切大小，单位是bytes
        #显示出文件的大概大小，单位是kB或者MB或者GB
        autoindex_exact_size off;

        #默认为off，显示的文件时间为GMT时间。
        #改为on后，显示的文件时间为文件的服务器时间
        autoindex_localtime on;

        add_header Cache-Control no-store;

        if (-f $request_filename){
            #定义文档以及编码格式防止乱码
            add_header Content-Type "text/plain;charset=utf-8";
            }
        }
    }
 }
```

3. 重启 nginx

```shell
sudo nginx -s reload
```

```conf
server {
        listen 80;
        server_name localhost;
        charset utf-8;

        # location /pos-cloud/ {
        #        proxy_pass http://localhost:8085/pos-cloud/;
        # }

        location /pos/ {
                alias /app/cloud-galaxy-web/;
        }
}
```
