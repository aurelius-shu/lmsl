<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Java 第一季](#java-第一季)
  - [1. ++i 与 i++ 运算字节码过程](#1-i-与-i-运算字节码过程)
  - [2. 单例模式](#2-单例模式)
  - [3. 类初始化过程、实例初始化过程、方法重写](#3-类初始化过程-实例初始化过程-方法重写)
  - [4. 方法的参数传递机制](#4-方法的参数传递机制)
  - [5. 递归与循环迭代](#5-递归与循环迭代)
  - [6. 成员变量与局部变量](#6-成员变量与局部变量)
  - [7. Spring Bean 的作用域之间的区别](#7-spring-bean-的作用域之间的区别)
  - [8. Spring 支持的常用数据库事务传播属性和事务隔离级别](#8-spring-支持的常用数据库事务传播属性和事务隔离级别)
  - [9. SpringMVC 中 GET/POST 请求的中文乱码问题](#9-springmvc-中-getpost-请求的中文乱码问题)
  - [10. SpringMVC 的工作流程](#10-springmvc-的工作流程)
  - [11. MyBatis 中实体类的属性名称和表中的字段名不一样的处理方式](#11-mybatis-中实体类的属性名称和表中的字段名不一样的处理方式)
  - [12. Linux 常用服务类相关命令](#12-linux-常用服务类相关命令)
  - [13. git 相关命令](#13-git-相关命令)
  - [14. Redis 持久化类型](#14-redis-持久化类型)
  - [15. MySQL 什么时候适合建索引](#15-mysql-什么时候适合建索引)
  - [16. JVM 垃圾回收机制](#16-jvm-垃圾回收机制)
  - [17. Redis 的使用场景](#17-redis-的使用场景)
  - [18. Elasticsearch VS. solr](#18-elasticsearch-vs-solr)
  - [19. 单点登录实现的过程](#19-单点登录实现的过程)
  - [20. 购物车的实现过程](#20-购物车的实现过程)
  - [21. 消息队列的使用场景](#21-消息队列的使用场景)
- [Java 第二季](#java-第二季)
  - [1. 前提和说明](#1-前提和说明)
  - [2. volatile](#2-volatile)
  - [3. JMM 内存模型](#3-jmm-内存模型)
  - [4. 可见性 Demo](#4-可见性-demo)
  - [5. 不保证原子性 Demo](#5-不保证原子性-demo)
  - [6. 不保证原子性 原因](#6-不保证原子性-原因)
  - [7. 不保证原子性 解决方法](#7-不保证原子性-解决方法)
  - [8. 指令重排 Demo 1](#8-指令重排-demo-1)
  - [9. 指令重排 Demo 2](#9-指令重排-demo-2)
  - [10. 单例模式多线程下存在安全问题](#10-单例模式多线程下存在安全问题)
  - [11. volatile 单例模式](#11-volatile-单例模式)
  - [12. CAS](#12-cas)

<!-- /code_chunk_output -->

# Java 第一季

[视频](https://www.bilibili.com/video/BV1Eb411P7bP?spm_id_from=333.788.b_636f6d6d656e74.28)
[资料](https://pan.baidu.com/s/1Kg7UUpO3wwALX6x28cWA7A#list/path=%2F%E5%B0%9A%E7%A1%85%E8%B0%B7Java%E5%AD%A6%E7%A7%91%E5%85%A8%E5%A5%97%E6%95%99%E7%A8%8B%EF%BC%88%E6%80%BB207.77GB%EF%BC%89%2F3.%E5%B0%9A%E7%A1%85%E8%B0%B7%E5%85%A8%E5%A5%97JAVA%E6%95%99%E7%A8%8B--%E5%BE%AE%E6%9C%8D%E5%8A%A1%E7%94%9F%E6%80%81%EF%BC%8866.68GB%EF%BC%89%2F%E5%B0%9A%E7%A1%85%E8%B0%B7%E7%BB%8F%E5%85%B8Java%E9%9D%A2%E8%AF%95%E9%A2%98%EF%BC%88%E7%AC%AC1%E5%AD%A3%EF%BC%89) [8op3]

## 1. ++i 与 i++ 运算字节码过程

```java
public static void main(String[] args) {
    int i = 1;
	i = i++;
	int j = i++;
	int k = i + ++i * i++;
	System.out.println("i=" + i);
	System.out.println("j=" + j);
	System.out.println("k=" + k);
}
```

- **执行结果**

```
    4, 1, 11
```

- 赋值=，最后计算

- =右边的从左到右加载值依次压入操作数栈

- 实际先算哪个，看运算符优先级

- 自增、自减操作都是直接修改变量(局部变量表)的值，不经过操作数栈

- 最后的赋值操作返回的结果由操作数栈弹出

## 2. 单例模式

- 饥饿模式 \* 3（枚举）

- 懒汉模式 \* 3（静态内部类）

  - 由于 Java 的内存模型，双重检查不成立，因此延迟加载存在问题
  - 静态内部类不属于外部类实例，不会自动随着外部类的加载和初始化而初始化，在使用静态内部内时才会加载和初始化
  - 静态内部类加载和初始化时调用，只会调用一次，是线程安全的

## 3. 类初始化过程、实例初始化过程、方法重写

![](./image/1.3-clinit-init-override.png)

- **执行结果**

```
    5, 1, 10, 6,  9, 3, 2, 9, 8, 7
    9, 3, 2, 9, 8, 7
```

- 类初始化过程

  1. 类的实例化需要先加载并初始化该类

     - main 所在的类需要先加载和初始化

  2. 子类的初始化需要先初始化父类

  3. 类初始化就是执行 \<clinit\> 方法

     - \<clinit\> 方法由静态变量显示赋值代码和静态代码块组成
     - 类变量显示赋值代码和静态代码块代码从上到下顺序执行
     - \<clinit\> 方法只执行一次

- 实例初始化

  1. 实例初始化就是执行 \<init\> 方法

     - \<init\> 方法可能重载多个，有几个构造器就有几个\<init\> 方法
     - \<init\> 方法由非静态实例变量显示赋值代码、非静态代码块、对应构造器代码组成
     - 非静态实例变量显示赋值和非静态代码块从上到下顺序执行，而对应构造器代码最后执行
     - 每次创建实例对象，调用对应构造器，执行的就是对应的 \<init\> 方法
     - \<init\> 方法的首行是 super() 或 super(实参列表)，即对应父类的 \<init\> 方法

- 方法的重写 Override

  1. 哪些方法不可以被重写

     - final 方法
     - 静态方法
     - private 等子类中不可见方法

  2. 对象的多态性

     - 子类如果重写了父类的方法，通过子类对象调用的一定是子类重写过的代码
     - 非静态方法默认的调用对象是 this
     - this 对象在构造器或者说 \<init\> 方法中就是正在创建的对象

  3. Override 和 Overload 的区别

  4. Override 重写的要求
     - 方法名
     - 形参列表
     - 返回值类型
     - 抛出的异常列表
     - 修饰符
  5. invokespecial 指令

## 4. 方法的参数传递机制

![](./image/1.4-func-parameter.png)

- **执行结果**

```
   1, hello, 200, {2,2,3,4,5}, 11
```

- 形参是基本数据类型
  - 传递数据值
- 实参是引用数据类型
  - 传递地址值
  - 特殊的类型：String、包装类等对象不可变性，不可变对象的赋值相当于改变变量指向的地址

## 5. 递归与循环迭代

```
   有n步台阶，一次只能上1步或2步，共有多少种走法？
```

- 方法调用自身称为递归，利用变量的原值推出新值称为迭代
- 递归
  - 优点：大问题转化为小问题，可以减少代码量，同时代码精简，可读性好；
  - 缺点：递归调用浪费了空间，而且递归太深容易造成堆栈的溢出。
- 迭代
  - 优点：代码运行效率好，因为时间只因循环次数增加而增加，而且没有额外的空间开销；
  - 缺点：代码不如递归简洁，可读性好

## 6. 成员变量与局部变量

![](./image/1.6-variable.png)

- **执行结果**

```
   2, 1, 5
   1, 1, 5
```

- 就近原则
  - 局部变量与成员变量重名时，操作的是成员变量还是局部变量取决于最近定义的变量
  - 局部变量与实例变量重名
    - 在实例变量前面加“this.”
  - 局部变量与类变量重名
    - 在类变量前面加“类名.”
- 变量的分类
  - 成员变量：类变量、实例变量
  - 局部变量
- 非静态代码块的执行：每次创建实例对象都会执行
- 方法的调用规则：调用一次执行一次

- 局部变量与成员变量的区别
  - 声明的位置
    - 局部变量：方法体{}中，形参，代码块{}中
    - 成员变量：类中方法外
      - 类变量：有 static 修饰
      - 实例变量：没有 static 修饰
  - 修饰符
    - 局部变量：final
    - 成员变量：public、protected、private、final、static、volatile、transient
  - 值存储的位置
    - 局部变量：栈
    - 实例变量：堆
    - 类变量：方法区
  - 作用域
    - 局部变量：从声明处开始，到所属的}结束
    - 实例变量：在当前类中“this.”(有时 this.可以缺省)，在其他类中“对象名.”访问
    - 类变量：在当前类中“类名.”(有时类名.可以省略)，在其他类中“类名.”或“对象名.”访问
  - 生命周期
    - 局部变量：每一个线程，每一次调用执行都是新的生命周期
    - 实例变量：随着对象的创建而初始化，随着对象的被回收而消亡，每一个对象的实例变量是独立的
    - 类变量：随着类的初始化而初始化，随着类的卸载而消亡，该类的所有对象的类变量是共享的

## 7. Spring Bean 的作用域之间的区别

**scope 属性指定 bean 的作用域**

| 类型      | 说明                                                                                                            |
| --------- | --------------------------------------------------------------------------------------------------------------- |
| singleton | 默认类型，当 IOC 容器一创建就会创建 bean 的实例，而且是单例的，每次得到的都是同一个实例                         |
| prototype | 原型的，当 IOC 容器创建是不会创建 bean 实例，每次调用 getBean 方法时实例化该 bean，而且每次得到的都是不同的实例 |
| request   | 每次请求实例化一个 bean，适用于 WebApplicationContext 环境                                                      |
| session   | 在依次会话中共享一个 bean，适用于 WebApplicationContext 环境                                                    |

## 8. Spring 支持的常用数据库事务传播属性和事务隔离级别

- **`propagation` 属性用于设置事务传播级别**

| propagation 属性 | 说明                                                                                                                                                     |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| REQUIRED         | 如果当前没有事务，就创建一个新事务，如果当前有事务，就加入到当前事务中执行                                                                               |
| SUPPORTS         | 表示如果有事务，就加入到当前事务，如果没有，那也不开启事务执行。这种传播级别可用于查询方法，因为 SELECT 语句既可以在事务内执行，也可以不需要事务；       |
| MANDATORY        | 表示必须要存在当前事务并加入执行，否则将抛出异常。这种传播级别可用于核心更新逻辑，比如用户余额变更，它总是被其他事务方法调用，不能直接由非事务方法调用； |
| REQUIRES_NEW     | 表示不管当前有没有事务，都必须开启一个新的事务执行。如果当前已经有事务，那么当前事务会挂起，等新事务完成后，再恢复执行；                                 |
| NOT_SUPPORTED    | 表示不支持事务，如果当前有事务，那么当前事务会挂起，等这个方法执行完成后，再恢复执行；                                                                   |
| NEVER            | 和 NOT_SUPPORTED 相比，它不但不支持事务，而且在监测到当前有事务时，会抛出异常拒绝执行；                                                                  |
| NESTED           | 表示如果当前有事务，则开启一个嵌套级别事务，如果当前没有事务，则开启一个新事务。                                                                         |

- [并发一致性问题](http://www.cyc2018.xyz/%E6%95%B0%E6%8D%AE%E5%BA%93/%E6%95%B0%E6%8D%AE%E5%BA%93%E7%B3%BB%E7%BB%9F%E5%8E%9F%E7%90%86.html#%E4%B8%8D%E5%8F%AF%E9%87%8D%E5%A4%8D%E8%AF%BB)

- [隔离级别](http://www.cyc2018.xyz/%E6%95%B0%E6%8D%AE%E5%BA%93/%E6%95%B0%E6%8D%AE%E5%BA%93%E7%B3%BB%E7%BB%9F%E5%8E%9F%E7%90%86.html#%E5%9B%9B%E3%80%81%E9%9A%94%E7%A6%BB%E7%BA%A7%E5%88%AB)

## 9. SpringMVC 中 GET/POST 请求的中文乱码问题

- POST 通过 Filter 指定 utf-8 编码
- GET 通过 tomcat 配置文件指定 urlencoding 为 utf-8 编码

## 10. SpringMVC 的工作流程

![](./image/1.10-springmvc-processing.png)

## 11. MyBatis 中实体类的属性名称和表中的字段名不一样的处理方式

- sql 语句中字段别名
- 开启驼峰命名规则
- 使用 resultMap 自定义映射规则

## 12. Linux 常用服务类相关命令

- centos6

![](./image/1.12.1-centos6-service.png)
![](./image/1.12.2-centos6-runlevel.png)

- centos7

![](./image/1.12.3-centos7-service.png)

## 13. git 相关命令

![](./image/1.13-git.png)

![](./image/1.13-git-processing.png)

## 14. Redis 持久化类型

- RDB(Redis DataBase)

  - Redis 会单独创建（fork）一个子进程来进行持久化，会先将数据写入到 一个临时文件中，待持久化过程都结束了，再用这个临时文件替换上次持久化好的文件。 整个过程中，主进程是不进行任何 IO 操作的，这就确保了极高的性能 如果需要进行大规模数据的恢复，且对于数据恢复的完整性不是非常敏感，那 RDB 方式要比 AOF 方式更加的高效。RDB 的缺点是最后一次持久化后的数据可能丢失

- AOF(Append Of File)

  - 以日志的形式来记录每个写操作（增量保存），将 Redis 执行过的所有写指令记录下来(读操作不记录)， 只许追加文件但不可以改写文件，redis 启动之初会读取该文件重新构建数据，换言之，redis 重启的话就根据日志文件的内容将写指令从前到后执行一次以完成数据的恢复工作

## 15. MySQL 什么时候适合建索引

![](./image/1.15-mysql-index.png)

## 16. JVM 垃圾回收机制

- [GC4 大算法](https://youthlql.gitee.io/javayouth/#/docs/Java/JVM/JVM%E7%B3%BB%E5%88%97-%E7%AC%AC10%E7%AB%A0-%E5%9E%83%E5%9C%BE%E5%9B%9E%E6%94%B6%E6%A6%82%E8%BF%B0%E5%92%8C%E7%9B%B8%E5%85%B3%E7%AE%97%E6%B3%95?id=%e6%b8%85%e9%99%a4%e9%98%b6%e6%ae%b5%ef%bc%9a%e6%a0%87%e8%ae%b0-%e6%b8%85%e9%99%a4%e7%ae%97%e6%b3%95)

## 17. Redis 的使用场景

![](./image/1.17-redis-usage.png)

## 18. Elasticsearch VS. solr

![](./image/1.18-es-solr.png)

## 19. 单点登录实现的过程

- 一处登录多处使用（分布式系统），将 token 放入到 cookie 中

![](./image/1.19-single-sign-on.png)

## 20. 购物车的实现过程

[视频](https://www.bilibili.com/video/BV1Eb411P7bP?p=20)

## 21. 消息队列的使用场景

- 背景: 在分布式系统处理高并发请求
- 弊端: 消息的不确定性，可以通过延迟队列，轮询技术解决

- 异步

![](./image/1.21.1-mq-sync.png)

- 并行

![](./image/1.21.2-mq-concurrent.png)

- 排队

![](./image/1.21.3-mq-queue.png)

- 电商场景

![](./image/1.21.4-mq-market.png)

# Java 第二季

[视频](https://www.bilibili.com/video/BV18b411M7xz?spm_id_from=333.788.b_636f6d6d656e74.29)
[资料](https://gitee.com/moxi159753/LearningNotes/tree/master/%E6%A0%A1%E6%8B%9B%E9%9D%A2%E8%AF%95/JUC)

## 1. 前提和说明

- 面试题

![](./image/2.0.1-mayi-meituan.png)
![](./image/2.0.2-baidu.png)
![](./image/2.0.3-toutiao.png)
![](./image/2.0.4-meituan.png)
![](./image/2.0.5-mayi.png)

- 目录

1. 前提知识和要求
2. Java 基础
3. JUC
4. JVM + GC
5. MQ
6. NoSQL - Redis
7. Spring 原理
8. Netty + RPC
9. 网络通信与协议
10. Database
11. SpringBoot + SpringCloud + Dubbo
12. 项目

## 2. volatile

- [资料](https://mp.weixin.qq.com/s/Oa3tcfAFO9IgsbE22C5TEg)

- Java 虚拟机提供的轻量级同步机制

  1. 保证可见性
  2. 不保证原子性
  3. 禁止指令重排

## 3. JMM 内存模型

- 可见性
- 原子性
- 有序性

![](./image/2.3.1-jmm.png)
![](./image/2.3.2-jmm.png)

## 4. 可见性 Demo

[代码测试](https://gitee.com/moxi159753/LearningNotes/tree/master/%E6%A0%A1%E6%8B%9B%E9%9D%A2%E8%AF%95/JUC/1_%E8%B0%88%E8%B0%88Volatile/1_Volatile%E5%92%8CJMM%E5%86%85%E5%AD%98%E6%A8%A1%E5%9E%8B%E7%9A%84%E5%8F%AF%E8%A7%81%E6%80%A7#%E5%8F%AF%E8%A7%81%E6%80%A7%E4%BB%A3%E7%A0%81%E9%AA%8C%E8%AF%81)

## 5. 不保证原子性 Demo

[代码测试](https://gitee.com/moxi159753/LearningNotes/tree/master/%E6%A0%A1%E6%8B%9B%E9%9D%A2%E8%AF%95/JUC/1_%E8%B0%88%E8%B0%88Volatile/2_Volatile%E4%B8%8D%E4%BF%9D%E8%AF%81%E5%8E%9F%E5%AD%90%E6%80%A7#%E4%BB%A3%E7%A0%81%E6%B5%8B%E8%AF%95)

## 6. 不保证原子性 原因

```
public void add();
    Code:
       0: aload_0
       1: dup
       2: getfield      #2    // Field n:I
       5: iconst_1
       6: iadd
       7: putfield      #2    // Field n:I
      10: return
```

## 7. 不保证原子性 解决方法

- synchronized
- JUC 院子操作

## 8. 指令重排 Demo 1

![](./image/2.8-jmm-ordering.png)

[指令重排](https://gitee.com/moxi159753/LearningNotes/tree/master/%E6%A0%A1%E6%8B%9B%E9%9D%A2%E8%AF%95/JUC/1_%E8%B0%88%E8%B0%88Volatile/3_Volatile%E7%A6%81%E6%AD%A2%E6%8C%87%E4%BB%A4%E9%87%8D%E6%8E%92)

## 9. 指令重排 Demo 2

![](./image/2.9-jmm-forbid-ordering.png)

## 10. 单例模式多线程下存在安全问题

- 双端检锁（DCL）在 JMM 存在指令重排可能

## 11. volatile 单例模式

## 12. CAS


