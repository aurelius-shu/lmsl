<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [安装](#安装)
  - [CentOS 7](#centos-7)
- [pip](#pip)
  - [requirements](#requirements)
  - [pip 镜像](#pip-镜像)

<!-- /code_chunk_output -->

# 安装

## CentOS 7

1. 安装 wget

```shell
yum install wget
```

2. 安装 openssl-devel bzip2-devel expat-devel gdbm-devel readline-devel sqlite-devel gcc

```shell
yum -y install openssl-devel bzip2-devel gdbm-devel readline-devel sqlite-devel gccexpat-devel
yum -y install openssl-devel bzip2-devel gdbm-devel readline-devel sqlite-devel zlib-devel ncurses-devel tk-devel db4-devel libpcap-devel xz-devel libffi-devel gcc
```

3. 下载解压

```shell
wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tgz
tar -zxvf Python-3.7.2.tgz
```

4. 配置

```shell
cd Python-3.7.2
mkdir /usr/local/python3
./configure --prefix=/usr/local/python3
```

5. 编译安装

```shell
make && make install
```

编译失败

```shell
sudo yum install -y libffi libffi-devel
```

6. 建立软连接

```shell
ln -s /usr/local/python3/bin/python3 /usr/bin/python3
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
```

virtualenv

```
pip3 install virtualenv
ln -s /usr/local/python3/bin/virtualenv /usr/bin/virtualenv
```

7. python3.8 改成默认 python（pip 同理）

```shell
# 查找python位置
whereis python

# 删除软链接
rm /usr/bin/python

# 查看环境变量
echo $PATH

# 生成python3的软链接到环境变量
ln -s /usr/local/bin/python3.8 /usr/bin/python
```

# pip

## requirements

```shell
# 在项目中分析出所有依赖的库
pip freeze > requirements.txt

# 下载包到 DIR 这个目录中
pip download -d DIR -r requirements.txt
pip wheel -w DIR -r requirements.txt

# 离线安装
pip3 install --no-index --find-links=DIR -r requirements.txt

# 直接安装 requirements.txt
pip install -r requirements.txt
```

## pip 镜像

> 修改 C:\Users\Administrator\AppData\Roaming\pip\pip.ini

```
[global]
timeout = 60000
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
use-mirrors = true
mirrors = https://pypi.tuna.tsinghua.edu.cn
```
