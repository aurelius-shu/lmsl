# Alibaba Java 开发手册

## 编码规约

1. 【推荐】在常量与变量的命名时，表示类型的名词放在词尾，以提升辨识度。

- 正例:startTime / workQueue / nameList / TERMINATED_THREAD_COUNT
- 反例:startedAt / QueueOfWork / listName / COUNT_TERMINATED_THREAD

2. 接口和实现类的命名有两套规则

- 【强制】对于 Service 和 DAO 类，基于 SOA 的理念，暴露出来的服务一定是接口，内部的实现类用 Impl 的后缀与接口区别。
  - 正例:CacheServiceImpl 实现 CacheService 接口。
- 【推荐】如果是形容能力的接口名称，取对应的形容词为接口名(通常是–able 的形容词)。
  - 正例:AbstractTranslator 实现 Translatable 接口。

3. 【参考】枚举类名带上 Enum 后缀，枚举成员名称需要全大写，单词间用下划线隔开。

- 说明: 枚举其实就是特殊的常量类，且构造方法被默认强制是私有。
- 正例: 枚举名字为 ProcessStatusEnum 的成员名称:SUCCESS / UNKNOWN_REASON。

4. 【参考】各层命名规约:

- Service/DAO 层方法命名规约
  1. 获取单个对象的方法用 get 做前缀。
  2. 获取多个对象的方法用 list 做前缀，复数结尾，如:listObjects。
  3. 获取统计值的方法用 count 做前缀。
  4. 插入的方法用 save/insert 做前缀。
  5. 删除的方法用 remove/delete 做前缀。
  6. 修改的方法用 update 做前缀。
- 领域模型命名规约
  1. 数据对象:xxxDO，xxx 即为数据表名。
  2. 数据传输对象:xxxDTO，xxx 为业务领域相关的名称。
  3. 展示对象:xxxVO，xxx 一般为网页名称。
  4. POJO 是 DO/DTO/BO/VO 的统称，禁止命名成 xxxPOJO。

5. 【强制】不允许任何魔法值(即未经预先定义的常量)直接出现在代码中。

```java 反例
    // 本例中，开发者 A 定义了缓存的 key，然后开发者 B 使用缓存时少了下划线，即 key 是"Id#taobao"+tradeId，导致 出现故障
    String key = "Id#taobao_" + tradeId;
    cache.put(key, value);
```

6. 【推荐】常量的复用层次有五层:跨应用共享常量、应用内共享常量、子工程内共享常量、包内共享常量、类内共享常量。

1) 跨应用共享常量: 放置在二方库中，通常是 client.jar 中的 constant 目录下。
2) 应用内共享常量: 放置在一方库中，通常是子模块中的 constant 目录下。
   反例: 易懂变量也要统一定义成应用内共享常量，两位工程师在两个类中分别定义了 "YES" 的变量:
   类 A 中: public static final String YES = "yes";
   类 B 中: public static final String YES = "y";
   A.YES.equals(B.YES)，预期是 true，但实际返回为 false，导致线上问题。
3) 子工程内部共享常量: 即在当前子工程的 constant 目录下。
4) 包内共享常量:即在当前包下单独的 constant 目录下。
5) 类内共享常量: 直接在类内部 private static final 定义。

7. 【强制】注释的双斜线与注释内容之间有且仅有一个空格。

```java 正例
    // 这是示例注释，请注意在双斜线之后有一个空格
    String commentString = new String();
```

8. 【强制】单行字符数限制不超过 120 个，超出需要换行，换行时遵循如下原则:

1) 第二行相对第一行缩进 4 个空格，从第三行开始，不再继续缩进，参考示例。
2) 运算符与下文一起换行。
3) 方法调用的点符号与下文一起换行。
4) 方法调用中的多个参数需要换行时，在逗号后进行。
5) 在括号前不要换行，见反例。

```java 正例
    StringBuilder sb = new StringBuilder();
    // 超过 120 个字符的情况下，换行缩进 4 个空格，并且方法前的点号一起换行
    sb.append("yang").append("hao")...
        .append("chen")...
        .append("chen")...
        .append("chen");
```

```java 反例
    StringBuilder sb = new StringBuilder();
    // 超过 120 个字符的情况下，不要在括号前换行
    sb.append("you").append("are")...append
        ("lucky");
    // 参数很多的方法调用可能超过 120 个字符，逗号后才是换行处
    method(args1, args2, args3, ...
        , argsX);
```

9. 【推荐】单个方法的总行数不超过 80 行。

- 说明:除注释之外的方法签名、左右大括号、方法内代码、空行、回车及任何不可见字符的总行数不超过 80 行。
- 正例:代码逻辑分清红花和绿叶，个性和共性，绿叶逻辑单独出来成为额外方法，使主干代码更加清晰；共性逻辑抽取成为共性方法，便于复用和维护。

