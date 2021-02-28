# 2-13

====== spring boot 2 ======

- 12:10 ~ 13:00
- 13:20 ~ 14:10
- 18:20 ~ 19:10
- 20:30 ~ 21:20
- 21:20 ~ 22:10
- 23:00 ~ 23:50

# 2-15

====== spring boot 2 ======

- 11:30 ~ 12:20
- 15:20 ~ 16:10
- 16:20 ~ 17:10
- 17:20 ~ 18:10
- 18:40 ~ 19:30
- 19:30 ~ 20:20
- 20:20 ~ 21:10
- 21:10 ~ 22:00
- 22:00 ~ 22:50
- 22:50 ~ 23:10

# 2-16

====== java 第三季 ======

- 10:50 ~ 11:40
- 11:50 ~ 12:40
- 11:40 ~ 13:30
- 14:20 ~ 15:10
- 15:40 ~ 16:30
- 16:30 ~ 17:20

# 2-17

====== java 第三季 ======

- 10:00 ~ 11:00
- 11:20 ~ 12:10
- 14:30 ~ 15:20

====== java 第二季 ======

- 15:40 ~ 16:30 (volatile、JMM)
- 16:40 ~ 17:30 (CAS、ABA)
- 17:30 ~ 18:20 (集合不安全)
- 19:50 ~ 20:40 (集合不安全)
- 20:40 ~ 21:30 (Java 锁)
- 21:30 ~ 22:20 (Java 锁)
- 23:00 ~ 23:50 (阻塞队列)
- 23:50 ~ 24:15 (synchronized 与 ReentrantLock 区别)

# 2-18

====== java 第二季 ======

- 12:00 ~ 12:50 (线程池)
- 12:50 ~ 13:40 (线程池)
- 13:40 ~ 14:30 (JVM)
- 15:00 ~ 15:50 (JVM)
- 16:40 ~ 17:30 (JVM)
- 17:30 ~ 18:20 (Reference)
- 18:20 ~ 19:10 (OOM)
- 20:20 ~ 21:10 (GC)
- 21:10 ~ 22:00 (G1)
- 22:05 ~ 22:55 (Linux, GitHub)

# 2-19

====== java 第二季 ======

- 19:40 ~ 20:30

  - ConditionOn...
  - 八大排序算法
  - 设计模式

- 20:30 ~ 21:20

  1. 包查找顺序:
     - 当前 package
     - import package
     - java.lang 包
  2. classpath 顺序查找

- 21:20 ~ 22:10

  - logging

- 22:10 ~ 23:00

  - reflection

- 23:00 ~ 23:30

# 2-21

- 11:40 ~ 12:30

6. [spring boot2](https://www.bilibili.com/video/BV19K4y1L7MT?spm_id_from=333.788.b_636f6d6d656e74.14)

# 2-22

1. [idea](https://www.bilibili.com/video/BV1PW411X75p?p=3&spm_id_from=pageDriver)(180min/2)
   [done]

# 2-23

2. [mysql](https://www.bilibili.com/video/BV1KW411u7vy?spm_id_from=333.788.b_636f6d6d656e74.22)
   [10]

3. [spring cloud](https://www.bilibili.com/video/BV18E411x7eT?spm_id_from=333.788.b_636f6d6d656e74.15)
   [55]

# 2-24

# 2-27

[spring security]() [done]
[spring cloud security oauth2.0]() [done]

6. [spring](https://www.bilibili.com/video/BV1Vf4y127N5?spm_id_from=333.788.b_636f6d6d656e74.12)

- 解耦

  - new
  - Factory
  - IoC <- 反射

- IoC
  - BeanFactory (使用时创建)
    - ApplicationContext (加载配置时创建)

# 2-28

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

4. [redis](https://www.bilibili.com/video/BV1oW411u75R?spm_id_from=333.788.b_636f6d6d656e74.18)

5. [ActiveMQ](https://www.bilibili.com/video/BV164411G7aB?spm_id_from=333.788.b_636f6d6d656e74.24)

6. [nginx](https://www.bilibili.com/video/BV1zJ411w7SV?spm_id_from=333.788.b_636f6d6d656e74.21)

[netty]

8. [k8s]

# 3-14
