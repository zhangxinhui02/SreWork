# C进阶作业

(\*\^▽^*)

#### Level0:

利用数组，实现以下两个函数：

```c++
int vectorAdd(const double *, const double *, double *, int dimension);
int vectorMul(const double *, const double *, double *, int dimension);
double vectorPeojection(const double * ,const double *);
```

他们分别是向量加、向量点积、向量距离、向量投影。

#### Level1:

利用不同类型指针的特性，实现下面这个函数:

```c
void bitSwap(unsigned int x);
//它的作用是交换一个int数据的高位和低位。
//在注释解释input和output这么交换的原因。
-->input  :0x1234ABCD
-->output :0xCDAB3412
```

#### Level2:

以递归和非递归的两种形式实现下面这个函数:

```c
returnValue Dec2Bin(unsigned int n);
//输出需要是:
-->input  : 6
-->output : 110
```

#### Level2.5:

分别实现顺序栈和链式栈，并写出测试案例，至少要完成的操作有:

```c++
bool isEmpty(args);
bool push(args);
ElementType pop(args);
ElementType getTop(args);
```

#### Level4:

实现十进制数字到任意进制的转换函数:

```c++
void baseConverter(int dec,int base);
//其中base为转换的基数
-->input   :17,16
-->output  :11
```

#### Level5(选):

自己写代码并从汇编层面分析C语言，最少要分析：

- 不同类型数组的行为
- 指针
- 结构体
- 栈
- 函数的调用
- ...

## 提交格式

将作业文件打包为 “作业_学号\_姓名\_最高Level”提交到 **qingshui@redrock.team**。

<font color = red>**注意**</font>：至少做到 Level1 再提交，提交 Lv5 时注意可读性，至少让人能有兴趣看得下去再提交。除**Lv5**期限为4个星期，其余截止日期为 2021-11-22:00。