10. 【推荐】不同逻辑、不同语义、不同业务的代码之间插入一个空行分隔开来以提升可读性。

- 说明:任何情形，没有必要插入多个空行进行隔开。

11. 【强制】Object 的 equals 方法容易抛空指针异常，应使用常量或确定有值的对象来调用 equals。

- 正例:"test".equals(object);
- 反例:object.equals("test");
- 说明:推荐使用 JDK7 引入的工具类 java.util.Objects#equals(Object a, Object b)

12. 【强制】所有整型包装类对象之间值的比较，全部使用 equals 方法比较。

- 说明:对于 Integer var = ? 在-128 至 127 之间的赋值，Integer 对象是在 IntegerCache.cache 产生， 会复用已有对象，这个区间内的 Integer 值可以直接使用==进行判断，但是这个区间之外的所有数据，都 会在堆上产生，并不会复用已有对象，这是一个大坑，推荐使用 equals 方法进行判断。

13. 关于基本数据类型与包装数据类型的使用标准如下:

1) 【强制】所有的 POJO 类属性必须使用包装数据类型。
2) 【强制】RPC 方法的返回值和参数必须使用包装数据类型。
3) 【推荐】所有的局部变量使用基本数据类型。

- 说明:POJO 类属性没有初值是提醒使用者在需要使用时，必须自己显式地进行赋值，任何 NPE 问题，或 者入库检查，都由使用者来保证。
- 正例:数据库的查询结果可能是 null，因为自动拆箱，用基本数据类型接收有 NPE 风险。 反例:某业务的交易报表上显示成交总额涨跌情况，即正负 x%，x 为基本数据类型，调用的 RPC 服务，调 用不成功时，返回的是默认值，页面显示为 0%，这是不合理的，应该显示成中划线-。所以包装数据类型 的 null 值，能够表示额外的信息，如:远程调用失败，异常退出。

14. 【推荐】当一个类有多个构造方法，或者多个同名方法，这些方法应该按顺序放置在一起，便于阅读，此条规则优先于下一条。

15. 【推荐】 类内方法定义的顺序依次是:公有方法或保护方法 > 私有方法 > getter / setter 方法。

- 说明:公有方法是类的调用者和维护者最关心的方法，首屏展示最好;保护方法虽然只是子类关心，也可 能是“模板设计模式”下的核心方法;而私有方法外部一般不需要特别关心，是一个黑盒实现;因为承载 的信息价值较低，所有 Service 和 DAO 的 getter/setter 方法放在类体最后。

16. 【强制】不允许在程序任何地方中使用:

1) java.sql.Date。
2) java.sql.Time。
3) java.sql.Timestamp。

- 说明: 第 1 个不记录时间，getHours()抛出异常;第 2 个不记录日期，getYear()抛出异常;第 3 个在构造 方法 super((time/1000)\*1000)，在 Timestamp 属性 fastTime 和 nanos 分别存储秒和纳秒信息。
- 反例: java.util.Date.after(Date)进行时间比较时，当入参是 java.sql.Timestamp 时，会触发 JDK BUG(JDK9 已修复)，可能导致比较时的意外结果。

17. 【强制】关于 hashCode 和 equals 的处理，遵循如下规则:

1) 只要覆写 equals，就必须覆写 hashCode。
2) 因为 Set 存储的是不重复的对象，依据 hashCode 和 equals 进行判断，所以 Set 存储的对象必须覆写 这两种方法。
3) 如果自定义对象作为 Map 的键，那么必须覆写 hashCode 和 equals。

- 说明: String 因为覆写了 hashCode 和 equals 方法，所以可以愉快地将 String 对象作为 key 来使用。

18. 【强制】判断所有集合内部的元素是否为空，使用 isEmpty()方法，而不是 size()==0 的方式。

- 说明:在某些集合中，前者的时间复杂度为 O(1)，而且可读性更好。

```java 正例
Map<String, Object> map = new HashMap<>(16); if(map.isEmpty()) {
System.out.println("no element in this map."); }
```

19. 【强制】在使用 java.util.stream.Collectors 类的 toMap()方法转为 Map 集合时，一定要使用含有参数类型为 BinaryOperator，参数名为 mergeFunction 的方法，否则当出现相同 key 值时会抛出 IllegalStateException 异常。

- 说明:参数 mergeFunction 的作用是当出现 key 重复时，自定义对 value 的处理策略。

```java 正例
    List<Pair<String, Double>> pairArrayList = new ArrayList<>(3);
    pairArrayList.add(new Pair<>("version", 12.10));
    pairArrayList.add(new Pair<>("version", 12.19));
    pairArrayList.add(new Pair<>("version", 6.28));
    Map<String, Double> map = pairArrayList.stream().collect(
        // 生成的 map 集合中只有一个键值对:{version=6.28}
        Collectors.toMap(Pair::getKey, Pair::getValue, (v1, v2) -> v2));
```

