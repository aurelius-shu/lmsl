<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [一、Python 简介](#一-python-简介)
- [二、安装 Python](#二-安装-python)
  - [Python 解释器](#python-解释器)
- [三、第一个 Python 程序](#三-第一个-python-程序)
  - [输入和输出](#输入和输出)
- [四、Python 基础](#四-python-基础)
  - [数据类型和变量](#数据类型和变量)
    - [数据类型](#数据类型)
    - [变量](#变量)
  - [字符串和编码](#字符串和编码)
    - [字符编码](#字符编码)
    - [Python 的字符串](#python-的字符串)
    - [格式化](#格式化)
  - [使用 list 和 tuple](#使用-list-和-tuple)
    - [list](#list)
    - [tuple](#tuple)
  - [条件判断](#条件判断)
  - [循环](#循环)
  - [使用 dict 和 set](#使用-dict-和-set)
    - [dict](#dict)
    - [set](#set)
    - [不可变对象](#不可变对象)
- [五、函数](#五-函数)
  - [调用函数](#调用函数)
    - [数据类型转换](#数据类型转换)
  - [定义函数](#定义函数)
    - [定义函数](#定义函数-1)
    - [空函数](#空函数)
    - [参数检查](#参数检查)
    - [返回多个值](#返回多个值)
    - [开平方](#开平方)
  - [函数的参数](#函数的参数)
  - [递归函数](#递归函数)
- [六、高级特性](#六-高级特性)
  - [切片](#切片)
  - [迭代](#迭代)
  - [列表生产式](#列表生产式)
  - [生成器](#生成器)
  - [迭代器](#迭代器)
- [七、函数式编程](#七-函数式编程)
  - [高阶函数](#高阶函数)
    - [map/reduce](#mapreduce)
    - [filter](#filter)
    - [sorted](#sorted)
  - [返回函数](#返回函数)
  - [匿名函数](#匿名函数)
  - [装饰器](#装饰器)
  - [偏函数](#偏函数)
- [八、模块](#八-模块)
  - [使用模块](#使用模块)
    - [作用域](#作用域)
  - [安装第三方模块](#安装第三方模块)
    - [模块搜索路径](#模块搜索路径)
- [九、面向对象编程](#九-面向对象编程)
  - [类和实例](#类和实例)
    - [数据封装](#数据封装)
  - [访问限制](#访问限制)
  - [继承和多态](#继承和多态)
  - [获取对象信息](#获取对象信息)
    - [type()](#type)
    - [isinstance()](#isinstance)
    - [dir()](#dir)
  - [实例属性和类属性](#实例属性和类属性)
- [十、面向对象高级编程](#十-面向对象高级编程)
  - [\_\_slots\_\_](#__slots__)
  - [@property](#property)
  - [多重继承](#多重继承)
  - [定制类](#定制类)
    - [\_\_str\_\_](#__str__)
    - [\_\_repr\_\_](#__repr__)
    - [\_\_iter\_\_](#__iter__)
    - [\_\_getitem\_\_](#__getitem__)
    - [\_\_getattr\_\_](#__getattr__)
    - [\_\_call\_\_](#__call__)
  - [枚举类](#枚举类)
  - [元类](#元类)
    - [type](#type-1)
    - [metaclass](#metaclass)
- [十一、错误、调试和测试](#十一-错误-调试和测试)
  - [错误处理](#错误处理)
  - [debug](#debug)
    - [assert](#assert)
    - [logging](#logging)
    - [pdb](#pdb)
    - [IDE](#ide)
  - [unittest](#unittest)
    - [编写](#编写)
    - [运行](#运行)
    - [setUp 与 tearDown](#setup-与-teardown)
  - [doctest](#doctest)
- [十二、IO 编程](#十二-io-编程)
  - [文件读写](#文件读写)
    - [读文件](#读文件)
    - [写文件](#写文件)
  - [StringIO 和 BytesIO](#stringio-和-bytesio)
    - [StringIO](#stringio)
    - [BytesIO](#bytesio)
  - [操作文件和目录](#操作文件和目录)
    - [环境变量](#环境变量)
    - [操作文件和目录](#操作文件和目录-1)
  - [序列化](#序列化)
    - [Pickle](#pickle)
    - [JSON](#json)
    - [JSON 进阶](#json-进阶)
- [十三、进程与线程](#十三-进程与线程)
  - [多进程](#多进程)
    - [multiprocessing](#multiprocessing)
    - [Pool](#pool)
    - [subprocess](#subprocess)
    - [进程间通行](#进程间通行)
  - [多线程](#多线程)
    - [Lock](#lock)
    - [GIL](#gil)
  - [ThreadLocal](#threadlocal)
  - [进程 vs. 线程](#进程-vs-线程)
    - [线程切换](#线程切换)
    - [计算密集型 vs. IO 密集型](#计算密集型-vs-io-密集型)
    - [异步 IO](#异步-io)
  - [分布式进程](#分布式进程)
- [十四、正则表达式](#十四-正则表达式)
  - [进阶](#进阶)
  - [re 模块](#re-模块)
    - [match](#match)
    - [split](#split)
    - [group](#group)
    - [贪婪匹配](#贪婪匹配)
    - [编译](#编译)
- [十五、常用内建模块](#十五-常用内建模块)
  - [datetime](#datetime)
  - [colections](#colections)
    - [namedtuple()](#namedtuple)
    - [deque](#deque)
    - [defaultdict](#defaultdict)
    - [OrderedDict](#ordereddict)
    - [ChainMap](#chainmap)
    - [Counter](#counter)
  - [base64](#base64)
  - [struct](#struct)
  - [hashlib](#hashlib)
    - [摘要算法](#摘要算法)
    - [摘要的应用](#摘要的应用)
  - [hmac](#hmac)
  - [itertools](#itertools)
  - [contextlib](#contextlib)
    - [\_\_enter\_\_ 和 \_\_exit\_\_](#__enter__-和-__exit__)
    - [@contextmanager](#contextmanager)
    - [closing](#closing)
  - [urllib](#urllib)
    - [GET](#get)
    - [POST](#post)
    - [Handler](#handler)
  - [XML](#xml)
    - [DOM](#dom)
    - [SAX](#sax)
  - [HTMLParser](#htmlparser)
- [十六、常用第三方模块](#十六-常用第三方模块)
  - [Pillow](#pillow)
  - [requests](#requests)
  - [chardet](#chardet)
  - [psutil](#psutil)
- [十七、virtualenv](#十七-virtualenv)
- [十八、图形界面](#十八-图形界面)
  - [Tkinter](#tkinter)
  - [turtle](#turtle)
- [十九、网络编程](#十九-网络编程)
  - [TCP/IP 简介](#tcpip-简介)
  - [TCP 编程](#tcp-编程)
    - [服务端](#服务端)
    - [客户端](#客户端)
  - [UDP 编程](#udp-编程)
    - [服务端](#服务端-1)
    - [客户端](#客户端-1)
- [todo:](#todo)

<!-- /code_chunk_output -->

# 一、Python 简介

**简介**

- 1. 高级编程语言，解释型语言
- 2. 代码在执行时会逐行翻译成 CPU 能理解的机器码
- 3. 代码精简，但运行速度慢
- 4. 基础代码库丰富，还有大量第三方库
- 5. 代码不能加密

**用途**

- 1. 网络应用
- 2. 工具软件
- 3. 包装其他语言开发程序

# 二、安装 Python

## Python 解释器

| 解释器     | 说明                                                                               |
| ---------- | ---------------------------------------------------------------------------------- |
| CPython    | 用 C 语言开发                                                                      |
| IPython    | 基于 CPython 之上的一个交互式解释器，只是在交互方式上有所增强，以 In[n] 作为提示符 |
| PyPy       | 采用 JIT 技术对 Python 代码进行动态编译（不是解释），提高执行速度                  |
| Jython     | 运行在 Java 平台的 Python 解释器，可以把 Python 代码编译成 Java 字节码执行         |
| IronPython | 与 Jython 类似，运行在 .Net 平台的 Python 解释器，编译成 .Net 字节码               |

```html
与 Java 和 .Net 平台交互最好的办法不是使用 Jython 和
IronPython，而是通过网络条用来交互，确保各程序之间的独立性。
```

# 三、第一个 Python 程序

**命令行模式**

- Windows 的 CMD、PowerShell（提示符是 C:\>）
- Linux 的 Terminal（提示符是 [aurelius@centos-dev ~]\$）

**Python 交互模式**

- 在命令行模式键入 python，即进入 Python 交互模式（提示符是 >>>）,输入 exit() 退出

**命令行模式和 Python 交互模式**

- 执行 .py 文件只能在命令行模式执行： python hello.py
- python 交互模式会输出每一行执行的结果，命令模式不会

**直接运行 .py 文件(仅限 Mac 和 Linux)**

- 通过 .py 文件首行特殊注释指定执行的 python 解释器

```python
#!usr/bin/env python3
print('hello world.')
```

- 通过如下命令给 hello.py 添加执行权限

```shell
chmod a+x hello.py
```

## 输入和输出

- 输出 print(), 遇到逗号 “,” 会输出空格
- 输入 input(), 入参会被打印出来

# 四、Python 基础

**基础语法**

- ”#“ 开头的是注释
- 每一行是一个语句，当语句以冒号 “:” 结尾时，缩进的语句被视为代码块

  > 好处：强迫代码格式化，强迫少用缩进
  > 坏处：“复制-粘贴”失效，无法自动格式化

## 数据类型和变量

### 数据类型

| 类型   | 精度     | 大小       | 说明                                                                                                                       |
| ------ | -------- | ---------- | -------------------------------------------------------------------------------------------------------------------------- |
| 整型   | 精确     | 无大小限制 | 十六进制，以 0x 为前缀，由 0-9，a-f 表示，允许数字中间以 ‘\_’ 分隔，入 10_000_000(同 10000000)，0xa1b2_c3d4(同 0xa1b2c3d4) |
| 浮点型 | 四舍五入 | 无大小限制 | inf(无限大)，科学计数法，把 10 用 e 替代，1.23e9                                                                           |
| 字符串 | -        | -          | r'' 表示''内部的字符串默认不转义，'''...''' 的格式表示多行内容                                                             |
| 布尔   | -        | -          | 可以用 and, or, not 运算                                                                                                   |
| 空值   | -        | -          | None                                                                                                                       |

**整数除法**

| 运算符 | 说明                           |
| ------ | ------------------------------ |
| /      | 结果是精确的商，永远是浮点数   |
| //     | 结果是商的整数部分，永远是整数 |
| %      | 结果是余数部分，永远是整数     |

### 变量

```html
必须是大小写英文，数字和 ‘_’ 组合，并且不以数字开头；
可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量
```

变量在计算机内存中的表示，如下

```python
a = 'ABC'
```

Python 解释器干了两件事情：

1. 在内存中创建了一个'ABC'的字符串；
2. 在内存中创建了一个名为 a 的变量，并把它指向'ABC'。

`变量本身类型不变的计算机编程语言为动态语言`

**常量**

常量就是不能变的变量，Python 通常用全部大写的变量名表示常量，Python 不强制常量无法修改

## 字符串和编码

### 字符编码

- 8 比特(bit)为一个字节(byte)，最大表示 2<sup>8</sup>-1 =255
- ASCII 码有 127 个字符
- Unicode 把所有语言都统一到一套编码里
- UTF-8 把 Unicode 字符根据不同的数字大小编码成 1-6 个字节（常用英文字符编码成 1 个字节，汉字通常是 3 个字节，很生僻字才编码成 4-6 字节）
- ASCII 可以看作 UTF-8 的一部分
- 计算机内存统一使用 Unicode，当需要保存到磁盘或传输时，转为通用 UTF-8s

### Python 的字符串

- ord() 可以获取字符的整数表示
- chr() 把编码转成对应的字符
- len() 参数是 str 时表示字符数，参数是 list 时表示元素个数，参数是 bytes 时表示字节数

**编码与解码**
`encode() 将 str 编码成指定的 bytes`

```python
>>> 'ABC'.encode('ascii')
b'ABC'
>>> '中文'.encode('utf-8')
b'\xe4\xb8\xad\xe6\x96\x87'
```

`decode() 将指定 bytes 解码为 str`

```python
# errors='ignore' 忽略错误的字节
>>> b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
'中'
```

### 格式化

**占位符**
| 占位符 | 替换内容 | 说明 |
| - | - | - |
| %d | 整数 | 用空位或 0 补长，`'%2d-%02d' % (3, 1)` => ` 3-01` |
| %f| 浮点数| 保留小数位数，`'%.2f' % 3.1415926` => `3.14`
| %s | 字符串|
| %x| 十六进制整数|

`format() 用传入的参数依次替换字符串内的占位符 {0}, {1}...`

```python
>>> 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
'Hello, 小明, 成绩提升了 17.1%'
```

`f-string 字符串包含 {xxx}，就会以 xxx 变量来替换`

```python
>>> r = 2.5
>>> s = 3.14 * r ** 2
>>> print(f'The area of a circle with radius {r} is {s:.2f}')
The area of a circle with radius 2.5 is 19.62
```

## 使用 list 和 tuple

### list

一种有序的集合，可以随时添加或删除其中的元素，元素的类型可以不同

| 方法   | 说明                                                                                                |
| ------ | --------------------------------------------------------------------------------------------------- |
| []     | 索引，listA[0]：获取第一个元素；listA[-1]：获取最后一个元素；listA[1] = 'C'：把第二个元素替换为 'C' |
| append | 追加，listA.append('A')：在末尾最佳一个 'A'                                                         |
| insert | listA.insert(1, 'B')：在第一个元素后面插入一个 'B'                                                  |
| pop    | listA.pop()：删除末尾；pop(1)：删除第二个元素                                                       |

**赋值语句不能与这些方法同用**

```python
>>> listB = listA.append('A')
>>> print(listB)
None
```

### tuple

另一种有序集合，一旦初始化不能修改（`指向不变`：变量所指向的实例不能修改）

- 定义空元组，t = ()
- 定义单元素元组，t = (1,)
- 要保证元组内容不可变，必须保证元组的每个元素本身不可变

## 条件判断

```python
if x:
    print(True)
```

只要 x 是非零，非空白字符串，非空 list，非 None 等空白或空值，就判断为 True，否则为 False

## 循环

- for x in ...：把每个元素代入变量 x
- range(x)：可以生成一个整数序列，从 0 开始，遇 x 停止
- list(range(x))：可以得到[0,1,2,3,...x-1]
- while n>0：满足 n>0 就不断循环
- break：提前结束当前整个循环
- continue：跳出当前这次循环

## 使用 dict 和 set

### dict

python 内置字典，在其他语言也叫 map，使用键-值存储，具有极快的查找速度，不会随着大小的变化而变慢，相比 list 占用大量内存，以空间换时间

| 方法 | 说明                                                                                           |
| ---- | ---------------------------------------------------------------------------------------------- |
| in   | `'T' in d` 判断'T'是否存在于 d.keys                                                            |
| get  | `d.get('T')` 获取 key 为 'T' 的值； `d.get('T', -1)` 获取 key 为 'T' 的值，如不存在取默认值 -1 |
| pop  | `d.pop('B')` 删除 key 为'B' 的键值对                                                           |

**dict 的 key 必须是不可变对象，如：字符串，整数等，否则抛异常（TypeError: unhashable type）**

### set

与 dict 类似，也是一组 key 的集合，但不存储 value，key 不能重复，数学意义上的无序和无重复元素的集合

**创建**

```python
>>> s = set([1,2,2,3,3])
>>> s
{1, 2, 3}
```

**添加**

```python
>>> s.add(4)
>>> s
{1, 2, 3, 4}
```

**删除**

```python
>>> s.remove(4)
>>> s
{1, 2, 3}
```

**并交**

```python
>>> ss = set([2,3,4])
>>> s&ss
{2, 3}
>>> s|ss
{1, 2, 3, 4}
```

### 不可变对象

```python
>>> a = 'abc'
>>> b = a.replace('a', 'A')
>>> b
'Abc'
>>> a
'abc'
```

**tuple 也是不可变对象**

- (1, 2, 3) 可以作为 dict 和 set 的 key
- (1, 2, [1, 2]) 不可作为 dcit 和 set 的 key，TypeError: unhashable type

# 五、函数

一种重复代码的抽象方式，Python 内建支持的一种封装

## 调用函数

调用一个函数，需要知道函数的名称和参数；函数名是只想一个函数对象的引用

```python
>>> a = abs
>>> a(-1)
1
```

`可以在交互式命令行通过help(abs)查看abs函数的帮助信息`

### 数据类型转换

```python
>>> int('123')
123
>>> int(12.34)
12
>>> float('12.34')
12.34
>>> str(1.23)
'1.23'
>>> str(100)
'100'
>>> bool(1)
True
>>> bool('')
False
```

## 定义函数

### 定义函数

定义一个函数要使用 def 语句，依次写出函数名、括号、括号中的参数和冒号`:`，然后，在缩进块中编写函数体，函数的返回值用 return 语句返回。

如果没有 return 语句，函数执行完毕后也会返回结果，只是结果为 None。return None 可以简写为 return。

### 空函数

定义一个什么事也不做的空函数，可以用 `pass` 来作为占位符

### 参数检查

调用函数时，如果参数个数不对，Python 解释器会自动检查出来，并抛出 `TypeError`

### 返回多个值

Python 的函数返回多值其实就是返回一个 tuple；在语法上，返回一个 tuple 可以省略括号，而多个变量可以同时接收一个 tuple，按位置赋给对应的值

### 开平方

```python
# 方法一
>>> import math
>>> math.sqrt(100)
10.0

# 方法二
>>> pow(100, 0.5)
10.0

# 方法三
>>> 100 ** 0.5
10.0
```

## 函数的参数

| 参数类型       | 说明                                                                                                                                                                                                                                                                                     |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 位置参数       | `def power(x, n):` 传入的值依次赋给对应位置的参数                                                                                                                                                                                                                                        |
| 默认参数       | `def power(x, n=2):` 在调用时可以不用输入该位置的参数，而直接使用默认值；变化大的参数放在前，变化小的放在后作为默认参数，降低调用难度；调用含多个默认参数的函数时，可以写上参数名；如调用 `def enroll(name, gender, age=6, city='Beiging'):` 可以用`enroll('Adam', 'M', city='Tianjin')` |
| 可变参数       | `def calc(*numbers):` 传入的参数个数时可变的，在参数前面加 1 个 `*` 号，参数接收到的将是一个 `tuple`；在 `tuple`/`list` 前加 1 个 `*`，可以将其以可变参数传入函数 `calc(*[1,2,3])`                                                                                                       |
| 关键字参数     | `def person(name, age, **kw):` 同理可变参数，在参数前面加 2 个`_`号，允许传入 0 个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个`dict`；在 `dict`前加 2 个`_` 可以将其以关键字参数传入函数 `person(name, age, **kw)`                                                     |
| 命名关键字参数 | `def person(name, age, *, city, job):` 如果要限制关键字参数的名字，可以用命名关键字参数；命名参数需要以 `*` 分隔，其后视为命名关键字参数，如果函数定义了一个可变参数，可以不要 `*`，命名关键字参数可以给默认值                                                                           |

**默认参数必须只想不可变对象**
`不可变对象减少了由于修改数据导致的错误，多任务环境同时读取不需加锁`

```python
# 错误写法
>>> def add_end(L=[]):
...     L.append('End')
...     return L
...
>>> add_end()
['End']
>>> add_end()
['End', 'End']
```

**参数组合**

顺序：必选参数 > 默认参数 > 可变参数 > 命名关键字参数 > 关键字参数

## 递归函数

一个函数在内部调用自己本身，就叫递归函数

函数调用是通过栈实现的，每进入一个函数调用，加一层栈锁，过多时会栈溢出

**尾递归**

把每一步的结果传递给递归函数，和循环的效果一样，栈不会增加；python 解释器没有对尾递归做优化，会栈溢出

**汉诺塔**

```python
def move(n, a, b, c):
    if n == 1:
        print(a, '->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)
```

# 六、高级特性

在 Python 中，代码越少越好，越简单越好，开发效率越高越好

## 切片

**slice**

```python
[m:n:p]
```

`m` 开始位，为 0 时可以不写，为负数时表示倒数第几个
`n` 结束位（不含），为最大长度时可以不写，为负数时表示倒数第几个
`p` 步长，从开始位取第一个元素，每 `p` 位取一个元素

**slice 实现 trim()**

```python
def trim(s):
    if s == '':
        return s
    if s[0] == ' ':
        return trim(s[1:])
    if s[-1] == ' ':
        return trim(s[:-1])
    return s
```

## 迭代

**Iteration**

遍历一个 `list`、`tuple`、`dict`、`set`、`str` 或其他可迭代对象，就叫迭代

**dict**

`dict` 不是顺序排列，迭代结果无序

`keys`: 迭代 key，`for i in d.keys():` 等同于 `for i in d:`
`values`: 迭代 value `for v in d.values():`
`items`：同时迭代 key 和 value `for key, value in d.items():`

**判断是否可迭代对象**

```python
# `str` 也是可迭代对象
>>> from collections import Iterable
>>> isinstance('abc', Iterable)
True
```

**同时迭代索引和元素**

```python
# 在 for 循环中同时引用两个变量
>>> for index, value in enumerate(['a', 'b', 'c']):
...     print(index, value)
...
0 a
1 b
2 c
```

## 列表生产式

**List Comprehensions**

把要生成的元素放在前面，后面跟 for 循环，就可以创建一个 list，这就是列表生成式

```python
# 双重循环
# if 在 for 后面，if 是筛选条件，不能加 else
>>> [m + n for m in L1 for n in L2 if isinstance(m, str) and isinstance(n, str)]
# if 在 for 前面，for 前面是一个完整表达式，必须加 else 以计算出一个结果
>>> [x if x % 2 == 0 else -x for x in range(1, 11)]
>>> list(range(2, 10, 2)) # 参数位同切片
```

## 生成器

**Generator**

可以按照某种算法推算出列表后续的元素，而不用创建完整的列表，一边循环一边计算的机制，就叫生成器

**创建方式**

1. 把列表生成式的 [] 换成 ()
2. 函数的 return 换成 yield（包含 yield 的函数即生成器）

**调用方式**
调用 genertor 时，会生成一个 generator 对象 g

1. next(g)
2. for n in g

**生成器与函数的区别**

|           | 说明                                                                                                                  |
| --------- | --------------------------------------------------------------------------------------------------------------------- |
| function  | 顺序执行，遇到 return 或最后一行返回，直接返回结果                                                                    |
| generator | 调用 next() 时执行，遇到 yield 返回，再次执行 next() 时从上次返回的 yield 继续执行，“调用”实际返回一个 generator 对象 |

generator 调用 next()

```python
# 杨辉三角
def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]
```

## 迭代器

**Iterator**

|          | 说明                                                                                                                                            |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Iterable | 可迭代对象，如 `list`、`tuple`、`dict`、`set`、`str` 等，以及 `generator`                                                                       |
| Iterator | 可以被 next() 函数调用并不断返回下一个值的对象，没有下一个值时抛出 `StopIteration` 错误，表示的是一个数据流，其计算是惰性的，并不能提前知道长度 |

**判断是否迭代器**

```python
>>> from collections.abc import Iterator
>>> isinstance((x for x in range(10))， Iterator)
True
```

**iter()**
将 `Iterable`对象变成 `Iterator`

```python
>>> isinstance(iter('abc'), Iterator)
True
```

`for 本质就是不停调用 next()，对于 Iterable 对象，先使用 iter() 将其变为 Iterator`

# 七、函数式编程

**面向过程程序设计**

通过一层一层的函数调用，把复杂的任务分解成简单任务，这种分解称之为面向过程的程序设计，`函数`是面向过程编程的基本单元

**Functional Programming**

一种抽象程度很高的编程范式，纯粹的函数式编程语言（Lisp）编写的函数没有变量，只要输入确定，输出就是确定的（没有副作用）。允许使用变量的函数内部变量状态不确定，同样输入可能输出不同

Python 对函数式编程提供部分支持，其允许使用变量，不是纯函数式编程语言

## 高阶函数

**Higher-order function**

变量可以指向函数 `and` 函数名也是变量 `->` 函数可以接收另一个函数作为参数

`其参数能够接收别的函数的函数，就是高阶函数`

### map/reduce

**map()**

接收两个参数，一个是函数(单个参数)，一个是 Iterable 对象，map 将传入的函数依次作用在 Iterable 对象的每一个元素上，并把结果作为一个新的 Iterator 返回，注意 Iterator 是惰性的

```python
>>> list(map(str, [1, 2, 3, 4, 5]))
['1', '2', '3', '4', '5']
```

**reduce()**

把一个函数（必须是两个参数）作用在一个序列上，reduce 把结果与下个元素做累计计算

```python
reuce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
```

```python
# str2int
from functools import reduce

DIGITS = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}


def char2num(c):
    return DIGITS[c]


def str2int(s):
    return reduce(lambda x1, x2: x1 * 10 + x2, map(char2num, s))
```

```python
# str2float
from functools import reduce

DIGITS = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}


def char2num(c):
    return DIGITS[c]


def str2int(s):
    return reduce(lambda x1, x2: x1 * 10 + x2,
                  map(char2num, [c for c in s if c != '.']))


def str2float(s):
    return str2int(s) / (10**s[::-1].index('.'))
```

```python
# str2float
def str2float(s):
    point = 0

    def to_float(i, c):
        nonlocal point
        if not isinstance(c, int):
            point = 1
            return i
        if point == 0:
            return i * 10 + c
        else:
            point *= 10
            return i + c / point

    return reduce(to_float, map(char2num, s))
```

`nonlocal` 关键字用来在函数或其他作用域使用外层（非全局）变量

### filter

接收一个函数（单个参数）和一个序列，序列的每个元素作用于函数，返回 True/False 决定是否保留该元素

**素数 - 埃氏筛选**

```python
def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    oi = _odd_iter()
    while True:
        n = next(oi)
        yield n
        oi = filter(_not_divisible(n), oi)
```

### sorted

接收一个 Iterable 对象，一个函数（形参：key，一个参数的函数），以及 reverse；key 作用与序列的每个元素，再对结果排序，reverse 表示是否反向排序，默认为 False

## 返回函数

**函数作为返回值**
往往不需要立即执行的时候，可以使用返回函数的方式达到惰性计算的效果（`lazy`）

**闭包（Closure）**
当返回函数时，相关参数和变量都保存在返回的函数中，这种程序结构成为`闭包`

```python
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
```

```python
>>> f1()
9
>>> f2()
9
>>> f3()
9
```

返回的函数引用了变量 i，但它并没有立刻执行，等到 3 个函数都返回时，它们引用的变量 i 已经变成了 3，因此最终结果都是 9

`返回闭包时，返回函数不要引用任何循环变量，或者后续会发生变化的变量`

```python
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        # f(i) 立即执行，因此 i 的当前值被传入 f()
        fs.append(f(i))
    return fs
```

```python
>>> f1, f2, f3 = count()
>>> f1()
1
>>> f2()
4
>>> f3()
9
```

添加多层函数，用执行外层函数将循环变量的值绑定到函数的参数中，可以绑定循环变量变化过程中的值

**计数器（闭包）**

```python
def createCounter():
    def counter():
        n = 0
        while True:
            n += 1
            yield n
    c = counter()
    return lambda : next(c)
```

```python
def createCounter():
    n = 0
    def counter():
        nonlocal n
        n += 1
        return n
    return counter
```

## 匿名函数

关键字 `lambda` 表示匿名函数，冒号前面的是参数表，冒号后面的是返回结果，不用写 return，只能有一个表达式

匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数

```python
>>> f = lambda x: x*x
>>> f(5)
25
```

也可以把匿名函数当作一个函数的返回值返回

```python
def build(x, y):
    return lambda x, y: x*x + y*y
```

## 装饰器

**Decorator**

在函数调用前后自动增加处理，不修改函数的定义，这种在代码运行期间动态增加功能的方式，即为 `Decorator`

```python
import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'call {func.__name__}():')
        return func(*args, **kwargs)

    return wrapper
```

```python
def log(info):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f'{info} {func.__name__}')
            return func(*args, **kwargs)

        return wrapper

    return decorator
```

**调用 Decorator**

```python
@log
def now():
    print('2020-11-12')
```

```python
now = log(now)
```

```python
@log('execute')
def now():
    print('2020-11-12')
```

```python
now = log('execute')(now)
```

`functools.wraps(func)` 的作用是将 `wrapper` 函数的 `__name__` 改为被装饰函数对象的 `__name__`， 相当于：

```python
wrapper.__name__ = func.__name__
```

`Decorator` 即在 `面向对象(OOP)` 的 `设计模式` 中的 `装饰模式`，OOP 的装饰模式通过类的继承和组合实现，而 Python 可以直接从语法层面支持 decorator，也可以通过类实现

## 偏函数

**Partial function**

把一个函数的某些参数固定住（给这些参数设置默认值），返回一个新函数，以方便调用

`偏函数仅仅是给参数设定了默认值，在调用新函数时是可以传入其他值给这些参数的`

```python
import functools
# 相当于
# kw = {'base': 2}
# int('1000000', **kw)
>>> int2 = functools.partial(int, base=2)
>>> int2('1000000')
64
>>> int2('1000000', base=10)
1000000
```

```python
# 相当于
# args = [10]
# args.extend([5, 6, 7])
# max(*args)
>>> max2 = functools.partial(max, 10)
>>> max2(5, 6, 7)
10
```

创建偏函数时，实际接收的参数是：函数对象，\*args / \*\*kwargs

# 八、模块

**Module**

模块是一组 Python 代码集合，可以使用其他模块，也可以被其他模块使用，创建模块不能与系统模块名重复

一个 `.py` 文件就是一个模块

```
mycompany
├─ __init__.py
├─ abc.py
└─ xyz.py
```

按目录组织模块的方法，称之为包 `Package`，每个包目录下必须有一个 `__init__.py` 文件，否则这个目录就是一个普通目录；`__init__.py` 本身就是一个模块，它的模块名就是所在目录的名称

## 使用模块

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'aurelius'

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello world.')
    elif len(args) > 1:
        print('too many arguments.')


if __name__ == "__main__":
    test()
```

> 第 1 行指定 `.py` 文件在 `Unix/Linux/Mac` 上运行使用的 Python 解释器
> 第 2 行表示 `.py` 文件本身使用标准 UTF-8 编码
> 第 4 行表示模块文档注释，模块代码的第一个字符串都被视作模块的文档注释
> 第 6 行使用 `__author__` 变量表明作者
> 第 8 行导入模块，这样就可以访问模块的所有功能

**sys**

`sys` 模块有一个 `argv` 变量，存储着启动 `.py` 文件时命令中的所有参数，至少有一个元素，第一个元素永远是该 `.py` 文件的名称

**\_\_main\_\_**

在使用 Python 解释器启动 `.py` 文件时，Python 解释器会把该 `.py` 模块的 `__name__` 置为 `__main__`，通常用于通过命令行直接执行 `.py` 文件执行一些额外代码，用于运行测试等

### 作用域

- public: xxx
- private: \_xxx, \_\_xxx
- 特殊变量: \_\_xxx\_\_

`Python 对 private 函数或变量的访问限制无强制作用`

## 安装第三方模块

- 使用 `pip`

```shell
pip install Pillow
```

- 使用 `Anaconda`

基于 Python 的数据处理和科学计算平台

### 模块搜索路径

模块搜索路径存放在 `sys` 模块的 `path` 变量

**模块搜索顺序**

当前目录 > 所有已安装的内置模块 > 第三方模块

**修改模块搜索目录**

- 直接修改 sys.path 的值，运行时修改，运行结束失效
- 设置环境变量 `PYTHONPATH`，该环境变量的内容会被添加到模块搜索目录

# 九、面向对象编程

**Object Oriented Programming**

简称 OOP，一种程序设计思想，以对象为程序基本单元，一个对象包含数据和数据的操作方法

面向对象的设计思想来自自然界的类（Class）和实例（Instance），抽象出 `Class`，根据 `Class` 创建 `Instance`，抽象程度比函数高（既包含数据，又包含操作数据的函数）

数据封装、继承、多态是面向对象的三大特点

## 类和实例

`Class` 是抽象的模板，是创建 `Instance` 的模板

```python
>>> class Student(object): # 定义类
...     pass
...
>>> s1 = Student() # 创建实例
>>> s1.name = 'Aurelius' # 实例属性绑定
>>> s1.name
'Aurelius'
```

Python 允许对实例绑定任何数据，即使一个类的两个实例，他们拥有的变量名称都可能不同

创建实例时强制绑定属性

```python
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
```

和普通函数相比，类中定义的函数第一个参数永远是实例变量 `self`，且调用时不用传值，`self` 指向创建的实例本身

### 数据封装

通过实例函数访问实例的数据，不直接从外部访问这些数据

**好处**

调用方便

## 访问限制

限制外部代码对实例内部一些属性和方法的访问，可以加强代码的健壮性

Python 没有任何强制机制限制访问权限

在 Class 定义的内部属性前加 `__` 可以把属性变成私有，通过 get_p(), set_p() 方法来访问这些属性

`__property` 被 Python 解释器自动改为 `_ClassName__property`

`__xxx__` 在 Python 中属于特殊属性，不是私有的，可以被访问的

## 继承和多态

`继承` 可以把父类的所有功能直接拿来，子类只需要新增自己特有的方法，重写覆盖父类中不适合的方法

`多态` 是把一个子类对象赋给一个父类变量，调用方法是子类实现

**开闭原则**

对扩展开放，对修改封闭

**鸭子模式**

```python
def twice_run(animal):
    animal.run()
    animal.run()

class Timer(object):
    def run(self):
        print('Start ...')
```

传入 twice_run() 的对象不必是 Animal 的子类，只要有 run() 即可

`因此相对静态语言，动态语言（Python）的继承不是那么必要`

## 获取对象信息

### type()

获取对象类型

| 类型     | 类型常量                  | 对象                   |
| -------- | ------------------------- | ---------------------- |
| int      | int                       | 123                    |
| str      | str                       | '123'                  |
| 函数     | types.FunctionType        | def fn(): pass         |
| 内建函数 | types.BuiltinFunctionType | abs                    |
| 匿名函数 | types.LambdaType          | lambda x: x            |
| 生成器   | types.GeneratorType       | (x for x in range(10)) |

### isinstance()

判断是否指定类型或指定类型元组中的一个

```python
>>> isinstance(x, t) # x 是对象，t 是类型，t 可以是多个类型组成的一个 tuple 对象
```

### dir()

获取对象的所有属性和方法

**len()**

实际是调用了对象的 \_\_len\_\_() 方法，因此按照鸭子类型，自己的类只要实现了 \_\_len\_\_()，也可以使用 len(myObj)

**getattr(obj, pname)**

获取对象的指定属性或方法，也可以传第 3 个参数作为默认值

**setattr(obj, pname, pvalue)**

设置对象指定属性的值

**hasattr(obj, pname)**

判断对象是否存在指定名称的属性或方法

可以确定存在而直接访问的属性或方法，就不要使用`getattr`，因此可以通过`hasattr`判断属性或方法是否存在

## 实例属性和类属性

通过实例变量或`self`变量绑定`实例属性`

通过类本身绑定的是`类属性`，类属性归类所有，但类的所有实例都可以访问到

```python
>>> class Student(object):
...     name = 'Student'
...
>>> s = Student()
>>> print(s.name)
Student
>>> print(Student.name)
Student
>>> s.name = 'Aurelius'
>>> print(s.name)
Aurelius
>>> print(Student.name)
Student
>>> del s.name
>>> print(s.name)
Student
```

相同名称的实例属性将屏蔽类属性（当查找到对应名称的实例属性时，即使存在同名类属性，也不会被查找到），当删除实例属性后，可以再次访问到类属性

# 十、面向对象高级编程

## \_\_slots\_\_

**动态绑定方法**

给`Instance`绑定方法，只对当前`Instance`有效

```python
class Student(object):
    pass

s = Student()

def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
```

给`Class`绑定方法，对所有`Instance`有效

```python
def set_score(self, score):
    self.score = score

Student.set_score = set_score
s.set_score(100)
```

**使用 \_\_slots\_\_**

用来限制 `class` 实例可以添加的属性，包括`Class`定义中绑定的属性

```python
class Student(object):
    # tuple定义允许绑定的属性名称
    __slots__ = ('name', 'age')
```

`__slots__`只对当前类有效，对子类无效；若子类也定义了`__slots__`，有效范围时自身加父类的范围

## @property

把一个`getter`方法变成属性，同时创建另一个装饰器`@pname.setter`，负责把另一个`setter`方法变成属性赋值

```python
class Student(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    # 只读属性
    @property
    def age(self):
        return 2020 - self._birth
```

## 多重继承

Python 允许使用多重继承，一个子类可以同时继承多个父类的所有功能

**MixIn**

除了继承自主线，还额外混入其他类的功能，这种设计叫`MixIn`

## 定制类

通过一些`__xxx__`属性定制类

### \_\_str\_\_

返回给用户看到的字符串，实例的打印结果

### \_\_repr\_\_

返回实例调式值显示结果

### \_\_iter\_\_

将`Class`实例变成一个迭代器，需要实现`__next__()`方法，for 循环会不断调用迭代对象的`__next__()`

```python
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration()
        return self.a
```

### \_\_getitem\_\_

通过索引器或者切片读取实例的值时被调用

```python
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start, stop = n.start, n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            res = []
            for x in range(stop):
                if x >= start:
                    res.append(a)
                a, b = b, a + b
            return res
```

`slice`的`step`参数和负数值可以进一步处理

### \_\_getattr\_\_

当调用实例不存在的属性时被调用，已有的属性不会在`__getattr__`中查找

`__getattr__`可以实现完全动态的调用

```python
class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain(f'{self._path}/{path}')

    def __call__(self, param):
        return Chain(f'{self._path}/{param}')

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().status.user('Aurelius').timeline.list)
```

### \_\_call\_\_

定义了`__call__`，就可以调用实例本身，`__call__`可以有参数

```python
class Student(object):
    def __init__(self, name):
        return self._name

    def __call__(self, text):
        print(f'{self._name}: {text}')

print(Student('Aurelius')('A'))
```

**类本身的调用会执行`type`的`__call__`方法**

## 枚举类

将一组相关常量定义在一个`Class`中，并且不可变，成员可以直接比较

**通过`Enum`调用**

```python
>>> from enum import Enum
>>> Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
>>> for name, member in Month.__members__.items():
...    print(name, '=>', member, ',', member.value)
...
Jan => Month.Jan , 1
Feb => Month.Feb , 2
Mar => Month.Mar , 3
Apr => Month.Apr , 4
May => Month.May , 5
Jun => Month.Jun , 6
Jul => Month.Jul , 7
Aug => Month.Aug , 8
Sep => Month.Sep , 9
Oct => Month.Oct , 10
Nov => Month.Nov , 11
Dec => Month.Dec , 12
```

**通过继承`Enum`**

```python
from enum import Enum, unique

@unique
class Weekday(Enum):
    Sum = 0 # 默认从 1 开始，这里设置 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
```

**获取方式**

- `Enum['Name']`
- `Enum.Name`
- `Enum(value)`

## 元类

### type

`type`函数既可以返回一个对象的类型，又可以创建出新的类型

**`type`创建`class`**

```python
def fn(self, name='world'):
    print(f'Hello, {name}')

Hello = type('Hello', (object,), dict(hello=fn))
h = Hello()
h.hello()
```

`type()` 的 3 个参数：

- class 的名称
- 继承的父类元组
- class 的方法和其绑定函数的字典

### metaclass

`metaclass`允许创建类或修改类，可以把类看作`metaclass`创建的实例

**定义`metaclass`**

```python
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
```

`__new__()`的 4 个参数依次是：

- 当前准备创建的类对象
- 类的名称
- 类继承的父类元组
- 类的方法字典

**定制类**

```python
# 在 Python 解释器创建 MyList 时，要通过 ListMetaclass.__new__() 来创建
class MyList(list, metaclass=ListMetaclass):
    pass
```

Python 解释器首先在当前类的定义中查找`metaclass`，如果没有，就继续在父类查找，知道找到，用来创建当前类，`metaclass`隐式继承到子类

# 十一、错误、调试和测试

## 错误处理

```python
try:
    # 可能有异常的代码块
    r = 10/int('2')
except ValueError as e:
    # 有异常时执行，捕获指定类型及其子类型的错误
    print('ValueError', e)
except ZeroDivisionError as e:
    # 当前面的异常命中后，后面不会再次捕获
    print('ZeroDivisionError', e)
else:
    # 无异常时执行
    print('no error.')
finally：
    # 上面结束后一定会执行
    print('finally')
```

**调用栈**

从上到下时整个错误的调用函数链，依次从外到内

**记录错误**

```python
try:
    r = 10/int('0')
except Exception as e:
    # 记录错误堆栈
    logging.exception(e)
```

**抛出异常**

```python
# 自定义异常
class FooError(ValueError):
    pass

# 抛出异常
raise FooError('invalid value')

# 捕获异常，原样抛出
except ValueError as e:
    raise

# 转化成另一种异常抛出
except ZeroDivisionError:
    raise ValueError('input error.')
```

程序主动抛出异常时，应该在文档写清楚可能抛出的异常及其原因，方便调用者处理相应的错误

## debug

### assert

如果断言的语句不成立，assert 语句会抛出 AssertionError

```python
assert n!=0, 'n is zero.'
```

可以通过 `-O` 参数关闭断言，关闭后，`assert` 语句相当于 `pass`

### logging

```python
import logging
logging.basicConfig(level=logging.INFO)

logging.info('xxx')
```

logging level

- CRITICAL
- ERROR
- WARNING - 根记录器级别默认级别
- INFO
- DEBUG
- NOTSET - 默认级别，处理所有消息

logging 的另一个好处时通过配置，一条消息可以同时输出到不同的地方，比如`console`、文件、`database`

**多使用`logging`**

### pdb

以参数`-m pdb`启动`.py`，单步运行

```cmd
python -m pdb xxx.py
```

`pdb`界面指令

| 指令 | 作用                |
| ---- | ------------------- |
| l    | 查看代码            |
| n    | 单步执行            |
| p    | `p 变量名` 查看变量 |
| q    | 结束调试，退出程序  |
| c    | 继续运行            |

**set_trace()**

设置断点，进入调试后，通过`c`命令运行自动暂停在该断点处

### IDE

[Visual Studio Code](https://code.visualstudio.com/)

[PyCharm](http://www.jetbrains.com/pycharm/)

## unittest

**TDD**

测试驱动开发（Test Driven Development）

单元测试是未来重构代码的保障

单元测试要覆盖常用输入组合，边界条件，异常

单元测试不能太复杂，否则自身也可能有 bug

### 编写

```python
import unittest
class TestDict(unittest.TestCase):
    def test_init(self):
        d = dict(a=1, b='test')
        # 断言相等
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        # 断言为真
        self.assertTrue(isinstance(d, dict))

    def test_keyerror(self):
        d = dict()
        # 期待语句块中抛出指定类型的 Error
        with self.assertRaises(KeyError):
            value = d['empty']
```

`单元测试类`继承自`unittest.TestCase`
`单元测试方法`必须以`test`开头命名，否则不会被执行

### 运行

**通过代码运行**

```python
if __name__ == '__main__':
    unittest.main()
```

**通过命令参数运行**

```powershell
python -m unittest mytest
```

### setUp 与 tearDown

在每调用一个单元测试的前后被执行

## doctest

文档测试，既可以用来运行测试，也是实例代码

严格按照 Python 交互命令行的输入和输出来判断测试结果的正确性

在测试异常时，可用`...`表示中间省略的输出

```python
class Dict(dict):
    """
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    """
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(f"'Dict' object has no attribute '{key}'")

    def __setattr__(self, key, value):
        self[key] = value


if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

**运行**

```powershell
python mydict.py
```

没有输出既是运行正确

# 十二、IO 编程

`IO`指`Input`/`Output`

`Input Stream` 从外面（磁盘、网络）流进内存

`Output Stream` 从内存流到外面

`同步 IO` CPU 等待`IO`完成，程序暂停后续执行

`异步 IO` CPU 不等待`IO`完成，先做其他事，通过**回调**或**轮询**处理`IO`后续

## 文件读写

在磁盘上读写文件的功能都是有操作系统提供的，现代操作系统不允许普通程序直接操作磁盘

**文件流操作方法**

| 方法        | 说明                                                                                                      |
| ----------- | --------------------------------------------------------------------------------------------------------- |
| open()      | 以指定模式打开文件对象，参数为`文件名`和`模式标示符`，可选参数`encoding`(编码) `errors`(编码错误处理方式) |
| read()      | 一次读取文件所有内容，返回`str`对象                                                                       |
| read(size)  | 每次读取`size`个字节的内容                                                                                |
| readline()  | 每次读取一行内容                                                                                          |
| readlines() | 一次读取所有内容，并返回以行分割的`list`                                                                  |
| write()     | 将要写入的内容写入内存缓存，当`close` 被调用时真正将内容写出                                              |
| close()     | 关闭文件，关闭前将内存缓存中的内容全部写出                                                                |

**文件对象模式**

| 字符 | 含义                                   |
| ---- | -------------------------------------- |
| `r`  | 读取（默认）                           |
| `w`  | 写入，先 truncate 文件                 |
| `x`  | 独占创建，如果文件已经存在则失败       |
| `a`  | 写入，如果文件已经存在则追加到文件末尾 |
| `b`  | 二进制模型                             |
| `t`  | 文字模式（默认）                       |
| `+`  | 更新（读写）                           |

### 读文件

```python
with open('/Users/aurelius/test.txt', 'r') as f:
    print(f.read())
```

`with`语句可保证`open`的文件最终会被`close`，同样的功能可以通过`try ... finally`语句在`finally`中执行`close`实现

### 写文件

```python
with open('/User/aurelius/test.txt', 'w') as f:
    f.write('hello, world.')
```

## StringIO 和 BytesIO

### StringIO

在内存中读写`str`，和读写文件具有一致的接口

```python
from io import StringIO
# InputStream
f = StringIO()
f.write('hello')
# 读取写入的 str
f.getvalue()

# OutputStream
f = StringIO('hello, 中国')
f.read()
```

### BytesIO

在内存中读写`bytes`

```python
from io import BytesIO
# InputStream
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

# OutputStream
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read().decode('utf-8'))
```

## 操作文件和目录

Python 内置的`os`模块可以直接调用系统提供的接口函数操作文件和目录

```python
>>> import os
>>> os.name
nt
```

### 环境变量

```python
os.environ # 全部环境变量 (Class<Environ>)
os.environ.get('key', 'default') # 指定的环境变量，default 可选
```

### 操作文件和目录

| 函数                                  | 作用                                                                         |
| ------------------------------------- | ---------------------------------------------------------------------------- |
| os.path.abspath('.')                  | 当前路径的绝对路径                                                           |
| os.path.join(r'd:\a', 'b')            | 把路径 2（`b`）拼接到路径 1（`d:\a`）上，路径 2 若为绝对路径，直接返回路径 2 |
| os.mkdir(r'd:\test')                  | 创建一个目录                                                                 |
| os.mkdir(r'd:\test')                  | 删除一个目录                                                                 |
| os.path.split(r'd:\test\file.txt')    | 拆分成最后级别目录和文件名                                                   |
| os.path.splitext(r'd:\test\file.txt') | 拆分下文件扩展名                                                             |
| os.rename('test.txt', 'text.py')      | 重命名文件                                                                   |
| os.remove('test.py')                  | 删除文件                                                                     |
| os.listdir('.')                       | 列举指定路径                                                                 |
| os.path.isdir('d:\test')              | 判断是否路径                                                                 |
| os.path.isfile('d:\test\test.txt')    | 判断是否文件                                                                 |

`shutil`模块对`os`功能做了补充，其`copyfile()`提供文件复制功能

## 序列化

把变量从内存中变成可存储或传输的过程称为序列化`pickling`，把序列化对象重新读到内存里称为反序列化`unpickling`

### Pickle

**dumps/dump**

```python
>>> import pickle
>>> d = dict(name='中国人', age=18, score=99)
# pickle.dumps 把任意对象序列化成 bytes
>>> pickle.dumps(d)
b'\x80\x04\x95*\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x04name\x94\x8c\t\xe4\xb8\xad\xe5\x9b\xbd\xe4\xba\xba\x94\x8c\x03age\x94K\x12\x8c\x05score\x94Kcu.'
# pickle.dump 直接把对象序列化后写入 file-like Ojbect
>>> with open('dump.txt', 'wb') as w:
...     pickle.dump(d, w)
```

**loads/load**

```python
>>> with open('dump.txt', 'rb') as r:
...     d = pickle.load(r)
...
>>> d
{'name': 'Aurelius', 'age': 18, 'score': 99}
```

`pickle`反序列化得到的变量与原来的变量完全无关，只是值相同而已

`pickle`序列化只适用于 Python，且不同版本彼此不兼容

### JSON

序列化的一种标准格式，适用于不同编程语言之间传递，标准编码使用 UTF-8

**JSON 类型关系**

| JSON 类型  | Python 类型 |
| ---------- | ----------- |
| {}         | dict        |
| []         | list        |
| string     | str         |
| int/float  | int/float   |
| true/false | True/False  |
| null       | None        |

```python
>>> import json
>>> d = dict(name='Aurelius', age=18, score=99)
>>> json_str = json.dumps(d)
>>> json_str
'{"name": "Aurelius", "age": 18, "score": 99}'
>>> json.loads(json_str)
{'name': 'Aurelius', 'age': 18, 'score': 99}
```

`dumps`/`dump`的`ensure_ascii`参数可以决定是否统一将返回的`str`对象编码为`ascii`字符

### JSON 进阶

自定义类的对象不能直接序列化，需要实现`dumps`/`dump`的`default`参数对应的方法，将该对象转化成`dict`对象

```python
json.dumps(o, default=object2dict)
```

通常`class`都有`__dict__`属性，存储着实例的变量（定义了`__solts__`除外），因此可以直接如此调用

```python
json.dumps(o, default=lambda o: o.__dict__)
```

`loads`/`load`在反序列化自定义类型时也需传入`object_hook`相应方法，将`dict`对象转化为自定义类型的对象

```python
json.loads(json_str, object_hook=dict2object)
```

# 十三、进程与线程

`线程`是最小的执行单元

`进程`是最小的资源分配单元，至少由一个线程组成

## 多进程

`Unix`/`Linux`操作系统的`fork()`可以把当前进程（父进程）复制一份（子进程），然后分别在父子进程内返回，其中子进程返回的是 0，父进程返回的是子进程 ID，子进程通过`getppid()`获取父进程 ID

`os`模块封装的系统调用包含`fork`

```python
import os

print(f'Process {os.getpid()} start...')
pid = os.fork()
if pid = 0:
    print(f'child process {os.getpid()}, parent is {os.getppid()}')
else:
    print(f'process {os.getpid()} created a child process {pid}')
```

```
Process 1798 start...
child process 1799, parent is 1798
process 1798 created a child process 1799
```

### multiprocessing

跨平台的多进程模板

```python
from multiprocessing import Process

import os
import time


def proc(name):
    # time.sleep(5)
    print(f'run child process {name} ({os.getpid()})')


if __name__ == "__main__":
    print(f'parent process {os.getpid()}')
    # 创建 Process 实例
    p = Process(target=proc, args=('test', ))
    print('child process will start.')
    # 启动 p 子进程
    p.start()
    # 阻塞，等待 p 子进程结束后才继续往下执行
    p.join()
    print('child process end.')
```

```
parent process 4872
child process will start.
run child process test (14360)
child process end.
```

子进程结束后主进程才会退出

### Pool

进程池，用于批量启动子进程

```python
from multiprocessing import Pool
import os, time, random


def proc(name):
    print(f'run task {name} ({os.getpid()})')
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print(f'task {name} runs: {end-start}')


if __name__ == "__main__":
    print(f'parent process {os.getpid()}')
    # 正在运行的子进程个数
    p = Pool(4)
    for i in range(5):
        p.apply_async(proc, args=(i, ))
    print('waiting for all subprocesses done...')
    # close 后不能继续添加新的 process
    p.close()
    # 等待所有子进程执行完毕，必须在 close 后调用
    p.join()
    print('all subprocess done.')
```

```
parent process 14360
waiting for all subprocesses done...
run task 0 (10800)
run task 1 (7996)
run task 2 (4084)
run task 3 (3492)
task 0 runs: 1.7698190212249756
run task 4 (10800)
task 1 runs: 1.9010038375854492
task 2 runs: 2.1044681072235107
task 3 runs: 2.431309700012207
task 4 runs: 2.9220056533813477
all subprocess done.
```

### subprocess

创建外部进程，并控制其输入输出，如调用命令`nslookup`，并与之交互

```python
# 调用 snlookup 子进程
p = subprocess.call(['nslookup', 'www.python.org'])

# 启动 nslookup 子进程，并设置其输入输出流
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# 向 p 子进程输入命令，并接收输出
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# 打印输出
print(output.decode('gbk'))
```

### 进程间通行

Python 的`multiprocessing`模块提供了`Queue`、`Pipes`等交换数据的方式

```python
from multiprocessing import Process, Queue
import os, time, random


def write(q):
    print(f'process to write: {os.getpid()}')
    for value in ['A', 'B', 'C']:
        print(f'put {value} to queue...')
        q.put(value)
        time.sleep(random.random())


def read(q):
    print(f'process to read: {os.getpid()}')
    while True:
        value = q.get(True)
        print(f'get {value} from queue.')


if __name__ == "__main__":
    q = Queue()
    pw = Process(target=write, args=(q, ))
    pr = Process(target=read, args=(q, ))
    pw.start()
    pr.start()
    pw.join()
    # 写完即可关闭读进程
    pr.terminate()
```

```
process to write: 9472
put A to queue...
process to read: 10084
get A from queue.
put B to queue...
get B from queue.
put C to queue...
get C from queue.
```

## 多线程

Python 标准库提供了两个线程模块：`_thread`(低级模块)、`threading`(高级模块，`_thread`的封装)

```python
import time, threading


def loop():
    print(f'thread {threading.current_thread().name} is running...')
    n = 0
    while n < 5:
        n = n + 1
        print(f'thread {threading.current_thread().name} >>> {n}')
        time.sleep(1)
    print(f'thread {threading.current_thread().name} ended.')


print(f'thread {threading.current_thread().name} is running...')
# 传入一个函数以创建 Thread 实例
t = threading.Thread(target=loop, name='LoopThread')
# 启动子线程
t.start()
# 阻塞等待子线程执行结束
t.join()
print(f'thread {threading.current_thread().name} ended.')
```

```
thread MainThread is running...
thread LoopThread is running...
thread LoopThread >>> 1
thread LoopThread >>> 2
thread LoopThread >>> 3
thread LoopThread >>> 4
thread LoopThread >>> 5
thread LoopThread ended.
thread MainThread ended.
```

### Lock

多进程中，同一个变量会被拷贝到每个进程中，互不影响

多线程中，所有变量由所有线程共享

高级语言的一条语句在 CPU 执行时可能是若干条语句，当多个线程同时操作同一个变量时，变量在缓存状态下可能已被修改，此时执行结果无法满足"一致性"（类比`事务`的`一致性`）

```python
import threading
balance = 0
lock = threading.Lock()

def run_thread(n):
    for i in range(10000):
        # 获取锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            # 释放锁
            lock.release()
```

`锁`可以避免上述问题，同一时刻最多只有一个线程持有同一个锁，只有成功获得锁，才能继续执行代码，其他尝试获取该锁的线程会被阻塞，知道获得锁的线程释放该锁

**坏处**

阻止多线程的并发执行

**死锁**

存在多个锁，多个线程试图获取对方持有的锁，会导致多个线程同时挂起，只能靠操作系统强制终止

### GIL

`Global Interpreter Lock` 全局解释器锁，任何 Python 线程在执行前必须先获得`GIL`，每执行 100 条字节码自动释放`GIL`，这导致多线程在同一时间实际永远不能利用多核 CPU，只能交替执行

Python 中多线程并发不能利用多核 CPU

## ThreadLocal

多线程环境下，全局变量必须加锁，相较使用局部变量会更好

局部变量需要在函数调用建以参数传递，十分麻烦，此时可引入`ThreadLocal`变量

`ThreadLocal`变量虽是全局变量，但每个线程只能读取自己线程独立副本，互不干扰

```python
import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()


def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('Alice', ), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob', ), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
```

## 进程 vs. 线程

**多进程**

- 优点：稳定性好，子进程挂掉不影响其他
- 缺点：创建，切换等操作开销巨大

**子线程**

- 优点：开销稍小
- 缺点：所有线程共享其所在进程的内存，一个线程挂掉，整个进程崩溃

### 线程切换

多线程的并行实际是单核快速在多线程间切换的效果，当线程多到一定程度，线程切换会消耗系统大量资源，使效率急剧下降

### 计算密集型 vs. IO 密集型

**计算密集型**

消耗都在 CPU，最高效率利用 CPU，同时进行的任务数应等于 CPU 核数

Python 的运行效率较低，不适合计算型程序，最好使用 C 语言

**IO 密集型**

消耗在等待 IO 上，CPU 消耗少，任务越多，CPU 效率越高

Python 与 C 语言在 IO 密集型程序上的运行效率表现相差不大，Python 开发效率往往更高

### 异步 IO

操作系统提供的异步 IO 支持，事件驱动模型

Python 中单线程的异步编程模型称为`协程`

## 分布式进程

Process 可以分布到多台机器上（分布式），Thread 最多只能分布在同一机器的多个 CPU

Python 的`multiprocessing`模块的子模块`managers`对分布式做了支持

```python
# task_master.py

import random, queue
from multiprocessing.managers import BaseManager

# 发送任务的队列:
task_queue = queue.Queue()
# 接收结果的队列:
result_queue = queue.Queue()


def get_task_queue():
    return task_queue


def get_result_queue():
    return result_queue


# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass


if __name__ == "__main__":

    # 把两个Queue都注册到网络上, callable参数关联了Queue对象:
    QueueManager.register('get_task_queue', callable=get_task_queue)
    QueueManager.register('get_result_queue', callable=get_result_queue)
    # 绑定端口5000, 设置验证码'abc':
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
    # 启动Queue:
    manager.start()
    # 获得通过网络访问的Queue对象:
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    # 放几个任务进去:
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)
    # 从result队列读取结果:
    print('Try get results...')
    for i in range(10):
        r = result.get(timeout=100)
        print('Result: %s' % r)
    # 关闭:
    manager.shutdown()
    print('master exit.')
```

```python
import time, queue
from multiprocessing.managers import BaseManager


# 创建类似的QueueManager:
class QueueManager(BaseManager):
    pass


if __name__ == "__main__":

    # 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
    QueueManager.register('get_task_queue')
    QueueManager.register('get_result_queue')

    # 连接到服务器，也就是运行task_master.py的机器:
    server_addr = '127.0.0.1'
    print('Connect to server %s...' % server_addr)
    # 端口和验证码注意保持与task_master.py设置的完全一致:
    manager = QueueManager(address=(server_addr, 5000), authkey=b'abc')
    # 从网络连接:
    manager.connect()
    # 获取Queue的对象:
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    # 从task队列取任务,并把结果写入result队列:
    for i in range(10):
        try:
            n = task.get(timeout=1)
            print('run task %d * %d...' % (n, n))
            r = '%d * %d = %d' % (n, n, n * n)
            time.sleep(1)
            result.put(r)
        except queue.Queue.Empty:
            print('task queue is empty.')
    # 处理结束:
    print('worker exit.')
```

通过`managers`模块把`Queue`暴露到网络以便其他机器的进程访问，`worker`中并没有保存`Queue`，`Queue`存储在`master`中

`Queue`是用来传递任务和接收结果的，任务的描述数据要尽量小，如果要传输体量较大的数据，可通过共享磁盘等，让`worker`自行读取

# 十四、正则表达式

用一种描述性的语言给字符串定义一个规则，用这种规则匹配字符串

| 描述符 | 作用                      | 示例                              |
| ------ | ------------------------- | --------------------------------- |
| \d     | 匹配数字                  | '00\d' 匹配 '007'                 |
| \w     | 字母或数字                | '\w\w\d' 匹配 'py3'               |
| .      | 任意字符                  | 'py.' 匹配 'pyc'、'py!'           |
| \*     | 人一个字符串（包括 0 个） |                                   |
| +      | 至少 1 个字符             |                                   |
| ?      | 0 个或 1 个字符           |                                   |
| {n}    | n 个字符                  | '\d{3}' 匹配 '010'                |
| {n,m}  | n ~ m 个字符              | '\d{3,8}' 匹配 '1234567'          |
| \      | 转义字符                  | '\d{3}\-\d{3,8}' 匹配 '010-12345' |
| \s     | 空格、空位符              |                                   |

## 进阶

| 描述符 | 作用        | 示例                                           |
| ------ | ----------- | ---------------------------------------------- |
| []     | 表示范围    | '[0-9a-zA-Z\_]' 匹配任意一个数字、字母或下划线 |
| A\|B   | 匹配 A 或 B |                                                |
| ^      | 行的开头    | '^\d' 表示以数字开头                           |
| \$     | 行的结束    | '\d\$' 表示以数字结束                          |

## re 模块

Python 字符串本身用`\`转义，正则表达式也用`\`转义，在拼写正则表达式时使用`r`前缀可以忽略掉 Python 本身字符串的转义

### match

```python
>>> import re
>>> re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
<re.Match object; span=(0, 9), match='010-12345'>
>>> re.match(r'^\d{3}\-\d{3,8}$', '010 12345')
>>>
```

当匹配成功时，返回一个 Match 对象，否则返回 None

### split

```python
>>> re.split(r'\s+', 'a b   c')
['a', 'b', 'c']
>>> re.split(r'[\s\,\;]+', 'a,b;; c  d')
['a', 'b', 'c', 'd']
```

通过模式分割字符串，返回分割的数组

### group

```python
>>> m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
>>> m
<re.Match object; span=(0, 9), match='010-12345'>
>>> m.group(2)
'12345'
>>> m.group(1)
'010'
>>> m.group(0)
'010-12345'
```

通过`()`提取分组子串，`group(0)`表示匹配的全部字符串，`group(n)`表示第 n 个子串

### 贪婪匹配

匹配尽可能多的字符

```python
>>> re.match(r'^(\d+)(0*)$', '102300').groups()
('102300', '')
>>> re.match(r'^(\d+)(0+)$', '102300').groups()
('10230', '0')
```

正则匹配默认是贪婪匹配，想要非贪婪匹配（尽可能少匹配），在`\d+`后加`?`

```python
>>> re.match(r'^(\d+?)(0*)$', '102300').groups()
('1023', '00')
```

### 编译

`re`模块执行步骤：

1. 编译正则表达式，不合法则报错
2. 用编译后的正则表达式匹配字符串

**预编译**

```python
>>> import re
>>> re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
>>> re_telephone.match('010-12345').groups()
('010', '12345')
>>> re_telephone.match('010-8086').groups()
('010', '8086')
```

> 匹配简单邮箱

```python
def is_valid_email(addr):
    if re.match(r'(^[a-zA-Z\.]+)\@(gmail|microsoft)\.com$', addr):
        return True
    else:
        return False
```

> 匹配带名称邮箱，提取名称

```python
def name_of_email(addr):
    # 提取邮箱前缀
    m = re.match(r'^([a-zA-Z\d\s\<\>]+)\@(voyager|example)\.(org|com)$', addr)
    if not m:
        return None
    # 提取前缀中 <> 里面的名称，若不存在，则取全名
    m = re.match(r'^\<([a-zA-Z\s]+)\>[\s]+[a-zA-Z\d]+|([a-zA-Z\d]+)$', m.group(1))

    return m.group(1) if m and m.group(1) else m.group(2)
```

# 十五、常用内建模块

无需安装和配置即可使用

## datetime

处理日期和时间的模块

```python
# 前一个 datetime 是模块，后一个是类
from datetime import datetime
```

**now()**

```python
>>> datetime.now()
datetime.datetime(2020, 11, 22, 10, 42, 2, 59763)
```

**datetime()**

```python
>>> dt = datetime(2020, 11, 22, 10, 30)
>>> dt
datetime.datetime(2020, 11, 22, 10, 30)
```

**timestamp**

1970 年 1 月 1 日 00:00:00 UTC+00:00 时区的时刻为`epoch time`(新纪元时间)，当前时间是相对于`epoch time`的秒数，称为`timestamp`

`timestamp`的值与时区无关

```python
>>> dt = datetime(2020, 11, 22, 10, 30)
# datetime 转 timestamp
>>> t = dt.timestamp()
# timestamp 转 datetime 本地时间
>>> dt = datetime.fromtimestamp(t)
# timestamp 转 datetime utc 时间
>>> dt_utc = datetime.utcfromtimestamp(t)
```

**strptime()**

`str`转`datetime` [时间格式](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior)

```python
>>> cday = datetime.strptime('2020-11-22 10:20:20', '%Y-%m-%d %H:%M:%S')
```

**strftime()**

`datetime`转`str`

```python
>>> datetime.now().strftime('%a,%b %d %H:%M')
'Sun,Nov 22 11:38'
```

**timedelta**

```python
>>> from datetime import timedelta
# 减 2天 2 小时
>>> datetime.now() - timedelta(days=2, hours=2)
datetime.datetime(2020, 11, 20, 9, 41, 8, 544137)
```

**timezone**

通过`timedelta`创建`timezone`

```python
>>> from datetime import timezone
# 创建时区 UTC+8:00
>>> tz_utc_8 = timezone(timedelta(hours=8))
>>> dt = datetime.now()
# 强制设置时区 为 UTC+8
>>> dt = dt.replace(tzinfo=tz_utc_8)
datetime.datetime(2020, 11, 22, 12, 4, 41, 559771, tzinfo=datetime.timezone(datetime.timedelta(seconds=28800)))
```

**时区转换**

`utcnow()`可以获得当前 UTC 时间，给 UTC 时间设置好时区后，利用`astimezone()`可以转换任意时区的时间

```python
>>> utc_now = datetime.utcnow().replace(tzinfo=timezone.utc)
>>> utc_8_now = utc_now.astimezone(timezone(timedelta(hours=8)))
>>> utc_9_now = utc_8_now.astimezone(timezone(timedelta(hours=9)))
```

不是必须从 UTC+0:00 时区转换到其他时区，任何带有时区的时间都可以正确的转换

## colections

内建模块集合

### namedtuple()

`namedtuple()`可以用来创建一个`tuple`对象，并规定`tuple`元素的个数，从而使用属性而不是索引的方式应用元素

```python
>>> rom collections import namedtuple
>>> Point = namedtuple('Point', ['x', 'y'])
>>> p = Point(1, 2)
>>> p.x
1
>>> p[0]
1
```

`Point`对象是`tuple`对象的子类

### deque

实现来高效插入和删除（相对 list，list 是线性存储）的双向列表

```python
>>> from collections import deque
>>> q = deque(['a', 'b', 'c'])
>>> q.append('x')
>>> q.appendleft('y')
>>> q
deque(['y', 'a', 'b', 'c', 'x'])
```

append 和 pop 操作列表的末尾
appendleft 和 popleft 操作列表的开头

### defaultdict

含默认值的`dict`，与`dict`的使用相同

```python
>>> from collections import defaultdict
# 默认值使用函数设置
>>> dd = defaultdict(lambda :'N/A')
>>> dd['key']
'N/A'
```

### OrderedDict

以`Key`插入的顺序排序的`dict`

```python
>>> OrderedDict(a=1, b=2, c=3)
OrderedDict([('a', 1), ('b', 2), ('c', 3)])
```

`FIFO`

```python
from collections import OrderedDict


class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):

        containKey = 1 if key in self else 0
        print(len(self))
        if len(self) - containKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)
```

### ChainMap

将多个`dict`对象串起来，在查找的时候，实际按照内部`dict`顺序一次查找

```python
from argparse import Namespace
from collections import ChainMap
import os, argparse

defauts = {'user': 'guest', 'color': 'red'}

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k: v for k, v in vars(namespace).items() if v}
# 查找时，现在 command_line_args 中查找，如果没有，再在 os.environ 查找，最后时 defaults
combined_args = ChainMap(command_line_args, os.environ, defauts)

print('color=%s' % combined_args['color'])
print('user=%s' % combined_args['user'])
```

### Counter

计数器，实际也是一个`dict`子类

```python
from collections import Counter
c = Counter

# 手动统计
for ch in 'programing':
    c[ch]=c[ch]+1

# 自动添加
c.update('hello')
```

## base64

`Base64`是一种任意二进制到文本字符串的编码方法，常用于小段`URL`，`Cookie`，数字签名等

对二进制数据，每 3 字节一组，按没 6 bit 分为 4 组，从 64 个预设好的字符找到对应编码，不足 3 字节的末尾加一个或两个`\x00`，再在编码后的末尾加上 1 或 2 个`=`标记，解码时自动去掉

```python
>>> import base64
>>> base64.b64encode(b'binary\x00string')
b'YmluYXJ5AHN0cmluZw=='
>>> base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
b'binary\x00string'
# 对比 urlsafe，将 + 和 / 分别变成 - 和 _
>>> base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
b'abcd++//'
>>> base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
b'abcd--__'
>>> base64.urlsafe_b64decode(b'abcd--__')
b'i\xb7\x1d\xfb\xef\xff'
```

`url`中`=`也需要去掉

## struct

用来处理`bytes`与其他二进制数据的转换

```python
>>> n = 10240099
>>> b1 = (n & 0xff000000) >> 24
>>> b2 = (n & 0xff0000) >> 16
>>> b3 = (n & 0xff00) >> 8
>>> b1 = (n & 0xff)
>>> bs = bytes([b1, b2, b3, b4])
>>> bs
b'\x00\x9c@c'
```

```python
>>> import struct
>>> struct.pack('>I', 10240099)
b'\x00\x9c@c'
```

```python
>>> struct.unpack('>I', b'\x00\x9c@c')
10240099
```

`>` 表示字节顺序是 big-endian，即网络序，`I`表示 4 字节无符号整数

[`struct`模块定义的数据类型](https://docs.python.org/3/library/struct.html#format-characters)

## hashlib

### 摘要算法

又叫哈希算法，散列算法，通过一个函数，把任意长度的数据转换成一个长度固定的数据串（通常是 16 进制字符串）

```python
>>> import hashlib
>>> md5 = hashlib.md5()
# 可分多次调用 update
>>> md5.update('how to use md5 in '.encode('utf-8'))
>>> md5.update('python hashlib?'.encode('utf-8'))
# 提取 16 进制摘要
>>> print(md5.hexdigest())
d26a53750bc40b38b65a520292f69306
```

`sha1`、`sha256`、`sha512`的调用方式与`md5`完全一致，它们更加安全，但更慢，所得摘要更长

**碰撞**

两个不同的数据通过某个摘要算法得到了相同的摘要，叫做碰撞，这是有可能的（因为任何摘要算法都是把无限的数据集合映射到有限的集合中）

### 摘要的应用

用于生成密文的口令存储于数据库

经过混入`salt`和唯一且不可修改的`ID`，再求哈希值，这样存储会更安全

摘要算法不是用来加密的，因为无法反推明文，只是用于防篡改的

## hmac

Keyed-Hashing for Message Authentication

通过标准的算法，把`key`混入计算过程

```python
>>> import hmac
>>> message = b'hello world'
>>> key = b'secret'
>>> h = hmac.new(key, message, digestmod='MD5')
# 如果 message 很长，可以分多次调用 h.update(msg)
>>> h.hexdigest()
'78d6997b1230f38e59b6d1642dfaa3a4'
```

## itertools

用于操作迭代对象的函数

**count(n)**

创建一个无限迭代器，起始于`n`，每次加 1

```python
import itertools
# 自然数
natuals = itertools.count(1)
```

**cycle(list)**

创建一个无限迭代器，无限重复传入的序列

```python
# 无限重复'A','B','C'
cs = itertools.cycle('ABC')
```

**repeat(item)**

创建一个无限迭代器，无限重复传入的一个元素，第二个参数可以限定重复的次数

```python
ns = itertools.repeat(123, 3)
```

**takewhile()**

传入一个筛选函数，用来截取子序列

与`filter`不同，当函数条件第一次不满足后，不再继续迭代

调用所得是一个`itertools.takewhile`迭代对象

```python
>>> ns = itertools.takewhile(lambda x: x<=10, natuals)
>>> list(ns)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

**chain()**

将一组迭代对象串联起来

```python
cn = itertools.chain('ABC', 'XYZ')
```

**groupby()**

把相邻的重复元素调出分到一组，`group`是`itertools._grouper`迭代对象

```python
>>> for key, group in itertools.groupby('aaabbbccaaa', lambda c: c.upper()):
...     print(key, list(group))
...
A ['a', 'a', 'a']
B ['b', 'b', 'b']
C ['c', 'c']
A ['a', 'a', 'a']
```

可以传入一个函数座位第二参数，元素通过函数处理后再作用于`groupby`

**圆周率**

```python
def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    natuals = itertools.count(1)
    odd = filter(lambda x: x % 2 > 0, natuals)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    odd = itertools.takewhile(lambda x: (x + 1) // 2 <= N, odd)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    items = map(lambda x: (4 / (x if (((x + 1) // 2) % 2 > 0) else (0 - x))),
                odd)
    # step 4: 求和:
    return sum(items)
```

## contextlib

只要实现了上下文管理，任何对象都可以使用`with`语句

### \_\_enter\_\_ 和 \_\_exit\_\_

```python
class Query(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('begin')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('query info about %s...' % self.name)


with Query('bob') as q:
    q.query()
```

使用`with`语句时，自动调用 \_\_enter\_\_ 和 \_\_exit\_\_

### @contextmanager

```python
class Query2(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print('query info about %s...' % self.name)


@contextmanager
def create_query(name):
    print('begin')
    q = Query2(name)
    yield q
    print('end')


with create_query('bob') as q:
    q.query()
```

`with`语句会先执行`yield`之前的语句，`yield`调用会执行`with`语句内部的语句，最后执行`yield`之后的语句

### closing

`closing`是一个经过`@contextmanager`装饰的`generator`

```python
@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
```

针对 Python 中读写资源使用完一定要正确关闭的问题，更简单的方式是使用 `closing`

```python
from contextlib import closing
from urllib.request import urlopen
# closing 将 没有实现上下文管理的对象变为上下文对象
with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)
```

## urllib

用于操作`URL`

### GET

```python
from urllib import request

req = request.Request('http://dict.youdao.com/w/odd/#keyfrom=dict2.top')
# 模拟 iphone OS 8.0 发起请求
req.add_header(
    'User-Agent',
    'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25'
)
with request.urlopen(req) as f:
    data = f.read()
    print('status:', f.status, f.reason)
    for k, v in f.getheaders():
        print(f'{k}: {v}')
    print('data:'.data.decode('utf-8'))
```

### POST

```python
email = 'aaa.foxmail.com'
pwd = '123456'
login_data = parse.urlencode([
    ('username', email), ('password', pwd), ('entry', 'mweibo'),
    ('client_id', ''), ('savestate', '1'), ('ec', ''),
    ('pagerefer',
     'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F'
     )
])

req = request.Request('https://passport.weibo.cn/sso/login')
# Origin 说明请求从哪里发起的，包括，且仅仅包括协议和域名
req.add_header('Origin', 'https://passport.weibo.cn')
# User-Agent 表示 HTTP 客户端程序的信息
req.add_header(
    'User-Agent',
    'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25'
)
# Referer 表示 请求中 URI 的原始获取方
req.add_header(
    'Referer',
    'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F'
)

# data 参数以 bytes 传入
with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
```

### Handler

通过代理访问

```python
proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
with opener.open('http://www.example.com/login.html') as f:
    pass
```

## XML

### DOM

把整个`XML`读入内存，解析为树，占内存大，解析慢

### SAX

流模式，占内存小，解析块，需要自己处理事务

```python
from xml.parsers.expat import ParserCreate


class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)


xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
# 可能会被分为多次调用，需要在 EndElementHandler 处合并
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)
```

通过 start 找到需要的节点，把节点数据保存起来，在 end 处对数据合并并做处理

## HTMLParser

编写搜索引擎，先爬取目标网页，然后解析页面，获取内容

`HTML`是`XML`的子集，是不严谨的`XML`

解析`HTML`的方式与`SAX`解析`XML`类似，自定义继承自`HTMLParser`的类，实现相关事件的相应

```python
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)


parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')
```

`feed()`可以分多次调用

# 十六、常用第三方模块

`PyPI`

the Python Package Index，所有第三方模块都会在此注册

## Pillow

[官方文档](https://pillow.readthedocs.org/)

```shell
$ pip install pillow
```

**操作图片**

```python
from PIL import Image, ImageFilter

# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('test.jpg')
# 获得图像尺寸:
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%:
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
im.save('thumbnail.jpg', 'jpeg')

# 应用模糊滤镜:
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')
```

**绘图**

```python
from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象，可以根据操作系统提供绝对路径
font = ImageFont.truetype('Arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
```

## requests

比`urllib`方便丰富的网络资源访问模块

```shell
$ pip install requests
```

```python
import requests
r = requests.get('https://www.douban.com/')
# 返回状态码
r.status_code
# 返回内容
r.text
# 带参请求，传一个 dict 给 params
r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
# 获取编码
r.encoding
# 获取 bytes 对象的响应内容
r.content
# 直接获取 JSON 类型的响应内容
r.json()
# 需要传入 HTTP Header 时，传入一个 dict 给 headers
r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
# POST 请求只需将 get 变为 post，data 参数以 dict 传入
r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
# 默认使用 application/x-www-form-urlencoded 对 POST 数据编码，如需传递 JSON 数据，可直接使用 json 传入
r = requests.post(url, json={'key': 'value'})

# 上传文件
upload_files = {'file': open('report.xls', 'rb')}
r = requests.post(url, files=upload_files)

# 响应头
r.headers
# 获取指定 cookie
r.cookies['ts']

# 以 dict 传入 cookies
r = requests.get(url, cookies={'token':'12345', 'status': 'working'})

# 2.5秒后超时
r = requests.get(url, timeout=2.5)
```

## chardet

对未知编码的 bytes 进行编码猜测（通过特征字符的判断）

```shell
pip install chardet
```

```python
>>> chardet.detect(b'Hello world')
{'encoding': 'ascii', 'confidence': 1.0, 'language': ''}
```

## psutil

process and system utilities，跨平台系统监控模块

```shell
pip install psutil
```

**CPU**

```python
import psutil
# CPU逻辑数量
psutil.cpu_count()
# CPU物理核心
psutil.cpu_count(logical=False)
# CPU的用户／系统／空闲时间
psutil.cpu_times()
# CPU 使用率
psutil.cpu_percent(interval=1, percpu=True)
```

**Memory**

```python
# 物理内存信息
psutil.virtual_memory()
# 交换区信息
psutil.swap_memory()
```

**Disk**

```python
# 磁盘分区信息
psutil.disk_partitions()
# 磁盘使用情况
psutil.disk_usage('/')
# 磁盘 IO
psutil.disk_io_counters()
```

**Network**

```python
# 获取网络读写字节／包的个数
psutil.net_io_counters()
# 获取网络接口信息
psutil.net_if_addrs()
# 获取网络接口状态
psutil.net_if_stats()
网络连接信息
psutil.net_connections()
```

**process**

```python
# 所有进程ID
psutil.pids()
# 获取指定进程ID=3776，其实就是当前Python交互环境
p = psutil.Process(3776)
# 进程名称
p.name()
# 进程exe路径
p.exe()
# 进程工作目录
p.cwd()
# 进程启动的命令行
p.cmdline()
# 父进程ID
p.ppid()
# 父进程
p.parent()
# 子进程列表
p.children()
# 进程状态
p.status()
# 进程用户名
p.username()
# 进程创建时间
p.create_time()
# 进程终端
p.terminal()
# 进程使用的CPU时间
p.cpu_times()
# 进程使用的内存
p.memory_info()
# 进程打开的文件
p.open_files()
# 进程相关网络连接
p.connections()
# 进程的线程数量
p.num_threads()
# 所有线程信息
p.threads()
# 进程环境变量
p.environ()
# 结束进程
p.terminate()
# 模拟 ps 命令效果，查看当前所有进程状态
psutil.test()
```

# 十七、virtualenv

用于创建独立的 python 运行环境，解决模块多版本冲突问题

使用`source`进入`virtualenv`环境时，`virtualenv`会修改相关环境变量，让`python`和`pip`命令均指向当前`virtualenv`环境

```shell
# 不复制系统 python 环境中的第三方包
$ virtualenv --no-site-package venv
# 进入创建的 python 环境
$ source venv/bin/activate
# 退出当前 python 环境
$ deactivate
```

# 十八、图形界面

## Tkinter

Tkinter 封装了访问 Tk 的接口，Tk 是一个图形库，使用 Tcl 语言开发，支持多操作系统，Tk 会调用操作系统提供本地 GUI 接口

复杂的 GUI 用操作系统原生语言或库编写

```python
from tkinter import *
import tkinter.messagebox as messagebox


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        # 将 widget 加到父容器
        self.nameInput.pack()
        # 点击触发 hello
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)


app = Application()
# 设置窗口标题
app.master.title('Hello World')
# 主消息循环
app.mainloop()
```

## turtle

[官方文档](https://docs.python.org/3.3/library/turtle.html#turtle-methods)

```python
def draw_star(x, y):
    pu()
    goto(x, y)
    pd()
    # set heading: 0
    seth(0)
    for i in range(5):
        fd(40)
        rt(144)


for x in range(0, 250, 50):
    draw_star(x, 0)

done()
```

# 十九、网络编程

网络通信就是两个进程之间的通信

## TCP/IP 简介

`IP 地址` 计算机的网络接口，通常是网卡，可有多个，是 32 位整数（IPv4），IPv6 是 128 位整数

`IP 协议` 负责把数据从一台计算机通过网络发送到另一台计算机，数据被分割成小块，IP 包特点是速度快，途径多个路由，不保证到达，也不保证顺序

`TCP 协议` 在 IP 协议基础上，负责在两台计算机上建立起可靠连接，保证数据包顺序到达。对每个 IP 包编号，顺序发收，失败的自动重发

`TCP 报文` 传输的数据，源 IP、目标 IP、源端口号、目标端口号

HTTP 协议、SMTP 协议都建立在 TCP 协议基础上

一个进程可能与多个计算机建立连接，因此可能申请很多个端口

## TCP 编程

`Socket`通常是表示打开一个网络链接，需要知道目标计算机的 IP 地址、端口号，还有指定协议类型

### 服务端

一个服务端`Socket`依赖 4 项确定唯一：服务器地址，服务器端口，客户端地址，客户端端口

服务端接收的每个连接需要一个新进程/线程来处理，否则服务器一次只能服务一个客户端

```python
import socket, threading, time
# 创建一个 Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定地址和端口
# 0.0.0.0 是广播地址，集所有网络地址
# 127.0.0.1 表示本机地址
s.bind(('localhost', 6666))
# 开始监听，5 是最大连接数
s.listen(5)
print('Waiting for connection...')

def tcplink(sock, addr):
    print('accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome.')

    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        print(f"receive, {data.decode('utf-8')}")
        sock.send(('hello, %s.' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('connection from %s:%s closed.' % addr)

# 通过永久循环接收客户端连接
while True:
    # 接收并返回一个客户端连接
    sock, addr = s.accept()
    # 构造一个线程处理这个连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    # 启动线程
    t.start()
```

### 客户端

```python
import socket
# AF_INET 表示 IPv4
# SOCK_STREAM 表示 TCP 协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# HTTP 协议规定客户端必须先发起请求，由服务端接收后再发送数据给客户端
# 端口 1024 以内为标准端口，如 SMTP 25，FTP 21
s.connect(('localhost', 6666))
# 接收指定长度的字节数据
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
```

用 TCP 协议进行 Socket 编程，客户端需要主动连接服务器 IP 和端口，服务端需要先监听指定端口，通常服务器程序会无限运行下去，同一个端口 Socket 绑定后，就不能被另一个 Socket 绑定（同协议类型）

## UDP 编程

相对 TCP 的可靠连接，UDP 是面向无连接的协议，UDP 协议知道对方 IP 和端口就能发送数据包，但不能保证送达，速度快

### 服务端

```python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# UDP 不需要listen()，直接接收
s.bind(('localhost', 6666))

print('bind udp on 6666...')

while True:
    # 返回数据和客户端IP、端口
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    # 向客户端回发
    s.sendto(b'Hello, %s.' % data, addr)
```

### 客户端

```python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in [b'Michael', b'Tracy', b'Sarah']:
    # 不需要 connect()
    s.sendto(data, ('localhost', 6666))
    print(s.recv(1024).decode('utf-8'))
s.close()
```

**服务器绑定相同的 UDP 端口和 TCP 端口不冲突**

# todo:

1. JIT 技术
2. dict 的实现原理
3. @property 的实现
4. open() 模式的`+`
5. Python 利用多线程使用多核 CPU（GIL）
6. BaseManager 的实现，为什么只能在 if \_\_name\_\_ == '\_\_main\_\_': 下调用
7. deque 的实现原理
8. struct 的数据类型
9. 生成器实现协程的原理
