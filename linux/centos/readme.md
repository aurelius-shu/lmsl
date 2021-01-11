# 网络配置

## 设置 IP, GATEWAY, DNS

```shell
# 编辑网络配置
vi  /etc/sysconfig/network-scripts/ifcfg-ens33
```

```
TYPE=Ethernet
PROXY_METHOD=none
BROWSER_ONLY=no
BOOTPROTO=static
DEEROUTE=yes
IPV4_FAILURE_FATAL=no
IPV6INIT=yes
IPV6_AUTOCONF=yes
IPV6_DEFROUTE=yes
IPV6_FAILURE_FATAL=no
IPV6_ADDR_GEN_MODE=stable-privacy
NAME=ens33
#删除UUID,防止克隆时出现两台机器的唯一标识是一样的
DEVICE=ens33
ONBOOT=yes
#ip
IPADDR=192.168.100.5
#网关
GATEWAY=192.168.100.2
#子网掩码
NETMASK=255.255.255.0
#使用主的DNS
DNS1=192.29.29.29
#备用的DNS
DNS2=8.8.8.8
```

```shell
# 重启网络服务
systemctl restart network.service
```

## 修改主机名

```shell
hostnamectl set-hostname  node-base
```

## 关闭防火墙

```shell
# CentOS6关闭防火墙使用以下命令
# 临时关闭
service iptables stop
# 禁止开机启动
chkconfig iptables off

# CentOS7关闭防火墙使用以下命令
# 临时关闭
systemctl stop firewalld
# 禁止开机启动
systemctl disable firewalld
Removed symlink /etc/systemd/system/multi-user.target.wants/firewalld.service.
Removed symlink /etc/systemd/system/dbus-org.fedoraproject.FirewallD1.service.

# 如果安装了iptables-service，也可以使用下面的命令
yum install -y iptables-services
# 关闭防火墙
service iptables stop
Redirecting to /bin/systemctl stop  iptables.service
# 检查防火墙状态
service iptables status
Redirecting to /bin/systemctl status  iptables.service
iptables.service - IPv4 firewall with iptables
   Loaded: loaded (/usr/lib/systemd/system/iptables.service; disabled; vendor preset: disabled)
   Active: inactive (dead)

# 关闭SELinxu命令（永久关闭）
vi /etc/selinux/config
# 将SELINUX=enforcing 改 为SELINUX=disabled ,设置后需要重启才能生效.
/usr/sbin/sestatus
SELinux status: disabled
```

## 创建用户，设置文件权限

```shell
# 添加用户通过手动输入修改密码
useradd admin
# 更改用户的密码
passwd  admin
# 所有的身份验证令牌已经成功更新。
123456  passwd：
# 设置admin用户具有root权限  修改 /etc/sudoers 文件，找到下面一行，在root下面添加一行，如下所示：
visudo
## Allow root to run any commands anywhere
root    ALL=(ALL)     ALL
admin   ALL=(ALL)     ALL
# 修改完毕，现在可以用admin帐号登录，然后用命令 su - ，即可获得root权限进行操作。
# root用户先创建文件 设置权限
su - admin
sudo mkdir module
sudo mkdir software
sudo chown admin:admin module/
sudo chown admin:admin software/
ls -al
```

## 图形化界面安装（可选安装）

```shell
# 在命令行下 输入下面的命令来安装Gnome包
yum groupinstall -y "GNOME Desktop"
# 更新系统的运行级别。设置默认图形化界面启动
ln -sf /lib/systemd/system/runlevel5.target /etc/systemd/system/default.target

# 设置CentOS7自动以root身份登陆gnome桌面
vi /etc/gdm/custom.conf
# 然后在[daemon]下面添加：
# [daemon]
# AutomaticLoginEnable=True
# AutomaticLogin=root  #你想自动登录的用户名
# 保存并重启，重启的时候已经以root用户登录了。
```

## centos7 yum 源设置（可选设置）

```shell
yum install wget
cd /etc/yum.repos.d/
mv /etc/yum.repos.d/CentOS-Base.repo  /etc/yum.repos.d/CentOS-Base.repo.backup
wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
yum clean all
yum makecache
```

# 克隆虚拟机

1. 修改静态 IP

```shell
nmcli c reload
nmcli c up ens33
```

2. 修改主机名

3. 修改主机与 IP 映射关系

4. 修改 root 密码