```java 反例
    String[] departments = new String[] {"iERP", "iERP", "EIBU"};
    // 抛出 IllegalStateException 异常
    Map<Integer, String> map = Arrays.stream(departments).collect(Collectors.toMap(String::hashCode, str -> str));
```

20. 【强制】在使用 java.util.stream.Collectors 类的 toMap()方法转为 Map 集合时，一定要注意当 value 为 null 时会抛 NPE 异常。

- 说明:在 java.util.HashMap 的 merge 方法里会进行如下的判断:

```java
if (value == null || remappingFunction == null)
    throw new NullPointerException();
```

```java 反例
    List<Pair<String, Double>> pairArrayList = new ArrayList<>(2);
    pairArrayList.add(new Pair<>("version1", 8.3));
    pairArrayList.add(new Pair<>("version2", null));
    Map<String, Double> map = pairArrayList.stream().collect(
    // 抛出 NullPointerException 异常
    Collectors.toMap(Pair::getKey, Pair::getValue, (v1, v2) -> v2));
```

21. 【强制】使用集合转数组的方法，必须使用集合的 toArray(T[] array)，传入的是类型完全一致、长度为 0 的空数组。

- 反例:直接使用 toArray 无参方法存在问题，此方法返回值只能是 Object[]类，若强转其它类型数组将出现 ClassCastException 错误。

```java 正例
List<String> list = new ArrayList<>(2);
list.add("guan");
list.add("bao");
String[] array = list.toArray(new String[0]);
```

- 说明:使用 toArray 带参方法，数组空间大小的 length:
  1. 等于 0，动态创建与 size 相同的数组，性能最好。
  2. 大于 0 但小于 size，重新创建大小等于 size 的数组，增加 GC 负担。
  3. 等于 size，在高并发情况下，数组创建完成之后，size 正在变大的情况下，负面影响与 2 相同。
  4. 大于 size，空间浪费，且在 size 处插入 null 值，存在 NPE 隐患。

22. 【强制】使用工具类 Arrays.asList()把数组转换成集合时，不能使用其修改集合相关的方法， 它的 add/remove/clear 方法会抛出 UnsupportedOperationException 异常。

- 说明: asList 的返回对象是一个 Arrays 内部类，并没有实现集合的修改方法。Arrays.asList 体现的是适配 器模式，只是转换接口，后台的数据仍是数组。

```java
String[] str = new String[] { "chen", "yang", "hao" };
List list = Arrays.asList(str);
```

- 第一种情况:list.add("yangguanbao"); 运行时异常。
- 第二种情况:str[0] = "change"; 也会随之修改，反之亦然。

23. 【强制】线程池不允许使用 Executors 去创建，而是通过 ThreadPoolExecutor 的方式，这 样的处理方式让写的同学更加明确线程池的运行规则，规避资源耗尽的风险。

- 说明:Executors 返回的线程池对象的弊端如下:

  1. FixedThreadPool 和 SingleThreadPool:
     允许的请求队列长度为 Integer.MAX_VALUE，可能会堆积大量的请求，从而导致 OOM。
  2. CachedThreadPool:
     允许的创建线程数量为 Integer.MAX_VALUE，可能会创建大量的线程，从而导致 OOM。

24. 【推荐】除常用方法(如 getXxx/isXxx)等外，不要在条件判断中执行其它复杂的语句，将复 杂逻辑判断的结果赋值给一个有意义的布尔变量名，以提高可读性。

- 说明: 很多 if 语句内的逻辑表达式相当复杂，与、或、取反混合运算，甚至各种方法纵深调用，理解成本 非常高。如果赋值一个非常好理解的布尔变量名字，则是件令人爽心悦目的事情。

```java 正例
    // 伪代码如下
    final boolean existed = (file.open(fileName, "w") != null) && (...) || (...);
    if (existed) {
    ... }
```

```java 反例
public final void acquire ( long arg) {
    if (!tryAcquire(arg) &&
        acquireQueued(addWaiter(Node.EXCLUSIVE), arg)) {
        selfInterrupt();
    }
```

25. 【推荐】循环体中的语句要考量性能，以下操作尽量移至循环体外处理，如定义对象、变量、 获取数据库连接，进行不必要的 try-catch 操作(这个 try-catch 是否可以移至循环体外)。

26. 【推荐】公开接口需要进行入参保护，尤其是批量操作的接口。

- 反例:某业务系统，提供一个用户批量查询的接口，API 文档上有说最多查多少个，但接口实现上没做任何保护，导致调用方传了一个 1000 的用户 id 数组过来后，查询信息后，内存爆了。

27. 【参考】下列情形，需要进行参数校验:

    1. 调用频次低的方法。
    2. 执行时间开销很大的方法。此情形中，参数校验时间几乎可以忽略不计，但如果因为参数错误导致中间执行回退，或者错误，那得不偿失。
    3. 需要极高稳定性和可用性的方法。
    4. 对外提供的开放接口，不管是 RPC/API/HTTP 接口。 5) 敏感权限入口。

