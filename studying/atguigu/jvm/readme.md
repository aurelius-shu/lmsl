# JVM

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

## 栈

### Minor GC、Major GC、Full GC

- Partital GC，部分收集
  - Minor GC/Young GC，只针对新生代，会引发 STW
  - Major GC/Old GC，只针对老年代，比 Minor GC 慢 10 倍以上
- Full GC，整堆收集

### 内存分配策略
