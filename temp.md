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

约定 >> 配置 >> 编码

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
xhr.open(
  "POST",
  "http://172.18.10.89/pos-cloud/api/up-selling/contact-us",
  true
);
xhr.setRequestHeader("Content-Type", "application/json");
xhr.send(
  '{  "id": 0,  "uid": 0,  "uname": "string",  "phone": "string",  "ename": "string",  "area": "string",  "timestamp": "2021-07-22T05:44:35.872Z"}'
);
xhr.onload = function (e) {
  var xhr = e.target;
  console.log(xhr.responseText);
};
```

```shell
java -jar -Dgalaxy.cloud.job.oss-kafka-integrator.enable=true \
    -Dgalaxy.cloud.job.oss-kafka-integrator.partition-executor.partition-start=202012011500 \
    -Dgalaxy.cloud.job.oss-kafka-integrator.partition-executor.partition-stop=202012011600 \
    -Dgalaxy.cloud.job.oss-kafka-integrator.partition-executer.object-prefix=bak-kdcloud-oss- \
    cloud-galaxy-job-1.0-SNAPSHOT.jar
```

# 一、POS Cloud 架构与环境

1. 【POS Cloud 架构】缓存层抽象，提供 pos-backend api 的 Redis 缓存服务
2. 【POS Cloud 架构】持久层抽象，消除通用数据库操作的 Mapper 层与 Service 层
3. 【POS Cloud 环境】华为云环境部署，DockerService、Nacos、Sentinel、MySQL、Redis、Nginx、Pos Cloud、Job Cloud
4. 【POS Cloud 环境】自动化测试、构建、部署，Jenkins Agent、DockerRepository、CI/CD 地铁线
5. 【POS Cloud 环境】前端部署，动静分离

# 二、新特性弹窗推送（落地页）

1. 【基础数据】模块（子系统）基础资料
2. 【基础数据】版本基础资料优化
3. 【POS Cloud 功能】落地页服务 Rest API，服务端接口开发，华为云部署，云平台发布
4. 【POS Cloud 功能】落地页跳转（产品端打开）

# 三、帮助中心配置中心与云服务

1. 【工具预研】wiki 转 markdown，及其代码化
2. 【工具预研】markdown 转 html，及其代码化
3. 【基础数据】文档基础资料、目录树、权限隔离、版本隔离，作为帮助中心配置后台
4. 【文档服务】html 文档自动生成与手动触发、版本隔离
5. 【文档服务】文档（左目录、版本隔离）获取 Rest API，服务端接口开发，华为云部署，云平台发布
6. 【连接服务】常见问题、使用技巧、相关课程获取 Rest API，服务端接口开发，华为云部署，云平台发布
7. 【产品端功能】帮助中心页面开发，帮助中心页面开发，文档目录树、文档、常见问题、使用技巧、相关课程的条件请求和展示

# 四、异常提示可运营性改造

1. 【数据分析】产品异常（含免统计）统计
2. 【数据分析】产品异常错误 ID 可用性分析
3. 【数据集成】社区产品异常错误 ID 与运营资料映射数据同步
4. 【POS Cloud 功能】运营资料 Rest API，服务端接口开发，华为云部署，云平台发布
