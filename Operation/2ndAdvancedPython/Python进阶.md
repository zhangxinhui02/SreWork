# 正则表达式

## 快速入门

> **我们用正则表达式,就是用一套规则来描述我们对于所需文本目标。然后通过程序去获取到目标。**

+ 平时命令行操作时的通配符

```shell
# 简单的匹配方法
rm -f *.txt
# 稍微复杂一点,就需要正则表达式:比如要求只允许用户名包含字符、数字、下划线和连接字符就需要如下描述:
[a-zA-Z0-9]{1,}[_-!]*
```

+ 单个字符的描述

```shell
# 表达某些类型字符的集合
[a-z0-9]  # 只匹配小写字母和数字
[^ABC]    # 表示除了ABC之外的所有字符
\w        # 与[A-Za-z0-9_]等价
\s        # 空白符(空格,制表符,换行符等)
\S        # 非空白符
```

+ 特殊符号

| 特殊       符号 | 描述                                                         |
| :-------------: | :----------------------------------------------------------- |
|        $        | 匹配输入字符串的结尾位置,**注意这里不同的环境下的正则可能有换行符匹配的问题** |
|       ( )       | 标记一个**子表达式**的开始和结束位置(**分组**)。             |
|        *        | 匹配前面的子表达式零次或多次。                               |
|        +        | 匹配前面的子表达式一次或多次。                               |
|        .        | 匹配除换行符 \n 之外的任何**单字符**。要匹配 . ，请使用 \. 。 |
|        [        | 标记一个中括号表达式的开始。要匹配 [，请使用 \[。            |
|        ?        | 匹配前面的子表达式**零次或一次**，或指明一个**非贪婪限定符**。要匹配 ? 字符，请使用 \?。 |
|        \        | 将下一个字符标记为或特殊字符、或原义字符、或向后引用、或八进制转义符。例如， 'n' 匹配字符 'n'。'\n' 匹配换行符。序列 '\\' 匹配 "\"，而 '\(' 则匹配 "("。 |
|        ^        | **不在方括号里使用时匹配输入字符串的开始位置**。当该符号在方括号表达式中使用时，表示不接受该方括号表达式中的字符集合。要匹配 ^ 字符本身，请使用 `\^`。 |
|        {        | 标记限定符表达式的开始**(用于限定表达式的个数)**。要匹配 {，请使用 `\{`。 |
|       \|        | 指明两项之间的一个选择。要匹配 \|，请使用 `\|`。             |

+ 演练一下

```shell
# 匹配1~99的正整数
[0-9]{1,2}   # 09,08这样的数也会被匹配到
[1-9][0-9]?  # 首字母不能出现0

# 如果出现了不同长度的满足匹配的文本,则出现了贪婪性问题
# 匹配第一个h1标签:<h1> redrock </h1>
<.*>  # 贪婪,第一个<
<.*?> # 
```

+ 定位符

| 字符 | 描述                                                         |
| :--- | :----------------------------------------------------------- |
| ^    | 匹配输入字符串开始的位置。如果设置了 RegExp 对象的 Multiline 属性，^ 还会与 \n 或 \r 之后的位置匹配。 |
| $    | 匹配输入字符串结尾的位置。如果设置了 RegExp 对象的 Multiline 属性，$ 还会与 \n 或 \r 之前的位置匹配。 |
| \b   | 匹配一个单词边界，**即字与空格间的位置**。                   |
| \B   | 非单词边界匹配。                                             |

```shell
# 匹配le 这个部分
apple leave
尝试一下 \ble 和 le\b的区别 
```

## re模块

> 这是python自带的正则表达式模块。注意事项:在re模块中的 pattern 一定要使用原始字符串。

+ 几个常用的函数

```python
# re.match
def match(pattern, string, flags=0):
 """Try to apply the pattern at the start of the string, returning
    a match object, or None if no match was found."""

# re.search
def search(pattern, string, flags=0):
"""Scan through string looking for a match to the pattern, returning a match object, or None if no match was found."""

# 想想 match 和 search两个函数的区别。
# re.findall:字面意思
```

+ 查询结果的使用

```python
res = re.search(pattern,content,flag)
# 查询的结果
res.span()  # 找到的匹配到的起始和截至位置 
res.group() # 找到匹配的字符串,若里面加了参数,则代表找到匹配到的分组
```

+ 更标准的使用方法

```python
r = re.complie("mypattern") # 返回一个对象
# 2.再进行调用
res = r.search(text)
# 3.最后再对res进行操作
res.group()
```

# 语法部分

## 文件操作

### 编码小常识

> 在 Python3 中对于字节流和字符串做了严格区分，分别用 str 表示字符串，主要用于展示给人看。byte 表示字节序列，任何需要写入文本或者网络传输的数据都只接收字节序列。

![](https://gitee.com/lzd-1230/img-host/raw/master/image/20211217233824.png)

其中字符串就是我们平时看到的这些汉字，英文等等，但是当要保存到文件的时候，都需要进行这样的`encode`操作,因为计算机只认识这种二进制的原始数据。

那么我们平时看到的字符编码方式有两大类，我们C语言课中应该有提到一种叫做`ASCII`码的方式。这种方式下，一个字符用一个字节(8位)表示。

但是在python中我们默认使用`Unicode`,其使用两个甚至是更多个字节来完成字符的编码，那么我们平时所熟悉的`utf-8`和`gbk`就是其中的两种编码方式。

![](https://gitee.com/lzd-1230/img-host/raw/master/image/20211218000845.png)

### 基本操作

+ 文件打开时

```python
# 首先要注意我们使用的文本处理模式
t:以字符串为单位,使用时记得指定编码方式
b:以字节为单位(二进制的形式)

# 然后是对文件的操作方式
r:只读
    若文件不存在则抛出异常
w:写
    如果文件不存在则会自动创建,若文件存在则清空内容(慎用)
a:追加写(演示)
    若文件存在则会将文件指针移动到最后!然后内容进行追加

+:跟在前面模式的后面,表示同时可读可写
    
# 用with打开一个文件,可以在with内部代码执行完毕后自动释放(推荐使用方式)

# 具体打开的函数与代码
f = open(path=<>,mode=<>,encoding=<>)

with open(path=,mode=,encoding=) as f: # 最终f就是拿到的文件句柄
    pass
# 注意这里的文件句柄的含义就是我们代码对文件操作的入口,因为我们应用程序对文件的操作都需要操作系统来帮我们完成,而不能直接操控文件。

# 一个系统可以用的文件句柄数目是有限的,因此记得使用完文件需要手动关闭,或者用with帮你自动关了
```

+ 对文件的操作

```python
# 读操作
f.read()  			# 读取文件所有内容,文件指针会移动到最后
f.readline() 		# 每次读取一行,在读取大文件的时候,无法一次性读取完
f.readlines()		# 读取所有,并保存为列表

# 写操作
f.write() 			# 注意使用的是a模式还是w模式,如果是w模式则会清空文件后再写
```

### 文件指针

> 打开文件后,在文件内操作的作用点。

```python
#大前提:文件内指针的移动都是Bytes为单位的,除了t模式下的read(n),n以字符为单位
with open('a.txt',mode='rt',encoding='utf-8') as f:
     data=f.read(3) # 读取3个字符

with open('a.txt',mode='rb') as f:
     data=f.read(3) # 读取3个Bytes

# f.tell():查看当前文件指针距离文件开头的位置
        
# 之前文件内指针的移动都是由读或写操作而被动触发的，若想读取文件某一特定位置的数据，则需要用f.seek方法主动控制文件内指针的移动，详细用法如下：

# --------f.seek(<指针移动的字节数>,<模式控制>) -----------
# 模式控制:
# 0: 默认的模式,该模式代表指针移动的字节数是以文件开头为参照的
# 1: 该模式代表指针移动的字节数是以当前所在的位置为参照的
# 2: 该模式代表指针移动的字节数是以文件末尾的位置为参照的
# 注意:其中0模式可以在t或者b模式使用,而1跟2模式只能在b模式下用
```

思考一下我们平常用的 `head` 和 `tail `命令与文件指针的关系。

### 文件编码问题

+ 在open未显示指明编码方式的时候，不同操作系统有不同的默认值

  + Linux/mac：`utf-8`
  + Windows: `gbk`

  大家可以下去试试不同的编解码方式显示出来的数据会是什么样子

## 函数

> python 中的函数名，与 C 中的函数名类似(指针)，都表示具体表现如下

+ 函数名可以放在任何位置

```python
def my_print(x):
    print(x)

# 可以直接被赋值
MY_PRINT = my_print
MY_PRINT("hhh")

# 可以放在字典里
func_dict = {"p":my_print,"real_p":print}
func_dict["p"]("hhh")

# 可以是返回值,可以是参数......

# 例如 sorted 函数
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
my_sorted = sorted(L,key=lambda ele:ele[0])

# lambda 表达式写法
lambda <参数>:<返回值>

# 大家想一想sorted如何对字典进行排序呢?
```

### 函数参数

+ 函数参数分为以下几个要求
  + 传入时是否必须命名
  + 是否**可变长度**
  + 是否有**默认值**
+ 特殊符号`*`的使用

```python
"""不定长参数"""
def add(*args):
    Sum = 0
    for i in args: # 这里以元组的形式传入
        Sum += i
    return Sum

print(add(1,2,3,4))

"""可变长关键字参数 keyword args"""
def show_val(**kwargs):
    print(kwargs)
show_val(x=2,y=3,z=4)

"""从某一个变量开始之后为关键字参数"""
def forec_key(x,y,*,z):
    print(f"x:{x} y:{y} z:{z}")
forec_key(1,2,z=3) # 最后一个参数必须时命名参数

# 思考如果我们想要函数中所有参数都是关键词参数如何做到?

"""默认参数"""
def myprint(x=1122):
    print(x)
    
# 思考如果我们将默认参数设为一个变量,那么变量发生改变的时候,默认值会变吗?
	不会,函数在创建的时候就会弄好自己的名称空间
    啥是名称空间?? 放变量的地方
```

## 闭包

> 用到了外层名称空间(不算全局区)的变量的函数

+ 函数名称空间在定义之初就已经决定

```python
# 版本一:理解局部变量和全局变量
res = 1
def fun1():
    def fun2():
        res = 3 # 把它干掉呢?
        print(res)
    return fun2

fun = fun1()
fun()

# 版本二:理解作用域的生成时期,一定是在函数定义的时候,其变量的引用就已经确定好了的
def fun3():
	res = 999
    fun2 = fun1()
    fun2()
fun3()
```

+ 闭包的概念:函数用到了函数外面设置好的变量(**非全局变量**)
  + 闭: 某个函数的内部
  + 包: 代表变量对于内部函数来说是在外面

```python
x=1
def outer():
    x=2
    def inner():
        print(x)
    return inner

func=outer()
func() # 结果为2,因为作用域的优先级是由内向外的
```

+ 闭包拿来干啥?

```python
# 如果一个函数多次被传入某个参数,则可以使用闭包的传参方式
def liner(k,b):
    def cal(x):
        return k*x+b  # 对里面这个我真正需要的函数来说,就相当于拿到了参数的引用
    return cal
 
my_liner = liner(3,2)
my_liner(1) # output = 5
```

## 函数装饰器

> 软件的开发过程应该遵从扩展的开放与修改的封闭。即对于最初的代功能代码的调用方式以及源码等，不应该进行修改。但我们仍需要对代码进行扩展，这个时候就有装饰器来了。

### 无参装饰器

现考虑给某一个函数添加代码**时间检测**的功能

```python
import time

# 我们已经写好的功能函数
def myfun():
    time.sleep(1)
    return "hhh"

# 给它加上计时功能
def wrapper(func):
    start = time.time()
    res = func()  # 调用了原来那个函数
    end = time.time()
    print(f"{end - start}s")
    return res
```

那么刚刚做好的新函数怎么使用呢?

```python
wrapper(myfun) 
```

我们**还是把函数名给它改掉了**,如何做到只改功能,不改名字呢?

```python
def timer(func): # 第一层的目的,可以给多种函数装饰
	def wrapper():
        start = time.time()
		res = func()
		end = time.time()
		print(f"{end - start}s")
		return res
	return wrapper

myfun = timer(myfun) # 这里的参数传入的是我们要加入的函数
myfun()
```

那假如我 `myfun` 函数需要传入参数怎么办?

```python
# 装饰器的定义 
def timer(func): # 其参数意义为什么?
	def wrapper(*args,**kwargs): # 其参数意义为什么?
        start = time.time()
		res = func(*args,**kwargs) # 注意自行了解一下传入参数中*的含义和用法
		end = time.time()
		print(f"{end - start}s")
		return res
    return wrapper
```

> 上述部分为无参装饰器的原理部分，在使用的时候我们更喜欢使用语法糖

```python
@timer # 装饰器已经提前定义好了
def myfun() # 在定义函数的位置给它加上功能，可以加多个装饰器
	...
```

多个装饰器叠加的时候如下

```python
@d3
@d2
@d1
def myfun():
    ...
# 等效于
myfun = d3(d2(d1(myfun)))
```

### 有参装饰器

如果对于某一个函数,需要跟据某一个参数来进行不同的修饰

```python
def auth(filetype): # 这一层的参数用来指定你可以对装饰有不同的选项
	def timer(func):
        def wrapper(*args,**kwargs):
            if(filetype == ".txt"):
                ...
            elif(filetype == ".jpg"):
                ...
            return res
        return wrapper
    return timer

# 调用时如何进行?
@auth(filetype = ".txt")
def myfun():
	...

```

# 面向对象

## 基本引入

> 面向对象的程序设计把计算机程序视为一组对象的集合，每个对象可以想象成一个特殊的数据类型,它拥有自己的数据以及对数据操作的方法。

+ 面向过程的实现

```python
# 任务:打印出学生的成绩
std1 = { 'name': 'Michael', 'score': 98 }
std2 = { 'name': 'Bob', 'score': 81 }
# 打印出学生成绩
def print_score(std):
    print('%s: %s' % (std['name'], std['score']))

print_score(std1)
print_score(std2)
```

+ 面向对象的实现

```python
# 定义这样一个类,里面包含了学生的数据以及方法
class Student():
    # 第一个参数是固定写法,且不用我们手动去传,但一定不能少
    def __init__(self, name, score):
        self.name = name
        self.score = score
	# 实例方法,可以被对象直接用.
    def print_score(self):
        print('%s: %s' % (self.name, self.score))

# 由类创建对象的过程
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

bart.print_score()
lisa.print_score()
```

+ `__init__函数`

由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的`__init__`方法，在创建实例的时候，就把`name`，`score`等属性绑上去

+ 在类中定义的函数(类方法,**实例方法**)

和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量`self`，并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。

## 封装性

> 可以看到,如果提供给你了一个类,就可以轻松地创建对象,并且调用其内部的方法来实现功能,并且无需知道其中实现的细节。可以把对象看成一个数据+方法的集合体。

+ 但是默认情况下，你仍然可以通过对象去修改这些属性

```python
bart.score = 100
```

+ 将初始化属性的前面加上`__`之后,就可以让属性对外隐藏起来

```python
class Student():
    # 第一个参数是固定写法,且不用我们手动去传
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

# 那么此时创建对象后对这两个属性的访问就会出错
# 其本质是python解释器对这两个属性名进行了修改
```

+ 封装的体现

```python
# 如果我们仍需要访问或者修改这样的变量就需要再定义一些实力方法
class Student():
    # 第一个参数是固定写法,且不用我们手动去传
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    # 通过调用方法来对属性进行修改与获取
    def set_name(self,new_name):
        if(type(new_name) == str):
	        self.__name = new_name
   	def get_name(self):
        return self.__name
    
# 注意这样做有很大的好处,我们可以做类型检查
# 回想之前讲到的f.write() 如果是以b方式打开的,那么传字符串进去就会报错
```

## 继承和多态

> 当我们定义一个class的时候，可以从某个现有的class继承，继承过后子类会拥有父类的属性与方法。

+ 继承会默认把父类的方法全部继承，属性则需要在构造函数中显示调用父类的构造函数，才有继承的效果。

```python
class People():
    def __init__(self,name,sex,height):
        self.name = name
        self.sex = sex
        self.__height = height
    def eat(self):
        print(f"{self.name} is eating")
    
class Student(People):
    def __init__(self, name, sex, height,score):
        super().__init__(name,sex,height)
        self.score = score
    
# 构造对象
stu = Student("Lihua","man","height",90)
print(stu.name)
stu.eat()
```

+ 多态：当子类可以有自己的个性，不想用父类的方法了，就可以自己定义一个同名的方法来覆盖其父类的方法。

```python
class People():
    def eat(self):
        print("这是People的吃饭")
        print(f"{self.name} is eating")
    
class Student(People):
    def eat(self):
        print("这是Student的吃饭")
        print(f"{self.name} is eating")
        # 注意这里同样可以使用super来调用父类的方法

class Teacher(People):
    def eat(self):
        print("这是Teacher的吃饭")
        print(f"{self.name} is eating")

# 同样我们可以使用super().eat()来调用父类的方法,以达到复用的效果
```

+ 多态的好处:当我们都继承了一个类之后,就只需要调用方法就行。

```python
def call_eat(peo):
    peo.eat()  # 不管传进来的是啥,我只管调用它的eat方法就可以了,具体的细节无需多虑

# 鸭子类型:只要它长得像鸭子->它就是鸭子
人话:只要类中实现了这个方法,我就拿来直接用
# Linux下的一切皆文件的实现原理:就是通过固定的结构体属性,给予不同的函数实现来做到的。
```

## 获取对象的信息

> 当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？

+ 类型判断

```python
# 使用type来查看其class的类型
type(1)
type("hahaha")

# 如何查看是否为函数,利用types里面定义好的常量
import types
def fun():
    pass
type(fun)==types.FunctionType  # True

# 对于有继承关系的可以使用isinstance
isinstance(<实例名>,<类名>)
考考大家isinstance(stu,People)返回什么
```

+ 对象属性判断

```python
# 判断对象是否拥有某些属性(在不清楚对象是否有这个属性的时候使用)
print(hasattr(stu, 'eat')) # 有方法eat吗
print(hasattr(stu,'name')) # 有属性name吗
print(hasattr(stu,'__height')) # 查看隐藏属性失败

# dir方法查看对象的所有属性
dir(stu)
```

## 魔法方法

> 很多python的内置函数其实在调用对象中的魔法方法,即:形如`__xxx__`的函数。

+ `len`函数

```python
len("123") # 返回3
len([1,2,3]) # 返回3

# 如果我们自己定义的People类中也想可以被len函数调用来返回身高,那么我们就需要实现
def __len__(self):
    return self.__height
```

+ `__slots__`属性

```python
class Student():
    __slots__ = ("name","age") # 限定这个类中只能有这两种属性,如果有多的就直接报错
```

+ `__str__`属性

```python
# 对一个普通的对象进行print(),会打印出一堆不是很好看的东西
class Student(object):
    def __init__(self, name):
         self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name

stu = Student("zhangsan")       
print(stu) # Student object (name: zhangsan)
```

+ `__iter__`

```python
class Fib():
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        return self.a # 返回下一个值
```

+ `__getitem__`

```python
# 如果想让自己的类也能够像列表一样被[]索引
class Fib():
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
```

## 实例属性和类属性

> 有时候,我们希望某些属性是属于整个类共有的,它可以让所有实例访问到。

```python
# 比如我们刚才的People类中如果希望有一个可以统计当前有多少人的属性
class People():
    count = 0  # 初始时默认给他赋值为0
    def __init__(self):
        People.count += 1
        pass
# 在外部，任何一个People构造出来的对象都可以访问这个属性
peo = People()
print(People.count) # 在内外的访问方法是一样的
```

注：千万不要给类属性和实例属性取一个同样的名字，否则会出现覆盖问题。

## 引用和对象

> python 中变量名和对象是分离的

+ 不可变数据对象(immutable object)：int，str，元组

![](https://gitee.com/lzd-1230/img-host/raw/master/image/20211218150333.png)

```python
a = 1 # 让a指向内存中的1对象
b = 1 # 让b也指向那个
# 使用id函数来查看对象指向的内存位置
print(id(a))
print(id(b))

# 当我们对a进行+1操作时再次观察
a += 1
print(id(a))
print(id(b))
# 结论:各个引用之间相互独立
```

![](https://gitee.com/lzd-1230/img-host/raw/master/image/20211218150416.png)

+ 可变对象(mutable object)：列表，字典…

```python
L1 = [1,2,3]
L2 = L1
# 猜猜结果? -> 一样
print(id(L1))
print(id(L2))

# 猜猜结果?
print(id(L1[0]))
print(id(L2[0]))
print(id(1))

# 改变一下
L1[0] = 99
# 猜猜结果?
print(id(L1))
print(id(L2))
# 猜猜结果?
print(L1)
print(L2)
```

![](https://gitee.com/lzd-1230/img-host/raw/master/image/20211218151156.png)

# 参考资料

+ [Python教程 - 廖雪峰的官方网站 (liaoxuefeng.com)](https://www.liaoxuefeng.com/wiki/1016959663602400)