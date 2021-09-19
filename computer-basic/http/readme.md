# HTTP

## HTTP 方法

1. GET
2. HEAD
3. POST
4. PUT
5. PATCH
6. DELETE
7. OPTIONS
8. CONNECT
9. TRACE

## HTTP 状态码

1XX - Informational 接收的请求正在处理
2XX - Success 请求正常处理完毕
3XX - Redirection 重定向
4XX - Client Error 服务器无法处理请求
5XX - Server Error 服务端处理请求出错

## HTTP 首部

### 通用首部字段

### 请求首部字段

### 响应首部字段

### 实体首部字段

## 具体应用

### 连接管理

1. 短连接 - 每个请求一个连接，HTTP/1.1 之前默认选择，Connection: Keep-Alive 改长连接
2. 长连接 - 复用一个连接发送多次 HTTP 请求，HTTP/1.1 开始的默认选择
3. 流水线 - 请求一个接着一个，下个请求的发送不用等待拿到上个请求的相应

### Cookie

服务器发送到用户浏览器并保存在本地的一小块数据，浏览器之后想统一服务器发起请求时被携带

1. 用途
   - 会话管理
   - 个性化设置
   - 浏览器行为跟踪
2. 创建过程
   - 服务器通过 Set-Cookie 的响应首部向浏览器发送数据，客户端得到后保存在浏览器中
   - 浏览器之后发送请求时，通过 Cookie 请求首部携带该部分数据
3. 分类
   - 会话期 Cookie: 浏览器关闭自动删除
   - 持久性 Cookie: 指定过期时间（Expires）或有效期（max-age）成为持久性 Cookie
4. 作用域
   - Domain: 指定可以接收 Cookie 的域名，不设置则仅限当前主机，设置了则可以包含其子域名
   - Path: 指定主机下可以接收 Cookie 的路径（存在于 URL 中的路径），子路径也会被匹配
5. JavaScript
   - 通过 document.cookie 可以创建新的 Cookie，也可以获取非 HttpOnly 标记的 Cookie
6. HttpOnly
   - HttpOnly 标记的 Cookie 不能被 JS 脚本调用，一定程度上避免了 XSS 攻击
7. Secure
   - Secure 标记的 Cookie 只能通过 HTTPS 协议加密过的请求发送给服务器，不过 Cookie 自身不安全性依旧无法提供安全保障
8. Session
   - 数据存储在服务器端更加安全
   - 存储：服务器上的内存、文件、数据库、Redis
   - Session ID 需要经常重新生成，安全性要求高的场景需要配合验证码，重新输入密码等使用
9. 禁用 Cookie
   - Session ID 也将无法写入 Cookie，只能通过 HTTP 请求参数传递 ÎÎ
   - Cookie 只能存储 ASCII，Session 可以是任意数据
   - Cookie 存放在浏览器端，安全性低，敏感数据建议加密
   - 大型应用的用户信息存储开销巨大，不建议统一存放在 Session

### 缓存

1. Cache-control
   - no-store: 禁止进行缓存
   - no-cache: 强制确认缓存，强制验证资源有效性
   - private: 私有缓存，单独用户使用，一般在浏览器
   - public: 公共缓存，多个用户使用，一般在代理服务器
   - max-age: 缓存过期设置
   - expire: 设置过期时间，优先处理 max-age

### 通信数据转发

#### 代理

1. 目的:
   - 缓存
   - 负载均衡
   - 网络访问控制
   - 访问日志记录
2. 方式：
   - 正向代理: 代理在客户端，用户察觉得到
   - 反向代理: 代理在服务端，用户察觉不到

#### 网关

网关可以将 HTTP 请求转化为其他协议的通信，请求其他非 HTTP 服务

#### 隧道

使用 SSL 等加密手段，在客户端与服务端之间建立一条安全的通信线路

## HTTPS

由 HTTP 与 SSL(Secure Sockets Layer)通信，再由 SSL 与 TCP 通信，使用了`隧道转发`
采用加密+认证机制，防篡改

### HTTP 的安全问题

1. 明文通信，易被窃听
2. 不验证通信方身份，易被伪装
3. 无法证明报文完整性，易被篡改

### 加密

#### 对称加密

加密和解密使用相同的秘钥
优点：运算速度快
缺点：无法安全将秘钥传输给对方

#### 非对称加密

加密和解密使用不同的秘钥（公开秘钥加密），还可以用来做签名验证

优点：安全地将公钥传输给发送方
缺点：运算速度慢

#### HTTPS 加密方式

- 非对称加密传输对对称加密所需的 Secret Key，保证安全性
- 使用 Secret Key 传输数据，保证效率

### 认证

CA, Certificate Authority， 数字证书认证机构，可信赖的第三方
CA 对 Server 公钥签名，并与公钥绑定生成公钥证书
Client 通过 HTTPS 向 Server 发起请求时，Server 将证书发给 Client
Client 获取到证书中的公钥，先签名验证公钥可信，再使用公钥开始通信

### HTTPS 缺点

1. 需要加密解密，速度更慢
2. 需要支付证书授权的费用

## HTTP/2.0

### HTTP/1.x 缺陷

1. 需要多个连接实现并发或缩短延迟
2. 缺失压缩请求和响应头部的机制，每次重复发送，导致了不必要的网络流量
3. 缺失资源优先级机制，TCP 连接利用率低

### 二进制分帧

报文分为 Headers 帧和 Data 帧，都是二进制
通信过程只会有一个 TCP 连接，承载任意数量的双向数据流（Stream）

数据流（Stream） - 承载双向信息，有唯一标识符和优先级
消息（Message） - 一系列完整逻辑请求和响应的帧
帧（Frame） - 最小的通信单位，可以交错发送，之后通过帧头标识符重组

### 服务端推送

Server 将 page.html 需要的 script.js、style.css 一起发送给 Client，避免 Client 再次请求

### 首部压缩

Client 和 Server 同时维护和更新一个包含之前见过的首部字段表，避免重复传输(差量传输)
使用 Huffman 编码对首部字段进行压缩

## HTTP/1.1 新特性

1. 默认长连接
2. 支持流水线
3. 支持同时打开多个 TCP 连接
4. 支持虚拟主机
5. 新增状态码 100
6. 支持分块传输编码
7. 新增缓存处理指令 max-age

## GET vs. POST

`作用` GET 获取资源，POST 传输实体主体
`参数` GET 参数以查询字符串出现在 URL（ASCII），POST 参数存储在实体主体（明文，标准字符集）
`安全` GET 方法被认为是安全的，只会读取资源，POST 方法被认为是不安全的，会修改服务端状态
`幂等` GET 方法是幂等的（无副作用，执行一次和多次效果一样，Server 的状态也一样，HEAD,PUT,DELETE），POST 不是
`缓存` GET 可缓存，POST 大多数情况不可缓存，响应报文的 Cache-Control 没有指定的不进行缓存
`XMLHttpRequest` GET 方法将 Header 和 Data 一起发送，POST 先发送 Header，在发送 Data（火狐除外）
