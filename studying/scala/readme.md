# 问题

1. 执行 scala HelloScala 报错：

```shell
No such file or class on classpath: HelloScala
```

2. Error:scalac: bad option: '-make:transitive'

```
删除 .idea/scala_compiler.xml 中的
<parameter value="-make:transitive" />
```

3. idea 查看源码

```
Shift + Ctrl + n 按类查找
```

4. '\_' 转换匿名函数时成对出现

5. '\_' 导致 '+' 运算失败，歧义

```scala
val b = List((3, 1), (2, 1))
b.reduce((t1, t2) => t1._2+t2._2)

b.map(t=>List(t._1, t._2)) 
// 无法转为 b.map(List(_._1, _._2))
```
