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

# 3.1

- 索引

  - 帮做 MySQL 高效获取数据的数据结构，排好序的快速查找（B 树）

- explain

  - id 数字大的优先级高
  - ## select_type
  - table
  - type
  - possible_keys
  - key
  - key_len
  - ref
  - rows
  - Extra

# 3.2

4. [redis](https://www.bilibili.com/video/BV1oW411u75R?spm_id_from=333.788.b_636f6d6d656e74.18)

# 3.3

6. [nginx](https://www.bilibili.com/video/BV1zJ411w7SV?spm_id_from=333.788.b_636f6d6d656e74.21)

7. [ActiveMQ](https://www.bilibili.com/video/BV164411G7aB?spm_id_from=333.788.b_636f6d6d656e74.24)

[15]

# 3.4

[57]
[netty]

8. [k8s]

# 3.6

java
spring 5
spring boot 2
spring cloud
spring security
spring cloud security oauth2.0
mysql
redis
nginx
activemq
java 第二、三季

# 3-12

(11)

1. java
   (3)

   - Web,Spring
   - 函数式编程
   - 设计模式

2. mysql

3. redis
4. activemq
5. 面试
6. spring boot, spring cloud
7. 大数据面试题
8. 项目经验
9. 算法

# 3-13

# 3-14

# 3-15

1. JVM 与 Java 体系结构
2. 类加载子系统
3. 运行时数据区概述及线程
4. 程序计数器
5. 虚拟机栈
6. 本地方法接口
7. 本地方法栈
8. 堆
9. 方法区
10. 直接内存
11. 执行引擎
12. StringTable
13. 垃圾回收概述
14. 垃圾回收相关算法
15. 垃圾回收相关概念
16. 垃圾回收器

- 跨语言的平台
- 基于栈的指令

  - 跨平台
  - 指令小
  - 指令多
  - 性能比寄存器差

- JVM 生命周期

  - 启动
  - 执行
  - 退出

- JVM 发展历程

  - SUN Classic, 只支持解释器
  - Exact
  - HotSpot
  - JRockit
  - J9, IBM
  - Azul
  - Liquid, BEA
  - Apache Harmony
  - Microsoft JVM
  - TaobaoJVM
  - Graal

- 内存结构

  - Class File
  - Class Loader Subsystem
  - Runtime Data Area
  - Interpreter
  - Execution Engine
  - Native Method Interface
  - Native Method Library

- 类加载器子系统

  - loading
  - linking
    - verifaication
    - preparation
    - resolution
  - initialization
    - 类构造器方法 clinit
    - init

- 类加载器分类

  - 引导类加载器（Java 的核心类库使用引导类加载器）
  - 扩展类加载器
  - 系统类加载器（应用类加载器，自定义类使用）
  - Operatial（自定义类加载器）

- 自定义类加载器

- ClassLoader

- 双亲委派机制（优势）

  - 避免类的重复加载
  - 保护程序安全，防止核心类被篡改（沙箱安全机制）

- JVM 中两个 class 对象是否为同一个类

  - 完整类名必须一直，包括包名
  - 加载这个类的 ClassLoader 必须相同

- 局部变量表

  - slot （double 与 long 占用两个 slot）
  - 作用域

- 数据类型：
  - 基本数据类型，引用数据类型
- 声名位置：

  - 成员变量：在使用时，都经历过默认初始化赋值
    - 类变量：linking/prepare 阶段，给类变量默认赋值 --> initial 阶段给类变量赋值即给静态代码块赋值
    - 实例变量：随着对象的创建，会在堆空间中分配实例变量空间，并进行默认赋值
  - 局部变量：在使用前，必须要显示赋值，否则变异不通过

- 操作数栈
- 符号引用转换为直接引用

  - 静态链接
  - 动态链接

- 方法的绑定机制

  - 早期绑定
  - 晚期绑定

- 非虚方法
  编译器确定调用版本
  （静态方法、私有方法、final 方法、实例构造器、父类方法）
- 虚方法

子类对象的多态的使用前提：1. 类的继承关系 2. 方法的重写

- 方法调用

  - 指令：

    - invokestatic 调用静态方法
    - invokespecial 调用构造器，私有及父类方法
    - invokevirtual 调用所有虚方法
    - invokeinterface 调用接口

  - 动态调用指令

  - invokedynamic 调用 lambda 表达式

  - IllegalAccessError maven 包引用版本冲突
  - 虚方法表 解析阶段

- 方法返回地址
- 附加信息

- 虚拟机栈

1. 举例栈溢出的情况
   - StackOverflowError，超出栈大小
   - OOM，超出内存大小
   - 栈大小通过 -Xss 调整
2. 能保证不出现栈溢出吗？
   - 不能
3. 分配的栈内存越大越好吗？
   - 不一定
4. 垃圾回收是否会涉及到虚拟机栈?
   - 不会
5. 方法中定义的局部变量是否线程安全
   - 不是，在方法中产生，并在方法中消亡的变量是线程安全的，从方法外传入，或被传递到方法外的变量是线程不安全的

- 什么是线程安全的？

  - 只有一个线程操作的数据是线程安全的
  - 多个线程操作的数据，如果不考虑同步机制，就不是线程安全的

- 本地方法

  - 使用 native 修饰的方法
  - 不能用 abstract 修饰

  - 与 Java 外部环境交互
  - 与操作系统交互
  - Java 本身实现

- 本地方法栈（HotSpot 独有）
  - 本地方法接口
  - 本地方法库

# 堆

## 堆的核心概念

### 内存细分（逻辑上）

1.  新生代（Eden/Survivor）
2.  老年代
3.  永久代（元空间-> 方法区）

## 堆内存大小设置与 OOM

1. 堆内存大小设置

-Xms600m 设置堆空间（新生代+老年代）的初始内存空间
-Xmx600m 设置堆空间（新生代+老年代）的最大内存空间

2. 堆空间的初始大小

初始内存大小： 内存大小/64
最大内存大小： 内存大小/4

3. 查看设置的参数

- jps /jstat -gc 进程 id
- -XX:+PrintGCDetails

## 年轻代与老年代

1. 新生代与老年代比例设置

   - NewRatio，设置新生代和老年代的比例，默认 1:2（NewRatio=2）

2. Eden 和 Survior 比例

   - SurvivorRatio，默认 8:1:1（SurvivorRatio=8），存在自适应机制（UseAdaptiveSizePolicy）

3. 设置新生代的大小

   - Xmn，一般不设置

## 对象分配过程

    - survior, 复制之后有交换，谁空谁to
    - 频繁在新生代收集，很少在老年代收集，几乎不在永久代/云空间收集
    - 80%的对象在新生代被回收

- Minor GC、 Major GC、 Full GC
  - Minor GC / YGC
  - Full GC

## 堆空间分代思想

## 内存分配策略

## 对象分配内存：TLAB

## 小结堆空间的参数设置

-XX:PrintFlagsInitial 所有参数的默认值
-XX:PrintFlagsFinal 所有参数的最终值（修改后的，可能不是初始值）
--查看具体参数的值： jinfo -flag survivorRatio 进程 id
-Xms: 初始堆空间内存(默认物理内存/64)
-Xmx: 最大堆空间内存(默认物理内存/4)
-Xmn: 新生代内存大小(初始值及最大值)
-XX:NewRatio: 配置新生代与老年代在堆结构中的占比
-XX:SurvivorRatio: 配置新生代中 Eden 和 S0/S1 空间的占比
-XX:MaxTenuringThreshold: 设置新生代的最大年龄
-XX:+PrintGCDetails: 输出纤细的 GC 处理日志
-XX:+PrintGC: 打印 gc 简要信息
-XX:HandlePromotionFailure: 是否设置空间分配担保

## 堆是分配对象的唯一选择吗

如果经过逃逸分析后发现，一个对象没有逃逸出方法，就可能被优化成栈上分配

- 逃逸分析：new 的对象是否有可能在方法外被调用
- 栈上分配
- 同步省略（锁消除）
- 标量替换（分离对象：聚合量和标量）

# 方法区

## 栈、堆、方法区的交互关系

## 方法区的理解

## 设置方法区大小与 OOM

-XX:PermSize
-XX:MaxPermSize
-XX:MetaspaceSize
-XX:MaxMetaspaceSize

## 方法区的内部结构

- 类型信息
- 域信息（类属性）
- 方法信息

## 方法区的使用举例

## 方法区的演进细节

1. 永久代空间大小难以确定
2. 永久代的调优比较困难

## 方法区的垃圾回收

## 总结

# 对象

## 实例化

1. 创建对象的方式
   - new
   - Class 的 newInstance()，反射，只能调用空参构造器，权限必须是 public
   - Constructor 的 newInstance(Xxx)，反射，可以调用空参、带参构造器，权限没有要求
   - 使用 clone()，不调用构造器，实现 Clonable 接口的 clone()
   - 反序列化，从文件、网络中获取一个对象的二进制流
   - 第三方库 Objenesis
2. 创建对象的步骤
   - 判断对象对应的类是否加载、链接、初始化
   - 为对象分配内存
   - 处理并发安全问题
   - 初始化分配到的空间
   - 设置对象的对象头
   - 执行 init 方法进行初始化

## 内存布局

1. 对象头
   - 运行时元数据
   - 类型指针
2. 实例数据
3. 对齐填充

## 访问定位

- 句柄访问
- 直接指针

# 直接内存

# 执行引擎

## 执行引擎概述

装在字节码到其内部，将字节码编译成对应平台的机器指令

## Java 代码编译和执行过程

## 机器码、指令、汇编语言

## 解释器

## JIT 编译器

程序运行过程中编译

- AOT 编译器
  Ahead Of Time Compiler
  静态提前编译器

# StringTable

## String 的基本特性

- 不可变性

- 字符串常量池是不会存储相同内容的字符串的 (Hashtable)

## String 的内存分配

## String 的基本操作

## 字符串拼接操作

- 拼接中只要有变量，则相当于在堆空间中 new String()，具体内容位拼接的结果

- 两边都是字符串常量或常量应用是，直接使用字符串常量

## intern() 方法

- 如果常量池中已有这个字符串，则返回常量池中的字符串，否则将字符串放入常量池并返回该字符串

- 字符串常量池不存在时：
  - jdk6 中会在串池中 new 一个对象放入
  - jdk7 中会将串池中的字符串指向堆中已经存在的串

## StringTable 垃圾回收

## G1 中 String 的去重操作

# GC

## 垃圾

运行程序中没有任何指针指向的对象

# 垃圾回收相关算法

## 标记阶段

- 引用计算
  - 引用计数器，随时回收
  - 无法处理循环引用
- 可达性分析算法（GC Roots)
  - 虚拟机栈中引用的对象
  - 本地方法栈内 JNI(本地方法)引用的对象
  - 方法区中类静态属性引用的对象
  - 方法区中常量引用的对象
  - 所有被同步锁 synchronized 持有的对象
  - Java 虚拟机内部的引用（Class 对象，常驻异常对象，系统类加载器）
  - Java 虚拟机内部情况的 JMXBean、JVMTI 中注册的回调、本地代码缓存等
  - 临时性：分代收集和局部收集（Partial GC）

## 对象的 finalization 机制

对象被销毁前的自定义处理逻辑

## MAT 与 JProfiler 的 GC Roots 溯源

## 清除阶段：标记-清除算法

## 清除阶段：复制算法

## 清除阶段：标记压缩算法

## 小结

## 分代收集算法

## 增量收集算法、分区算法

Serial：复制算法，串行，STW
SerialOld：标记整理，串行，STW

ParNew：复制算法，并发，STW
CMS：标记清除，并发，STW，与用户线程同步

Parallel Scavenge，可控制的吞吐量，复制算法，并发，STW
Parallel Old：标记整理，并发，STW
