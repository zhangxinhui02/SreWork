---
title: Linux基础
date: 2021-08-07 15:14:14
tags: mess



---

# <font color=#86473F>linux基础</font>

<font color=#BF6766>这节课的目的：</font>

- 让没有任何编程基础的萌新了解linux系统
- 大致了解linux最基本文件操作指令以及软件的下载安装

<font color=#BF6766>并没有很多的指令的学习，主要是想为萌新们加深对于linux系统的理解。以及讲一些个人的比较奇怪的体会，所以可能内容会比较少。另一方面这样也能空出一些时间拿来实操，翻车了也不怕。</font>

## <font color=#B19693>0）普通的介绍</font>

SRE第一节课，由我来给大家讲linux基础。讲课水平很菜，linux水平也就凑合做个ctf题。

希望大佬不要炸鱼。

## <font color=#B19693>1）linux是什么？</font>

Linux是一类自由和开源的操作系统。

通常情况下，我们接触到的linux都是被打包好的各种linux发行版，包括[Debian](https://zh.wikipedia.org/wiki/Debian)（<font color=#A96360>及其派生版本[Ubuntu](https://zh.wikipedia.org/wiki/Ubuntu)、Kali等</font>）、[Fedora](https://zh.wikipedia.org/wiki/Fedora)（<font color=#A96360>及其相关版本[CentOS](https://zh.wikipedia.org/wiki/CentOS)和[openSUSE](https://zh.wikipedia.org/wiki/OpenSUSE)等。)和[openSUSE](https://zh.wikipedia.org/wiki/OpenSUSE)等。</font>

也就是类似ubuntu，centos等操作系统，都属于linux。不同的发行版的命令格式以及依赖库都不太一样，在学习初期选择一种发行版使用就行，没有必要反复横跳。

建议没有明确方向的同学统一装ubuntu20.04LTS。据说每年都有大量萌新装各种奇怪的发行版，用完都哭了。所以建议统一一下。

## <font color=#B19693>2）安装一个linux系统</font>

这个在预习作业中大部分同学已经完成了，但是还是有一部分同学没有动静或者被卡住了。这个步骤我们就不再提了，如果还没有装的话课后一定要安装，有什么问题可以在课后问。。

我就不再重新装了，但是有几点需要注意。

之前提到，没有明确方向的同学建议装Ubuntu20.04LTS。

原因很简单，好用，而且大家都在用，有问题能快速解决。

虽然但是，我不敢说，但是Mac OS X 10.15的同学如果装ubuntu20.04LTS，我不敢说有多大概率，可能只有百分之一，会遇到日常崩系统（日常。指每天），我也不知道为什么，反正我遇到了，怎么想也想不通，所以我放弃了20.04（）。

vm我没用过没有办法给出什么建设性的意见，但是如果是pd用户我只能说，一定要经常备份（拍快照）。等你系统崩了没办法恢复需要忍痛重装系统的时候你就知道有多苦了。

还是Mac OS X 10.15 + ubuntu 20.04 LTS的环境，我当初重装了系统附加环境两次我才发现有快照这个东西，后面有一次我恢复快照都没办法解决系统崩盘的问题，然后心一狠把整个系统删除了，安装包也重新在官网下载了一个，果然稳定了，花了一上午把环境重新配好，开心地用了一个月，结果又又又开始崩。那个时候我就是，每天用完准备关闭系统让它休眠之前一定要拍快照，以至于现在环境很正常但是我还是养成了战战兢兢每隔几天备份系统的习惯

但是我现在用的18.04挺稳定的，几个月都没有崩的痕迹。所以我诚挚地希望电脑是低配mba然后用pd的同学谨慎考虑20.04 lts。

 Ps：那个靠每天恢复快照苟活的20.04在我换电脑移植文件后彻底与我说再见了，不是我要抛弃它，是它自己怎么也恢复不了，错的不是big sur，也不是惨兮兮的ubuntu20.04 lts，是~~这个世界~~。

## <font color=#B19693>3）为什么要使用linux？</font>

### <font color=#AB3B3A>1）免费</font>

windoe10家庭版在中国官网售价**1088rmb**，Mac OS X正版则只随电脑附赠，最便宜的是mac mini，**5299**起。

**然而作为三大操作系统之一的linux，完全免费**（<font color=#A96360>[关于开源协议以及开源精神](http://haacked.com/archive/2012/02/22/spirit-of-open-source.aspx/)</font>）

### <font color=#AB3B3A>2）开源</font>

开源意味着用户可以对linux 内核进行查看甚至修改，例如对于linux服务器来说，用户甚至可以自定义系统程序，为管理提供了便利。

另一方面，内核开源使得我们有机会去分析内核代码，使得源码剖析成为可能。（在ctf pwn方向，完全开源的内核代码为glibc pwn以及kernel pwn学习提供了极大的便利）

### <font color=#AB3B3A>3）软件生态丰富</font>

对于很多我们熟悉的桌面版软件（QQ，WX等），linux一众发行版的适配可以说是非常糟糕。比如你可能需要费非常大的力气才能在liunx上跑一个bug很多，ui很奇怪的qq。

但是对于SRE的日常学习来说，linux是必不可少的。我们使用的非常多的程序基本都是原生支持linux而不一定支持其他操作系统，也就意味着可能在Linux上能顺利运行，在win或者macosx上就会出现很多奇怪的bug，或者根本就不支持。并且，承接上文说到的开源，开源且自由的环境让服务器状态几乎变得透明，我们可以很方便地进行服务器的管理。

### <font color=#AB3B3A>4）ctf学习</font>

接上一点，Linux基本上是学习ctf竞赛道路中必备的工具，正确熟练地使用linux能使你学习效率大大提高。

传说“kali学得好，牢饭少不了”，作为linux发行版其一的kali拥有超过600个预装的渗透测试程序，为不管是打ctf还是实战都提供了极大的便利。美剧Mr.robot中，男主就是靠一台kali打四方，其标志性的龙图标在剧中非常惹人注目。



#### <font color=#AB3B3A>5）通过命令行控制</font>

此外，如果你拿到一个linux系统，无论任何发行版，你会发现linux与你平时习惯的操作系统有一个显著的区别----特别依赖命令行。

通过终端输入的命令行，基本能将整个linux系统拿捏在手里。比如linux的文件管理，对于文件的增删改查，都可以通过命令的方式完成。但是由于比如ubuntu桌面版本身带有图形化界面，我们也可以通过操作图形化界面的方式去对文件进行管理。但是如果遇到根目录下的文件的增删改查，这时候命令行反而会比图形化操作更加方便。综上，命令行是linux基础入门学习的重中之重。



## <font color=#B19693>4）linux基础知识及常见命令</font>

**事实上这个东西就和记英文单词一样，没有必要记。用得多了自然就熟了，特别生僻的直接查就好了。所以我觉得学习初期记一些简单的命令就行。**



#### <font color=#AB3B3A>在基本命令之前</font>

在记住一些基本的命令之前，有一些基本到没有人愿意给你说的操作是你必须要学会的。

比如

1:

```c
./filename  #相当于双击打开文件
```

./就可以类比为双击打开。无论什么文件，理论上都可以双击。但一般来说还是打开可执行文件，或者说编译好的程序比较有效果。不然可能就是命令没找到或者一行其他报错。

2:

通过操作上下可以在命令行中显示你曾经输入过的指令。这个自己感受一下。比如输一行指令，因为输错了最后一个字母然后报错，这个时候你又手贱把终端清空了，就可以按上，呼出你上一条执行的指令，然后通过左右键把光标移到要修改的地方然后修改。

3:

终端可以多开。记得终端使用右键看看。另外如果觉得终端的配色让你生不如死，可以在终端的界面右击选择偏好设置。ps：ubuntu的主题也是可以修改的，20.04挺好看。但是18。04就属实辣眼睛。修改也很简单。查一查啥都有。

4：

大部分情况下，按下tab键补全是可行的。）

5:

在很多虚拟机里复制粘贴的快捷键不是ctrl +cv而是 shift+ctrl+cv。



#### <font color=#AB3B3A>文件管理</font>

有一个众所周知的点就是，linux基本命令的命名实际上基本是英文缩写。

之前在知乎看到一个很有趣的linux命令全称大全，分享一下。

所以可以靠这个来记忆一下。比如ls就是list，cp就是copy，mkdir 就是 make directory...

```bash

ls  #列举出当前工作目录的内容（文件或文件夹）
  
cd  #切换文件路径
    
mkdir  #新建文件夹
  
pwd #显示当前工作目录。
#关于这个指令的用处，实际上好像没啥用，但是如果你要从这个文件夹中复制什么东西到根目录，就会比较方便。具体的演示留给cp这条指令
  
rm  #删除指定文件
#删除文件夹是rm -r 《文件夹》
```

```bash
cp #复制。
#基本的使用方法就是cp <路径1> <路径2>
#这里就可以提现pwd这个指令的用处。
#比如要把home目录下一个又臭又长的路径的东西移到根目录下另外一个又臭又长的路径下，如果耿直地一点一点输是很令人窒息的。
#这个时候我们可以使用先进的图形化文件管理系统，将它与终端有机结合。
```

```bash
mv  #移动文件或修改文件名，根据第二参数类型（如目录，则移动文件；如为文件则重命令该文件）。
mv 111.txt 233.txt #重命名111.txt为 233.txt
mv a.txt /test #将文件 a.txt移动到根的 test 目录中
```

```bash
cat
#一次显示整个文件
#eg1:cat flag
```

```bash
#mess
chmod #更改文件执行权限
#基本用法举例
chmod 700 <file>
修改文件权限为文件所有者可读写执行。
#其他用法可以自己学。专门讲只是因为当我还是个菜鸡的时候被这个东西坑过，当时做题，执行脚本一直报错，我以为是脚本的问题，结果是程序没有可执行权限。。。

#使用ls -l命令可以查看当前桌面文件的权限情况。


```

![image-20210811091910279](https://rin777-1306176007.cos.ap-nanjing.myqcloud.com/image-20210811091910279.png)

示例如图/我先用`ls-l`查看文件权限，发现是rw也就是只有可读可写权限胆识没有可执行权限，所以通过chmod 700将文件改为可执行后再次查看权限。发现文件可执行。



```bash
tar #压缩或解压文件

tar -xzvf <file>
```



以上的指令只要记住最基本的ls，cd就好了（甚至可以不记住），大家只需要有一个比较模糊的印象就好。遇到问题直接搜就好。

而且感觉大家大多数还是在用桌面版，桌面版的话ubuntu直接为文件管理提供了图形化界面，比较友好直观。像win那样操作就好了，但是如果是linux server就没办法啦。（好怪，不会真的有人拿云服学ctf吧）

#### <font color=#AB3B3A>安装/更新/包管理</font>

在了解相关指令之前，必须明确一个概念就是，抛开ubuntu贫瘠的应用市场不谈。ubuntu等一众发行版下载/安装程序基本都是通过shell来交互。

也就是ubuntu下载某个程序，一般来说不是到某个应用市场下载安装包再一键安装（当然也行），而是通过<font color=#86473F>储存库 -> 包管理器 ->用户</font>的路径对软件包进行分发。

比如我们要下载vim这个代码编辑器，只需要一条简单的指令就能实现自动下载和安装

```bash
sudo apt install vim
```



这里`sudo`表示以管理员身份指令后面的指令，如果你执行某条指令时报错了，不要慌张。认真看后面的报错的信息，（ps：如果使用的是ubuntu20.04，那么你可以调成中文，非常萌新友好）

`apt`则是ubuntu中的一个包管理器，可以自动下载，配置，安装二进制或者源代码格式的软件包。

类似apt的包管理还有很多，ubuntu上就有特别常用的pip，npm之类，

`install`则是具体的指令，类似的还有`remove`，`update`，`upgrade`等。

我们还忽略了一个叫储存库的东西，它比较大众的名字是“软件源”，负责储存各种软件下载的路径。

![2](https://img-blog.csdnimg.cn/5af2332d07e440ff91ae335c9ed28cb9.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzUxMTg3NTU4,size_16,color_FFFFFF,t_70)

比如说这里。

Do you want to continue？

当我们选择yes，apt就开始自动从` http://cn.archive.ubuntu.com/ubuntu bionic-updates/main amd64 vim-runtime all `这个网址下载vim的安装包，这个网址就可以理解为是一个软件源。

就像在手机上下载软件，有app store。软件源就类似app store，然后你需要通过包管理器将软件源上的东西下载并安装到本地。

当然软件源是可以更换的，由于国内不能科学上网，如果用默认的源下载速度一般会很慢。推荐更换清华或者阿里源。

具体的换源教程建议百度。

然后列举一些最基本的指令，具体的指令实际上不用记住，只要知道有这么个东西，它大致是干什么的就行。以后遇到了再学习也不会迟。

```bash
#apt
sudo apt update  #查看可新的软件包
sudo apt upgrate  #更新软件包
sudo apt remove  #删除某个通过apt下载安装的软件包
```



还要注意的就是以后大家会遇到要安装pip的情况。

pip是一个专门处理基于python语言程序的包管理器。但是一般来说ubuntu18及以上都是默认支持python3的，所以相对应的pip也应该安装pip3。具体的安装方法可自寻文章。

#### <font color=#AB3B3A>其他</font>

奇奇怪怪（）的重要命令。不能说很重要，只能说特别重要。

```bash
clear #清屏

#gcc最简单的无脑编译指令 
gcc -o main main.c #main.c是源码文件的名字，main是编译出来可执行文件的名字，这个名字可以随便取。
#也可以写成这样
gcc main.c -o main
#这样以默认参数编译出来的程序是比较安全的（）
#此外gcc还能生成编译各个阶段的文件，以及编译多个文件，还能通过控制参数改变程序的保护方式等等各种功能，具体参数可以自己查一查。
#https://www.runoob.com/w3cnote/gcc-parameter-detail.html里的命令比较全面。

```

```bash
#vim的基本操作
在命令行中输入vim就自动跳转到了vim的界面。
和其他编辑器一样，vim分为输入模式和命令行模式。
首先按i，进入输入模式，输你想输的。
输完以后，按一下esc，进入命令行模式。
vim的一切文件的保存以及退出vim都是靠这个命令行。
比如：q是退出
：wq是保存后退出
记住每条指令前要加冒号。
如果保存不了（权限不够），可以在后面跟一个！
比如
：wq！
：w！
：q！
```



## <font color=#B19693>5）linux学习心得</font>

在熟练掌握最基础命令+善用搜素引擎之后，你已经能初步操作linux做你想做的事情了。

但是上文中我也一直说在授课中我不想讲太多纯粹的指令。这些东西应该在课后自己折腾。就算课上讲了，有一说一一会儿就忘了。

但是就“如何学习（或者记住）命令”这个问题，我认为还是有一定的窍门的，并不是纯粹的熟能生巧。

比如一般通过萌新大概会对代码有天然的恐惧，给他一篇再清楚再详细的文章，也可能报错连连。犯诸如打错字，复制别人的用户名，行号等等。由于这种对于自己看不懂的东西天生的抵触，他可能在很长一段时间里都只是纯粹地对教程上的指令进行复制粘贴，而不去探究，哪怕只是搜一下，这个命令为什么是这样的，这个pip和pip3有什么区别等等。

所以我希望大家在学习某一条指令的时候，尽量先把每一条指令拆分开来，分别查对应的功能或者意思。

就比如我在前面写到的

```bash
sudo apt install vim
```

在新人眼里这就是一串英文字母，但是沉下心来你会发现它由四个部分组成，具体的前文已经分析过了。

然后你会逐渐发现这些指令都有共通的地方，学会了一条“语法”，就相当于学会了成百上千条指令。

同时明白了指令的原理也能让你随机应变，找到你自己环境的差异然后有针对性的对指令进行修改。

**ps：查资料的时候可以选一些看起来比较正规专业的网站来查询。如果是命令行或者代码语法首选类似官网文档，W3school或者菜鸟教程这种看起来就很正经的网站，可能相对于直接找别人写的博客来说比较慢，但是绝对准确。如果是做题等遇到的报错的话首先看有没有独立个人博客（不是csdn或者那种不知名广告网站，而是自己搭服务器或者xxpage建的个人网站），再看有无csdn博客园这种，当然如果有靠谱的参考书也行。具体原因的话，csdn这种网站门槛太低，什么牛马都有，鱼龙混杂，好坏参半，新手比较难分辨。除了各种无授权搬运、广告文、恶心的资源分享系统、占据互动半壁江山的机器人，还有部分文章内容会出现技术性错误，误导新人。而且ui不能自定义///////**。

但出错也难免，因为门槛低，所以本身就有各种新人的试错笔记，既然是新人犯错难免。事实上就算是个人博客也会出现错误，放宽心就好。参考文章出错虽然是一件很难受的事情，但是在我眼中确是最能容忍的555。

所以希望大家不要因为害怕出错就不写笔记哇。



说到查资料，那还是不得不提另外一个，提问的艺术。

这个问题其实挺有趣，可以看看知乎上面一个问题“为什么一些程序员很傲慢”的回答。



你喋喋不休问别人傻逼问题的时候你肯定不知道他十分恼火但是还要装出一副和颜悦色的表情回答你的样子有多动人（）

[为什么一些程序员很傲慢？ - 码客的回答 - 知乎]( https://www.zhihu.com/question/435258463/answer/1969561682)

基础部分就到此结束啦！

linux系统更加深奥的部分，将会由别的学姐在之后的课程中带领大家深入。希望下面简单的课后作业能使大家充满决心！

## <font color=#B19693>7）课后作业（实际上就是预习作业的pro edition）</font>

在完成了linux环境的配置的情况下，不用按顺序做，喜欢哪个做哪个。但是如果还未配置好linux环境，请参照预习课作业完成。

有问题可以私聊群管理。

#### <font color=#AB3B3A>Level0 </font>

利用（linux自带的）gcc编译器通过指令编译一个`hello world` c程序。

（ps：程序的源码不会写的话直接网上复制，不过hello world这种程度的代码建议花十分钟学一学）

做完将运行的程序的截图发至fuurinko@gmail.com。

示例如下。

![image-20210810105759326](https://rin777-1306176007.cos.ap-nanjing.myqcloud.com/image-20210810105759326.png)

#### <font color=#AB3B3A>Level1.1 </font>

熟悉typora的基本使用方式。

#### <font color=#AB3B3A>Level1.2 </font>

Glibc 是linux上一个至关重要的c运行库，随着版本的更新，glibc也会不断推出功能更完善，防护更周密的新版本。但是有时我们需要使用一些旧版本的glibc来完成特定的任务。此时我们可以选择手动编译某个版本的glibc，并将linux glibc切换到你编译的版本。

作业：

手动编译一个glibc2.23以上版本的libc（更低的版本不建议，因为源码中也许会出现许多你无法轻易解决的bug），并且将编译的过程使用typora用优雅的md格式记录成笔记。完成后提交md格式笔记到fuurinko@gmail.com

源码下载链接：https://ftp.gnu.org/gnu/glibc/

参考教程：https://marvinsblog.net/post/2019-02-12-compile-glibc/、

#### <font color=#AB3B3A>Level2.1</font>

购买一台vps，利用它以及图床软件为你的typora配置一个好用的图床。

#### <font color=#AB3B3A>Level2.1</font>

用vps+wordpress或hexo等博客软件搭建一个个人博客。

并且将过程写成笔记，并且将这篇笔记以及上一篇一起部署到博客上。

## <font color=#B19693>8）参考</font>

[Linux apt 命令](https://www.runoob.com/linux/linux-comm-apt.html)
