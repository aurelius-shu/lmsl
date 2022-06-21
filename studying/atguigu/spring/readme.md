<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

<!-- /code_chunk_output -->

### Spring

特点：

1. 降低代码解耦，组件的创建和使用分离，组件的创建、注入（相互引用）、配置转交给 IoC 容器
2. AOP 编程支持，解耦，重用，不修改源码添加功能到主干

#### IoC

```
Inversion of Control - 控制反转
Dependency Inj·ection - 依赖注入
```

1. 实现原理
   XML/注解解析 + 工厂模式 + 反射

2. 作用域
   singleton, prototype, request, session

3. 生命周期
   construct, set, postconstruct, getbean, predestroy

4. 循环依赖

   - 构造器注入无法解决循环依赖，BeanCurrentlyCreationException
   - setter 注入避免循环依赖
   - singleton 支持循环依赖，prototype 不支持

5. 三级缓存

   - A 创建需要 B，现将 A 放入三级缓存，去创建 B
   - B 创建需要 A，去 一、二、三级缓存一次查找 A，在 三级缓存找到 A，将 A 注入 B，并将 A 从三级缓存移到二级缓存
   - B 创建完成，直接放入一级缓存，返回 A 的创建，将一级缓存中的 B 注入 A，A 完成创建，将 A 从二级缓存移到一级缓存

#### AOP

1. 实现原理
   JVM 动态代理、CGLIB 动态代理
2.

#### DataBase

#### Web

#### JMX

#### Question

- 生命周期

  1. 无参构造
  2. set
  3. 后置处理方法(在初始化之前)
  4. init
  5. 后置处理方法(在初始化之后)
  6. getBean
  7. destroyBean(context.close)

- 自动装配

  1. byName
  2. byType (同类型多 bean 时报错)

- 创建 bean 实例的注解（功能一样）

  1. @Component
  2. @Service
  3. @Controller
  4. @Repository

- 开启 component 扫描

  - @ComponentScan

- 属性注入

  1. @AutoWired 根据属性类型注入
  2. @Qualifier 根据属性名称注入，与@Autowired 一起使用
  3. @Resource 根据熟悉类型或名称注入
  4. @Value 注入普通类属性

- AOP 操作

  - AspectJ (独立于 Spring)

    - xml
    - 注解

  - execution([修饰符] [返回值类型] [类名] [方法] ([参数]))

- 事务
  - 编程式
  - 声明式
- @Transactional

  - propagation 事务传播行为管理
    - REQUIRED 有事务，直接使用，否则新起一个事务
    - REQUIRES_NEW 一定新起一个事务，有事务的将事务挂起
  - ioslation 事务隔离级别
    - 问题
      - 脏读 一个未提交事务读到了另一个未提交事务的修改
      - 不可重复度 一个未提交事务读到了一个已提交事务的修改
      - 幻读 一个未提交事务读到了一个已提交事务的添加
    - 隔离级别
      - READ_UNCOMMITTED
      - READ_COMMITTED
      - REPEATABLE_READ
      - SERIALIZABLE
  - timeout 超时时间
  - readOnly 是否只读
  - rollbackFor 回滚 回滚的异常
  - noRollbackFor 不会滚 不回滚的异常

- SpringWebflux

  - 异步非阻塞

    - 同步 调用者发送请求，对方回应之后才能做其他事情
    - 异步 调用者发送请求，不用等对方回应就可以做其他事情

    - 阻塞 被调用者收到一个请求，做完任务后才反馈
    - 非阻塞 被调用者收到一个请求，马上给出反馈，不用等待做完任务

    - 吞吐量 更多的请求
    - 伸缩性

- 响应式编程

  - 观察者模式

    - Observer
    - Observable

  - Flow
    - Publisher
    - Subscruber

- Webflux Reactor 实现

  - Reactor

    - Mono
    - Flux

    - 三种数据信号
      - 元素值
      - 错误信号
      - 完成信号

  - 操作符

    - map
    - flatMap 圧平成流式

- SpringWebflux

  - netty

    - NIO

  - WebHandler

    - DispatcherHandler
      - HandlerMapping
      - HandlerAdapter
      - HandlerResultHandler

  - RouterFunction
  - HandlerFunction

  - 请求和响应

    - ServletRequest
    - ServletResponse

    - ServerRequest
    - ServerResponse

  - 实现方式
    - 注解
    - 函数式编程
