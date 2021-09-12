<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [常见问题](#常见问题)
  - [2020-06](#2020-06)
    - [2020-06-10](#2020-06-10)
    - [2020-06-11](#2020-06-11)
    - [2020-06-12](#2020-06-12)
    - [2020-06-13](#2020-06-13)
    - [2020-06-14](#2020-06-14)
    - [2020-06-15](#2020-06-15)
    - [2020-06-16](#2020-06-16)
    - [2020-06-17](#2020-06-17)

<!-- /code_chunk_output -->

# 常见问题

## 2020-06

### 2020-06-10

1. 解决 Maven 工程 compile, install 时[WARNING] Using platform encoding (UTF-8 actually) to copy filtered resources

**在 maven 项目的 pom.xml 中添加如下配置**

```xml
<properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
</properties>
```

2. Intellij idea 报错：Error : java 不支持发行版本 5

**报错应该是项目编译配置使用的 Java 版本不对，需要检查一下项目及环境使用的 Java 编译版本配置。**

    1. 在 Intellij 中点击“File” -->“Project Structure”，看一下“Project”和“Module”栏目中 Java 版本是否与本地一致

    2. 点击“Settings”-->“Bulid, Execution,Deployment”-->“Java Compiler”，Target bytecode version 设为本地 Java 版本。

3. Failed to execute goal org.apache.maven.plugins:maven-compiler-plugin:3.1:compile (default-compile) on project java-base: Compilation failure

**删掉 maven 默认的去找的那个 settings.xml(C:\Users\user\.m2\settings.xml)文件，这样自定义的文件就会生效了**

4. 整数的运算结果永远精确；整数除以 0 编译不会报错，但是运行会报错；计算结果溢出不会报错，但是会得到一个奇怪的结果

5. 浮点数常常不能精确表示，0.1 的二进制是一个无线循环小时，无论 float 还是 double 都只能存一个近似值；浮点数除以 0 得到一个正（负）无穷大数（Infinity, -Infinity, NaN)

6. 将下面一组 int 值视为字符的 Unicode 码，把它们拼成一个字符串

```java
int a = 72;
int b = 105;
int c = 65281;
String s = String.valueOf((char)a) + (char)b + (char)c;
System.out.println(s);
```

7. 数组本身是引用类型，元素是值类型时，改变单元素时是值发生改变，元素是引用类型时，改变单元素时是指向发生改变

### 2020-06-11

1. 配置 maven 阿里源

**conf/settings.xml**

```xml
<mirrors>
  <mirror>
    <id>alimaven</id>
    <name>aliyun maven</name>
    <url>http://maven.aliyun.com/nexus/content/groups/public/</url>
    <mirrorOf>central</mirrorOf>
  </mirror>
  <mirror>
    <id>alimaven</id>
    <mirrorOf>central</mirrorOf>
    <name>aliyun maven</name>
    <url>http://maven.aliyun.com/nexus/content/repositories/central/</url>
  </mirror>
</mirrors>
```

**配置不生效**

```shell
cp settings.xml ~/.m2/
```

2. 在 Java 中，任何 class 的构造方法第一行语句必须是调用父类构造方法，如果没有明确的调用父类的构造方法，编译器会帮我们自动加一句 super(); 如果父类没有提供无参构造方法，编译器会报错；此时必须显示的调用一个带参 super()；自雷不会继承任何父类的构造方法，子类的默认构造方法是编译器自动生成的，不是继承的

3. 子类与父类的方法名和方法参数相同，返回值不同，编译器会报错

4. final 修饰的方法不能被子类复写，final 修饰的类不能被继承，final 修饰的字段必须在创建对象时初始划，随后不可修改，final 修饰的局部变量不可重新赋值

5. 接口可以定义 default 方法，与抽象类的非抽象方法不同的是，default 方法在接口中是无法访问到字段的，而抽象类的非抽象方法是可以访问抽象类中的字段的

### 2020-06-12

1. [maven] maven 安装后，maven 用户可能没有某些路径的足够权限，如 repo，导致报如找不到路径等的错

2. idea pre-module bytecode version 默认为 1.5 问题
   **配置 pom.xml**

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-compiler-plugin</artifactId>
            <version>3.8.1</version>
            <configuration>
                <source>1.8</source>
                <target>1.8</target>
            </configuration>
        </plugin>
    </plugins>
</build>
```

3. idea maven 输出控制台的中文乱码

**Setting->maven->runner 配置 VMoptions:-Dfile.encoding=GB2312**

### 2020-06-13

1. [接口] 接口可以添加 final 的静态字段，实际上 interface 的字段只能是 public static final 的，一次可以直接去掉这三个修饰符

2. [类] 嵌套类有访问类中 private 成员的权限，不含作用域修饰符的成员作用域是 package

3. [类] 一个 .java 文件只能有一个 public 类，可以包含多个非 public 类，如果有 public 类，文件名必须和 public 类的类名相同

4. [jar 包] jar 包的层级必须与 package 声明的层级相同；可以包含一个 MANIFEST.MF 文件，添加 Main-Class（指定主类，这样就可以直接运行 jar 包： java -jar hello.jar），classpath 等信息；classpath 决定了搜索 class 的路径和顺序

5. [module] java 9 引入了 module 概念，用于便捷的打包；module 声明了 export 的类才可以被引用；

6. [java] jre 是运行 Java 字节码的虚拟机；jdk 是编译 Java 源码为 Java 字节码的工具，其中包含了 编译器，调试器等开发工具，同时包含了 jre

7. [String] Java 中的 String 是不可变的，这种不可变是通过内部 private final char[] 字段以及没有任何修改该字段的方法实现的

8. [String] Java 编译器在编译期会自动把相同的字符串当作一个对象放入常量池，如果是运行期间相同的 String 对象，不是一个对象则不相等

9. [链式操作] 实现链式操作的关键是返回实例本身

10. [包装类] 所有的包装类型都是不变类，value 字段都是以 private final 修饰的；所有的包装类都不要使用 == 比较，而应该使用 equals()；对于较小的数字，编译器会始终返回缓存的相同实例，因此可能 == 比较恰好为 true；Byte.valueOf() 方法返回的 Byte 实例全部是缓存实例；所有的数字包装类都继承自 **Number**

11. [enum] enum 是使用 final 修饰的 class，不可被继承，成员是使用 static final 修饰的静态常量；enum 可以使用 == 比较，因为 enum 类型的每个常量在 JVM 中只有一个唯一实例；每个 enum 的值都是 class 实例

12. [enum] enum 的字段可以是非 final 类型，这样可以在运行其间修改，但不推荐

13. [enum] enum 可以编写自定义构造方法（private）、字段(final)、方法；enum 自定义的值转 enum 需要实现 valueOf 静态方法

14. [BigInteger] BigInteger 转 int、long 等超出范围抛出 ArithmeticException，转 float 超出异常则返回 Infinity

15. [BigDecimal] BigDecimal 是由一个 BigInteger 表示完整整数，一个 scale 表示小数位数来实现的；BigDecimal 的 equals() 方法比较的是完整整数和小数位数，使用 compareTo()方法比较准确

16. [Math] 针对浮点数计算结果，StrictMath 保证所有平台计算结果都是完全相同，Math 会尽量针对平台优化计算速度，可能存在误差

17. [Exception] 捕获异常并抛出异常时，需要携带捕获的异常信息；在 finally 中抛出异常时，应该通过 getSuppressed() 方法将 catch 中可能的异常加入 throw 的异常对象中

### 2020-06-14

1. [Log] 始终使用 Commons Logging 接口写入日志，如果需要把日志写入文件，只需要把正确的配置文件和 Log4j 相关的 jar 包放入 classpath，即可实现 Log4j 写入的日志切换；或者使用 SLF4J 的接口，Logback 的实现；直接使用 log4j 更加可控

2. [class] JVM 为每个加载的 class 创建一个且仅一次对应的 Class 实例，该实例保存 class 的所有信息；通过 Class 实例获取 class 信息的方法被称为反射；反射可以访问对象的 private 作用域

3. [reflect] 反射通过 setAccessible(true) 调用非 public 方法时有可能失败，JVM 运行期可能存在 SecurityManager 阻止设置运行访问

4. [reflect] 反射父类方法作用于子类实例时，仍然遵循多态原则，即总是调用实际类型的复写方法；Constructor 总是当前类定义的构造方法，和父类无关，不存在多态问题

5. [动态代理] 通过 Proxy 创建代理对象，然后将接口方法“代理”给 InvocationHandler

6. [Annotation] 使用 @interface 定义注解，注解参数类似无参方法，可以使用 default 设置一个默认值；元注解是可以修饰其他注解的注解（@Target,@Retention,@Repeatable,@Inherited)

7. [泛型] 可以把 ArrayList<Integer>向上转型为 List<Integer>（T 不能变！），但不能把 ArrayList<Integer>向上转型为 ArrayList<Number>（T 不能变成父类）
8. [IO] Input 指从外部读入数据到内存，如磁盘、网络；Output 指吧数据从内存输出到外部；如果需要读写的是字符，且字符不全是单字节表示的 ASCII 字符，那么使用 char 来读写更方便，这种流叫字符流
9. [Serializable] 一个 Java 对象要能序列化，必须实现一个特殊的 java.io.Serializable 接口，Serializable 没有定义任何方法，是一个空接口，这样的空接口被称为“标记接口”（Marker Interface）
10. [IO] InputStreamReader 可以把一个 InputStream 转换成一个 Reader；OutputStreamWriter 可以将任意的 OutputStream 转换为 Writer
11. [JSON] JSON 只允许使用 UTF-8 编码，不存在编码问题；JSON 只允许使用双引号作为 key，特殊字符用\转义；

### 2020-06-15

1. [encryption] 三防：防窃听，防篡改，防伪造

2. [encode] URL 编码是对字符进行编码，表示成 %XX 形式，Base64 编码是对二进制数据进行编码，表示成字符串格式

3. [hash] 安全的 hash 算法要求：碰撞概率低，不能猜测输出

### 2020-06-16

1. [thread] 对目标线程调用 interrupt()方法可以请求中断一个线程，目标线程通过检测 isInterrupted()标志获取自身是否已中断。如果目标线程处于等待状态，该线程会捕获到 InterruptedException；目标线程检测到 isInterrupted()为 true 或者捕获了 InterruptedException 都应该立刻结束自身线程；

### 2020-06-17

1. [maven] SLF4J: Class path contains multiple SLF4J bindings.

**将指定引用的 SLF4J 引用排除掉**

```xml
<dependency>
    <groupId>org.apache.hadoop</groupId>
    <artifactId>hadoop-common</artifactId>
    <version>2.10.0</version>
    <exclusions>
        <exclusion>
            <groupId>org.slf4j</groupId>
            <artifactId>slf4j-log4j12</artifactId>
        </exclusion>
    </exclusions>
</dependency>
```

2. [maven] How to Create an Executable JAR with Maven
   [指导文档](https://www.baeldung.com/executable-jar-with-maven)

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-assembly-plugin</artifactId>
    <version>3.3.0</version>
    <executions>
        <execution>
            <phase>package</phase>
            <goals>
                <goal>single</goal>
            </goals>
            <configuration>
                <archive>
                    <manifest>
                        <mainClass>
                            com.xxxxxx.galaxy.db.SQLServerService
                        </mainClass>
                    </manifest>
                </archive>
                <descriptorRefs>
                    <descriptorRef>jar-with-dependencies</descriptorRef>
                </descriptorRefs>
            </configuration>
        </execution>
    </executions>
</plugin>
```

3. [synchronized] JVM 允许同一个线程重复获取同一个锁，这种能被同一个线程反复获取的锁，就叫做可重入锁

4. [synchronized] 死锁产生的条件是多线程各自持有不同的锁，并互相试图获取对方已持有的锁，导致无限等待；避免死锁的方法是多线程获取锁的顺序要一致

5. [ReadWriteLock] 只允许一个线程写入，允许多个线程在没有写入时同时读取，适合读多写少的场景

6. [StampedLock] 把读锁细分为乐观读和悲观读，能进一步提升并发效率；StampedLock 是不可重入锁

7. 包查找顺序:
   - 当前 package
   - import package
   - java.lang 包