28. 【参考】下列情形，不需要进行参数校验:

1) 极有可能被循环调用的方法。但在方法说明里必须注明外部参数检查。
2) 底层调用频度比较高的方法。毕竟是像纯净水过滤的最后一道，参数错误不太可能到底层才会暴露问题。一般 DAO 层与 Service 层都在同一个应用中，部署在同一台服务器中，所以 DAO 的参数校验，可以省略。
3) 被声明成 private 只会被自己代码所调用的方法，如果能够确定调用方法的代码传入参数已经做过检查或者肯定不会有问题，此时可以不校验参数。

29. 【强制】类、类属性、类方法的注释必须使用 Javadoc 规范，使用/\*_内容_/格式，不得使用 // xxx 方式。

- 说明:在 IDE 编辑窗口中，Javadoc 方式会提示相关注释，生成 Javadoc 可以正确输出相应注释;在 IDE 中，工程调用方法时，不进入方法即可悬浮提示方法、参数、返回值的意义，提高阅读效率。

30. 【强制】所有的抽象方法(包括接口中的方法)必须要用 Javadoc 注释、除了返回值、参数、 异常说明外，还必须指出该方法做什么事情，实现什么功能。

- 说明:对子类的实现要求，或者调用注意事项，请一并说明。

31. 【强制】方法内部单行注释，在被注释语句上方另起一行，使用//注释。方法内部多行注释使 用/\* \*/注释，注意与代码对齐。

32. 【强制】所有的枚举类型字段必须要有注释，说明每个数据项的用途。

33. 【推荐】与其“半吊子”英文来注释，不如用中文注释把问题说清楚。专有名词与关键字保持 英文原文即可。

- 反例: “TCP 连接超时”解释成“传输控制协议连接超时”，理解反而费脑筋。

34. 【推荐】代码修改的同时，注释也要进行相应的修改，尤其是参数、返回值、异常、核心逻辑 等的修改。

- 说明:代码与注释更新不同步，就像路网与导航软件更新不同步一样，如果导航软件严重滞后，就失去了导航的意义。

35. 【推荐】在类中删除未使用的任何字段、方法、内部类;在方法中删除未使用的任何参数声明 与内部变量。

36. 【参考】好的命名、代码结构是自解释的，注释力求精简准确、表达到位。避免出现注释的一个极端:过多过滥的注释，代码的逻辑一旦修改，修改注释又是相当大的负担。

```java 反例
    // put elephant into fridge
    put(elephant, fridge);
```

方法名 put，加上两个有意义的变量名 elephant 和 fridge，已经说明了这是在干什么，语义清晰的代码不需要额外的注释。

37. 【参考】特殊注释标记，请注明标记人与标记时间。注意及时处理这些标记，通过标记扫描， 经常清理此类标记。线上故障有时候就是来源于这些标记处的代码。

    1. 待办事宜(TODO):(标记人，标记时间，[预计处理时间])  
       表示需要实现，但目前还未实现的功能。这实际上是一个 Javadoc 的标签，目前的 Javadoc 还没有实现，但已经被广泛使用。只能应用于类，接口和方法(因为它是一个 Javadoc 标签)。
    2. 错误，不能工作(FIXME):(标记人，标记时间，[预计处理时间])
       在注释中用 FIXME 标记某代码是错误的，而且不能工作，需要及时纠正的情况。

38. 【强制】前后端数据列表相关的接口返回，如果为空，则返回空数组[]或空集合{}。

- 说明:此条约定有利于数据层面上的协作更加高效，减少前端很多琐碎的 null 判断。

39. 【强制】对于需要使用超大整数的场景，服务端一律使用 String 字符串类型返回，禁止使用 Long 类型。
    说明:Java 服务端如果直接返回 Long 整型数据给前端，JS 会自动转换为 Number 类型(注:此类型为双 精度浮点数，表示原理与取值范围等同于 Java 中的 Double)。Long 类型能表示的最大值是 2 的 63 次方 -1，在取值范围之内，超过 2 的 53 次方 (9007199254740992)的数值转化为 JS 的 Number 时，有些数值会有精度损失。扩展说明，在 Long 取值范围内，任何 2 的指数次整数都是绝对不会存在精度损失的，所 以说精度损失是一个概率问题。若浮点数尾数位与指数位空间不限，则可以精确表示任何整数，但很不幸， 双精度浮点数的尾数位只有 52 位。

- 反例: 通常在订单号或交易号大于等于 16 位，大概率会出现前后端单据不一致的情况，比如，"orderId": 362909601374617692，前端拿到的值却是: 362909601374617660。

40. 【强制】HTTP 请求通过 body 传递内容时，必须控制长度，超出最大长度后，后端解析会出错。

