Web 开发

1. TCP
2. Web Server + Servlet(.war)
3. Web Server + JSP(Servlet)
4. Web Server + MVC(Servlet + JSP)
5. Web Server + Servlet + Filter + Listener

Spring 开发

1. IoC
2. AOP
3. DB
   - JDBC
   - DAO
   - Hibernate
   - JPA
   - MyBatis -> MapperFactoryBean
   - 设置 ORM
4. 开发 Web 应用

## 20210704

1. Nacos
2. Sentinel
3. Seata

约定 >> 配置 >> 编码

docker - 20210707

## 20210708

同步
异步

List 并发修改异常

-- jenkins

公平锁、非公平锁 -- 线程饿死
读锁和写锁，都可能发生死锁

锁降级 ==> 获取写锁 -> 获取读锁 -> 释放写锁（降级） -> 释放读锁
锁升级 ==> 
行锁（发生死锁）、表锁

BlockingQueue

## CORS 配置

**Cross-Origin Resource Sharing**

1. 在服务端，网关，Nginx 三层，只能配置一个放行
2. 在服务端配置放行，通过网关请求还是会存在跨域拦截

### 跨域测试

```javascript
var xhr = new XMLHttpRequest();
xhr.open('POST', 'http://172.18.10.89/pos-cloud/api/up-selling/contact-us', true);
xhr.setRequestHeader("Content-Type","application/json");
xhr.send('{  "id": 0,  "uid": 0,  "uname": "string",  "phone": "string",  "ename": "string",  "area": "string",  "timestamp": "2021-07-22T05:44:35.872Z"}');
xhr.onload = function(e) {
    var xhr = e.target;
    console.log(xhr.responseText);
}
```