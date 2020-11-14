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
>>> from  collections.abc import Iterator
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

# todo:

1. JIT 技术
2. dict 的实现原理