- 说明: nginx 默认限制是 1MB，tomcat 默认限制为 2MB，当确实有业务需要传较大内容时，可以通过调大服务器端的限制。

41. 【强制】在翻页场景中，用户输入参数的小于 1，则前端返回第一页参数给后端；后端发现用户输入的参数大于总页数，直接返回最后一页。

42. 【推荐】服务器返回信息必须被标记是否可以缓存，如果缓存，客户端可能会重用之前的请求结果。

- 说明: 缓存有利于减少交互次数，减少交互的平均延迟。
- 正例: http 1.1 中，s-maxage 告诉服务器进行缓存，时间单位为秒，用法如下

```java
    response.setHeader("Cache-Control", "s-maxage=" + cacheSeconds);
```

43. 【推荐】前后端的时间格式统一为"yyyy-MM-dd HH:mm:ss"，统一为 GMT。

44. 【参考】在接口路径中不要加入版本号，版本控制在 HTTP 头信息中体现，有利于向前兼容。

- 说明:当用户在低版本与高版本之间反复切换工作时，会导致迁移复杂度升高，存在数据错乱风险。

45. 【强制】避免用 ApacheBeanutils 进行属性的 copy。

- 说明: Apache BeanUtils 性能较差，可以使用其他方案比如 Spring BeanUtils, Cglib BeanCopier，注意 均是浅拷贝。

46. 【推荐】及时清理不再使用的代码段或配置信息。

