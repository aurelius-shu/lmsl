# nginx

## 配置日志文件访问

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
