# 攻击技术

## XSS

**跨站脚本攻击**

### 原理

在页面插入 JavaScript 获取 document.cookie

### 防范

1. HttpOnly，静止 JavaScript 中获取 document.cookie
2. 转义标签中插入的 JS、Html，让插入的 JS、Html 失去执行能力

## CSRF

**跨站请求伪造**

### 原理

在恶意页面加入用户刚刚访问过的发送、支付、购买等链接，用户访问该链接时造成恶意转账

### 防范

1. Referer 限制 Http 请求源域名
2. 服务端使用随机数 + token 方式替代 cookie 校验
3. 验证码

## SQL Injection

**SQL 注入攻击**

### 原理

在 SQL 参数中加入`,`, `;` 等，从而实现 SQL 的 where 条件失效，或执行恶意 delete, insert 等语句

### 防范

1. 采用参数化查询（预编译，可重复使用）
2. 转义 `'` 字符

## DoS & DDoS

**(分布式)拒绝服务攻击**

### 原理

洪水攻击，通过高负荷请求让服务器带宽或资源耗尽，使服务中断或停止

### 防范

1. 防火墙黑/白名单
2. 黑洞引导
3. 流量清洗