- 说明: 对于垃圾代码或过时配置，坚决清理干净，避免程序过度臃肿，代码冗余。
- 正例: 对于暂时被注释掉，后续可能恢复使用的代码片断，在注释代码上方，统一规定使用三个斜杠(///) 来说明注释掉代码的理由。如:

```java
public static void hello() {
    /// 业务方通知活动暂停
    // Business business = new Business();
    // business.active();
    System.out.println("it's finished");
}
```

## 异常日志

1. 【强制】Java 类库中定义的可以通过预检查方式规避的 RuntimeException 异常不应该通过 catch 的方式来处理，比如:NullPointerException，IndexOutOfBoundsException 等等。

- 说明:无法通过预检查的异常除外，比如，在解析字符串形式的数字时，可能存在数字格式错误，不得不通过 catch NumberFormatException 来实现。

```java
    // 正例
    if (obj != null) {...}
    // 反例
    try { obj.method(); } catch (NullPointerException e) {...}
```

2. 【强制】catch 时请分清稳定代码和非稳定代码，稳定代码指的是无论如何不会出错的代码。 对于非稳定代码的 catch 尽可能进行区分异常类型，再做对应的异常处理。 说明:对大段代码进行 try-catch，使程序无法根据不同的异常做出正确的应激反应，也不利于定位问题，这是一种不负责任的表现。

- 正例:用户注册的场景中，如果用户输入非法字符，或用户名称已存在，或用户输入密码过于简单，在程序上作出分门别类的判断，并提示给用户。

3. 【强制】捕获异常是为了处理它，不要捕获了却什么都不处理而抛弃之，如果不想处理它，请 将该异常抛给它的调用者。最外层的业务使用者，必须处理异常，将其转化为用户可以理解的内容。

4. 【强制】不要在 finally 块中使用 return。

- 说明: try 块中的 return 语句执行成功后，并不马上返回，而是继续执行 finally 块中的语句，如果此处存在 return 语句，则在此直接返回，无情丢弃掉 try 块中的返回点。

```java 反例
private int x = 0;
public int checkReturn() {
    try {
        // x 等于 1，此处不返回
        return ++x; } finally {
        // 返回的结果是 2
        return ++x;
    }
}
```

5. 【强制】在调用 RPC、二方包、或动态生成类的相关方法时，捕捉异常必须使用 Throwable 类来进行拦截。

- 说明: 通过反射机制来调用方法，如果找不到方法，抛出 NoSuchMethodException。什么情况会抛出 NoSuchMethodError 呢?二方包在类冲突时，仲裁机制可能导致引入非预期的版本使类的方法签名不匹配，或者在字节码修改框架(比如:ASM)动态创建或修改类时，修改了相应的方法签名。这些情况，即使代码编译期是正确的，但在代码运行期时，会抛出 NoSuchMethodError。

6. 【推荐】方法的返回值可以为 null，不强制返回空集合，或者空对象等，必须添加注释充分说 明什么情况下会返回 null 值。

- 说明: 本手册明确防止 NPE 是调用者的责任。即使被调用方法返回空集合或者空对象，对调用者来说，也 并非高枕无忧，必须考虑到远程调用失败、序列化失败、运行时异常等场景返回 null 的情况。

7. 【推荐】防止 NPE，是程序员的基本修养，注意 NPE 产生的场景:

   1. 返回类型为基本数据类型，return 包装数据类型的对象时，自动拆箱有可能产生 NPE。
      - 反例: public int f() { return Integer 对象}， 如果为 null，自动解箱抛 NPE。
   2. 数据库的查询结果可能为 null。
   3. 集合里的元素即使 isNotEmpty，取出的数据元素也可能为 null。
   4. 远程调用返回对象时，一律要求进行空指针判断，防止 NPE。
   5. 对于 Session 中获取的数据，建议进行 NPE 检查，避免空指针。
   6. 级联调用 obj.getA().getB().getC();一连串调用，易产生 NPE。 正例:使用 JDK8 的 Optional 类来防止 NPE 问题。

8. 【推荐】定义异常时区分 unchecked / checked 异常，避免直接抛出 new RuntimeException()， 更不允许抛出 Exception 或者 Throwable，应使用有业务含义的自定义异常。推荐业界已定 义过的自定义异常，如: DAOException / ServiceException 等。

9. 【强制】应用中不可直接使用日志系统(Log4j、Logback)中的 API，而应依赖使用日志框架 (SLF4J、JCL--Jakarta Commons Logging)中的 API，使用门面模式的日志框架，有利于维护和 各个类的日志处理方式统一。

- 说明: 日志框架(SLF4J、JCL--Jakarta Commons Logging)的使用方式(推荐使用 SLF4J)

```java
// 使用 SLF4J
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
private static final Logger logger = LoggerFactory.getLogger(Test.class);
// 使用 JCL:
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
private static final Log log = LogFactory.getLog(Test.class);
```

10. 【强制】在日志输出时，字符串变量之间的拼接使用占位符的方式。

- 说明: 因为 String 字符串的拼接会使用 StringBuilder 的 append()方式，有一定的性能损耗。使用占位符仅 是替换动作，可以有效提升性能。
- 正例: logger.debug("Processing trade with id: {} and symbol: {}", id, symbol);

11. 【强制】生产环境禁止直接使用 System.out 或 System.err 输出日志或使用 e.printStackTrace()打印异常堆栈。

- 说明: 标准日志输出与标准错误输出文件每次 Jboss 重启时才滚动，如果大量输出送往这两个文件，容易造成文件大小超过操作系统大小限制。

12. 【强制】异常信息应该包括两类信息:案发现场信息和异常堆栈信息。如果不处理，那么通过 关键字 throws 往上抛出。

- 正例: logger.error("inputParams:{} and errorMessage:{}", 各类参数或者对象 toString(), e.getMessage(), e);

13. 【强制】日志打印时禁止直接用 JSON 工具将对象转换成 String。

- 说明: 如果对象里某些 get 方法被覆写，存在抛出异常的情况，则可能会因为打印日志而影响正常业务流 程的执行。
- 正例: 打印日志时仅打印出业务相关属性值或者调用其对象的 toString()方法。

14. 【推荐】谨慎地记录日志。生产环境禁止输出 debug 日志;有选择地输出 info 日志;如果使用 warn 来记录刚上线时的业务行为信息，一定要注意日志输出量的问题，避免把服务器磁盘撑 爆，并记得及时删除这些观察日志。

- 说明: 大量地输出无效日志，不利于系统性能提升，也不利于快速定位错误点。记录日志时请思考:这些 日志真的有人看吗?看到这条日志你能做什么?能不能给问题排查带来好处?

15. 【推荐】可以使用 warn 日志级别来记录用户输入参数错误的情况，避免用户投诉时，无所适从。如非必要，请不要在此场景打出 error 级别，避免频繁报警。

- 说明: 注意日志输出的级别，error 级别只记录系统逻辑出错、异常或者重要的错误信息。

## 单元测试

1. 【推荐】单元测试的基本目标:语句覆盖率达到 70%;核心模块的语句覆盖率和分支覆盖率都要达到 100%

- 说明: 在工程规约的应用分层中提到的 DAO 层，Manager 层，可重用度高的 Service，都应该进行单元测试。

2. 【推荐】编写单元测试代码遵守 BCDE 原则，以保证被测试模块的交付质量。

- B: Border，边界值测试，包括循环边界、特殊取值、特殊时间点、数据顺序等。
- C: Correct，正确的输入，并得到预期的结果。
- D: Design，与设计文档相结合，来编写单元测试。
- E: Error，强制错误信息输入(如:非法数据、异常流程、业务允许外等)，并得到预期的结果。

3. 【推荐】和数据库相关的单元测试，可以设定自动回滚机制，不给数据库造成脏数据。或者对单元测试产生的数据有明确的前后缀标识。

- 正例: 在阿里巴巴企业智能事业部的内部单元测试中，使用 ENTERPRISE*INTELLIGENCE \_UNIT_TEST* 的前缀来标识单元测试相关代码。

## 安全规约

1. 【强制】用户输入的 SQL 参数严格使用参数绑定或者 METADATA 字段值限定，防止 SQL 注入， 禁止字符串拼接 SQL 访问数据库。

- 反例: 某系统签名大量被恶意修改，即是因为对于危险字符 # --没有进行转义，导致数据库更新时，where 后边的信息被注释掉，对全库进行更新。

2. 【强制】用户请求传入的任何参数必须做有效性验证。

- 说明:忽略参数校验可能导致:
  - page size 过大导致内存溢出
  - 恶意 order by 导致数据库慢查询
  - 缓存击穿
  - SSRF
  - 任意重定向
  - SQL 注入，Shell 注入，反序列化注入
  - 正则输入源串拒绝服务 ReDoS
- Java 代码用正则来验证客户端的输入，有些正则写法验证普通用户输入没有问题，但是如果攻击人员使用 的是特殊构造的字符串来验证，有可能导致死循环的结果。

## 数据库

1. 【强制】表达是与否概念的字段，必须使用 is_xxx 的方式命名，数据类型是 unsigned tinyint(1 表示是，0 表示否)。

- 说明: 任何字段如果为非负数，必须是 unsigned。
- 注意: POJO 类中的任何布尔类型的变量，都不要加 is 前缀，所以，需要在 <rsultMap> 设置从 is_xxx 到 Xxx 的映射关系。数据库表示是与否的值，使用 tinyint 类型，坚持 is_xxx 对命名方式是为了明确其取值含义与取值范围。
- 正例: 表达逻辑删除的字段名 is_deleted，1 表示删除，0 表示未删除。

2. 【强制】表名不使用复数名词。 说明:表名应该仅仅表示表里面的实体内容，不应该表示实体数量，对应于 DO 类名也是单数形式，符合 表达习惯。

3. 【强制】主键索引名为 pk\_ 字段名；唯一索引名为 uk\_ 字段名；普通索引名则为 idx\_ 字段名。

- 说明: pk\_ 即 primary key; uk\_ 即 unique key; idx\_ 即 index 的简称。

4. 【强制】小数类型为 decimal，禁止使用 float 和 double。

- 说明: 在存储的时候，float 和 double 都存在精度损失的问题，很可能在比较值的时候，得到不正确的 结果。如果存储的数据范围超过 decimal 的范围，建议将数据拆成整数和小数并分开存储。

5. 【强制】表必备三字段: id, create_time, update_time。

- 说明: 其中 id 必为主键，类型为 bigint unsigned、单表时自增、步长为 1。create_time, update_time 的类型均为 datetime 类型，前者现在时表示主动式创建，后者过去分词表示被动式更新。

6. 【强制】业务上具有唯一特性的字段，即使是组合字段，也必须建成唯一索引。

- 说明: 不要以为唯一索引影响了 insert 速度，这个速度损耗可以忽略，但提高查找速度是明显的;另外， 即使在应用层做了非常完善的校验控制，只要没有唯一索引，根据墨菲定律，必然有脏数据产生。

7. 【强制】超过三个表禁止 join。需要 join 的字段，数据类型保持绝对一致;多表关联查询时， 保证被关联的字段需要有索引。

- 说明: 即使双表 join 也要注意表索引、SQL 性能。

8. 【推荐】利用延迟关联或者子查询优化超多分页场景。

- 说明: MySQL 并不是跳过 offset 行，而是取 offset+N 行，然后返回放弃前 offset 行，返回 N 行，那当 offset 特别大的时候，效率就非常的低下，要么控制返回的总页数，要么对超过特定阈值的页数进行 SQL 改写。

```sql
-- 正例: 先快速定位需要获取的 id 段，然后再关联
SELECT t1.* FROM 表 1 as t1, (select id from 表 1 where 条件 LIMIT 100000,20 ) as t2 where t1.id=t2.id
```

9. 【推荐】in 操作能避免则避免，若实在避免不了，需要仔细评估 in 后边的集合元素数量，控 制在 1000 个之内。

10. 【强制】iBATIS 自带的 queryForList(String statementName,int start,int size)不推荐使用。 说明:其实现方式是在数据库取到 statementName 对应的 SQL 语句的所有记录，再通过 subList 取 start,size 的子集合。

```java 正例
Map<String, Object> map = new HashMap<>(16);
map.put("start", start);
map.put("size", size);
```

11. 【强制】更新数据表记录时，必须同时更新记录对应的 update_time 字段值为当前时间。

12. 【参考】@Transactional 事务不要滥用。事务会影响数据库的 QPS，另外使用事务的地方需 要考虑各方面的回滚方案，包括缓存回滚、搜索引擎回滚、消息补偿、统计修正等。

## 工程结构

1. 【参考】(分层异常处理规约)在 DAO 层，产生的异常类型有很多，无法用细粒度的异常进 行 catch，使用 catch(Exception e)方式，并 throw new DAOException(e)，不需要打印日志，因 为日志在 Manager/Service 层一定需要捕获并打印到日志文件中去，如果同台服务器再打日志，浪费性能和存储。在 Service 层出现异常时，必须记录出错日志到磁盘，尽可能带上参数信息， 相当于保护案发现场。Manager 层与 Service 同机部署，日志方式与 DAO 层处理一致，如果是 单独部署，则采用与 Service 一致的处理方式。Web 层绝不应该继续往上抛异常，因为已经处 于顶层，如果意识到这个异常将导致页面无法正常渲染，那么就应该直接跳转到友好错误页面， 尽量加上友好的错误提示信息。开放接口层要将异常处理成错误码和错误信息方式返回。

2. 【参考】分层领域模型规约:

- DO(Data Object):此对象与数据库表结构一一对应，通过 DAO 层向上传输数据源对象。
- DTO(Data Transfer Object):数据传输对象，Service 或 Manager 向外传输的对象。
- BO(Business Object):业务对象，可以由 Service 层输出的封装业务逻辑的对象。
- Query:数据查询对象，各层接收上层的查询请求。注意超过 2 个参数的查询封装，禁止使用 Map 类 来传输。
- VO(View Object):显示层对象，通常是 Web 向模板渲染引擎层传输的对象。

3. 【强制】二方库版本号命名方式:主版本号.次版本号.修订号
   1. 主版本号:产品方向改变，或者大规模 API 不兼容，或者架构不兼容升级。
   2. 次版本号:保持相对兼容性，增加主要功能特性，影响范围极小的 API 不兼容修改。
   3. 修订号:保持完全兼容性，修复 BUG、新增次要功能特性等。

- 说明: 注意起始版本号必须为:1.0.0，而不是 0.0.1。
- 反例: 仓库内某二方库版本号从 1.0.0.0 开始，一直默默“升级”成 1.0.0.64，完全失去版本的语义信息。

4. 【强制】二方库里可以定义枚举类型，参数可以使用枚举类型，但是接口返回值不允许使用枚 举类型或者包含枚举类型的 POJO 对象。

5. 【参考】为避免应用二方库的依赖冲突问题，二方库发布者应当遵循以下原则:

   1. 精简可控原则。移除一切不必要的 API 和依赖，只包含 Service API、必要的领域模型对象、Utils 类、 常量、枚举等。如果依赖其它二方库，尽量是 provided 引入，让二方库使用者去依赖具体版本号;无 log 具体实现，只依赖日志框架。
   2. 稳定可追溯原则。每个版本的变化应该被记录，二方库由谁维护，源码在哪里，都需要能方便查到。除 非用户主动升级版本，否则公共二方库的行为不应该发生变化。

6. 【推荐】给 JVM 环境参数设置-XX:+HeapDumpOnOutOfMemoryError 参数，让 JVM 碰到 OOM 场景时输出 dump 信息。

- 说明: OOM 的发生是有概率的，甚至相隔数月才出现一例，出错时的堆内信息对解决问题非常有帮助。

7. 【推荐】在线上生产环境，JVM 的 Xms 和 Xmx 设置一样大小的内存容量，避免在 GC 后调整 堆大小带来的压力。

## 设计规约

1. 【推荐】系统设计阶段，共性业务或公共行为抽取出来公共模块、公共配置、公共类、公共方法等，在系统中不出现重复代码的情况，即 DRY 原则(Don't Repeat Yourself)。

- 说明: 随着代码的重复次数不断增加，维护成本指数级上升。随意复制和粘贴代码，必然会导致代码的重复，在维护代码时，需要修改所有的副本，容易遗漏。必要时抽取共性方法，或者抽象公共类，甚至是组件化。
- 正例: 一个类中有多个 public 方法，都需要进行数行相同的参数校验操作，这个时候请抽取:

```java
private boolean checkParam(DTO dto) {...}
```

2. 【推荐】类在设计与实现时要符合单一原则。

- 说明: 单一原则最易理解却是最难实现的一条规则，随着系统演进，很多时候，忘记了类设计的初衷。

3. 【推荐】系统设计阶段，注意对扩展开放，对修改闭合。

- 说明: 极端情况下，交付的代码是不可修改的，同一业务域内的需求变化，通过模块或类的扩展来实现。

4. 【推荐】谨慎使用继承的方式来进行扩展，优先使用聚合/组合的方式来实现。

- 说明: 不得已使用继承的话，必须符合里氏代换原则，此原则说父类能够出现的地方子类一定能够出现，比如，“把钱交出来”，钱的子类美元、欧元、人民币等都可以出现。

5. 迪米特法则，最少知识原则

- 说明: 尽可能点少知道其它类，目的在于降低耦合，减少类之间的依赖关系（Low of demeter）

6. 【推荐】系统设计阶段，根据依赖倒置原则，尽量依赖抽象类与接口，有利于扩展与维护。

- 说明: 低层次模块依赖于高层次模块的抽象，方便系统间的解耦。

7. 接口隔离原则，实现最小接口，使接口类不包括多余的方法，子类不用实现用不上的方法。
