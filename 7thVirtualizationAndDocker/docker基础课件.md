# docker基础

## 安装

+ 软件的安装可以借助官方文档 + 博客(官方的下载速度可能较满,需要参考自己的Linux版本查看有没有换源):

  官方:https://docs.docker.com/get-docker/
  
+ 运行命令启动 helloword 容器或者使用`docker version`查看是否安装成功:

  `docker run hello-world`

  `docker version`

## 虚拟化与容器

+ 系统虚拟化的概念

  系统虚拟化是指在一台物理计算机系统上虚拟出一台或多台虚拟计算机系统，最终每个操作系统同时运行，相互独立。

+ 系统虚拟化技术的简单分类

  + 传统虚拟化

    比如大家安装过的 Vmware Workstation等虚拟机软件所实现的功能。

  + 容器化技术

    以 docker 为代表的容器引擎所实现的功能。

+ 传统虚拟化技术

  ![img](https://img2.baidu.com/it/u=1942673583,1276127957&fm=26&fmt=auto)


我们以x86的CPU为例,其运行有严格的级别划分,我们应用程序日常是处于较低的级别中。当其需要访问一些硬件资源,则需要执行系统调用，切换到更高的级别，之后就可以使用一些特权指令比如(控制中断，访问设备等等)，这些指令由内核负责完成资源的访问，拿到资源后再切换回用户的代码。

那如果我们需要虚拟化出很多个 Guest OS 就遇到了难题了，它们如何与宿主操作系统怎么去分配 Ring0 呢？

我们下面来看一下**纯软件虚拟化**的架构。

![img](https://img0.baidu.com/it/u=2744699496,986817359&fm=26&fmt=auto)

在上图中，Hypervisor 运行在 Ring0 中，当 Guest OS 中的应用程序发出系统调用的指令后会产生异常，能够被 Hypervisor 层捕获到，然后跟据不同地指令选择是交予硬件去处理，还是使用仿真出来的 CPU 给予相应。重点在于，此时的 Guest OS 是不知道。

<img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fwww.pianshen.com%2Fimages%2F907%2F1f1c1386f451f7ddda345a1e167b119b.png&refer=http%3A%2F%2Fwww.pianshen.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1641139036&t=ef1d0c1e665b259ef5869c64d0288316" alt="img" style="zoom:50%;" />

  + QEMU：QEMU是一套开源的硬件模拟器，它能让 Guest OS 认为自己和硬件直接打交道。它与KVM相互配合,完成硬件的虚拟。

  + KVM：KVM是 `linux` 内核模块,用于初始化CPU以提供的虚拟化架构,提供了**CPU**和**内存**等高性能设备的虚拟化控制技术。KVM 属于需要处理器硬件支持虚拟化，其简化了部分VMM中调用经过的路径，性能有所提升。其可以让 Linux 操作系统转变为上面所说的虚拟监控器，从而可以在Linux中虚拟出多个子系统来。

  + Hypervisors: 虚拟机监控程序有时候也叫VMM，它可以访问服务器上包括磁盘和内存在内的所有物理设备,从而将一个系统划分为不同的、单独安全环境。Hypervisors 不但协调着这些**硬件资源**的访问，让我们可以比较无感地切换。

    ![How virtualization works](https://www.redhat.com/cms/managed-files/how-virtualization-works-400x217.png)

+ 容器化技术

  容器化技术利用 Linux 命名空间的技术,将容器彼此之间隔离开,作为 HOST 操作系统的一个进程。

  > 虚拟机和容器最大的区别是容器更快并且更轻量级——与虚拟机运行在完整的操作系统之上相比，容器会共享其所在主机的**操作系统/内核**。

  <img src="https://gitee.com/lzd-1230/img-host/raw/master/image/20210320222912.png" style="zoom:150%;" />

  虚拟机一般会占用100~200MB的内存,因此对计算机的网络,磁盘,CPU的性能都会有一定的损耗。但是 docker 基于 namespace 的内核技术可以做到很小的性能损耗与极快的开启速度。

## 容器的引出

看完了虚拟机和容器技术的介绍，下面我们正式进入 docker 的学习。

> Basically there are a few new Linux kernel features (“**namespaces**” and “**cgroups**”) that let you isolate processes from each other. When you use those features, you call it “containers”

+ 容器: 本质上就是运行在自己操作系统上的一个进程，只不过是利用了内核特性进行隔离过的一个进程。

+ 案例:

  > 为什么程序在我这可以运行,到你那里就不行了? 

  造成这种结果的原因特别多,而且一般还跟的代码没关系->两个程序运行的环境不同。
  
  而 docker 就可以解决这个问题。

```
我们将目光转到Android系统上来,其是一个开源的手机操作系统,也是一个生态圈,安卓手机的APP以apk的形式打包,发布。
当我们需要某个APP的时候,我们就会去应用市场上下载。

当我们从这个角度来看的时候Docker就和Android十分类似

Docker是一个开源的容器引擎,也有着自己的生态圈,它的应用以镜像(image)的形式打包发布,我们也可以在官方的"镜像市场"中下载自己所需要的镜像                        
```

+ 讲到这里,我们可不可以试着在这个应用商店中下载一个 `wordpress` 试试?

  ```shell
  # 执行以下命令
  docker run --name db --env MYSQL_ROOT_PASSWORD=123456 -d mariadb
  docker run --name wp --link db:mysql -p 8081:80 -d wordpress
  ```
  
+ namespace：

<img src="https://img0.baidu.com/it/u=1577231600,1762630384&fm=26&fmt=auto" alt="img" style="zoom: 150%;" />

我们想一下我们的班级，每一个班级都可以有自己的排序。

> 我们来开辟一个全新的进程环境，让我们的进程与主机上的其它进程隔离开来。

```shell
# 我们以进程的命名空间作为举例
sudo unshare --fork --pid --mount-proc bash
ps -aux # 来查看该进程的pid命名空间
# 输出
USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root          1  1.3  0.1 116316  2884 pts/0    S    14:32   0:00 bash
root         29  0.0  0.0 155448  1836 pts/0    R+   14:32   0:00 ps aux

我们可以看到该进程所在pid命名空间下的进程明显与我们平常所在的进程空间隔离了。
在不同的PID中，进程ID是独立的。最顶层的名称空间是`root` ,其下面可以开启若干个子名称空间。
```

![](https://gitee.com/lzd-1230/img-host/raw/master/image/20211129222041.png)

+ cgroup: 用于资源使用的限制

  ```shell
  # 我们创建一个cgroup
  mkdir /sys/fs/cgroup/cpu/test 
  # 在/sys/fs/cgroup/cpu/test下我们可以看见很多文件
  比如:cpu.cfs_period_us 用来控制CPU的占有时间, tasks内规定所限制的进程的PID号
  ```

## docker基本概念

docker 中的基本概念主要有三个：**镜像，容器，仓库**。

+ 镜像:制造容器的模板

<img src="https://gitee.com/lzd-1230/img-host/raw/master/image/20210810213405.png" style="zoom:67%;" />

镜像由多个层组成，每层叠加之后，从外部看来就如一个独立的对象，内部包含容器应用运行所必须的文件和依赖等。

镜像中**不包含内核**——容器都是共享所在 Docker 主机的内核。所以有时会说容器仅包含必要的操作系统（通常只有操作系统文件和文件系统对象）。

+ 容器

在我们本机的OS层之上,需要安装容器引擎（如 Docker）,容器引擎可以获取系统资源，接着将资源分割为安全的互相隔离的资源结构。

每个容器看起来就像一个真实的操作系统，在其内部可以运行我们自己的应用。

+ docker 的使用逻辑

![img](https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=3715698682,4278914997&fm=26&gp=0.jpg)

+ docker 的软件架构

<img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg-blog.csdnimg.cn%2F20191101151405994.png%3Fx-oss-process%3Dimage%2Fwatermark%2Ctype_ZmFuZ3poZW5naGVpdGk%2Cshadow_10%2Ctext_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xqdzI3NzUxODM1Nw%3D%3D%2Csize_16%2Ccolor_FFFFFF%2Ct_70&refer=http%3A%2F%2Fimg-blog.csdnimg.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1641046773&t=f32f796ea4f89823d56a1ec525165a58" alt="img" style="zoom:67%;" />

```shell
# 客户端程序位于/usr/bin/docker
Client: Docker Engine - Community
 Version:           20.10.8
 API version:       1.41
 ...

# 服务端:提供了一个sock文件以支持本地进程通信
# /var/run/docker.sock
Server: Docker Engine - Community
 Engine:
  Version:          20.10.8
  API version:      1.41 (minimum version 1.12)
...
```

但同时docker的客户端/服务端之间采取Rest API作为通信协议,因此我们也可以配置使得`docker daemon`进程来监听远程的客户端请求。

使用远程连接时需要在客户端配置环境变量 `DOCKER_HOST` ,以及在服务端配置docker的守护进程即可实现。

## 容器

### 命令行常用命令

+ `docker --help`: 查看 docker 的命令帮助

+ `docker imges`: 查看本机中已有的镜像。

+ `docker run [选项] <镜像名:版本号> [命令]`: 运行容器

  寻找镜像的过程:

  1. 判断本机是否有这个镜像
  2. 如果有就直接运行,如果没有就去 DockerHub 上去寻找
  3. 如果在 Dockerhub 上也找不到就报错,如果找得到就下载下来

  ![](https://gitee.com/lzd-1230/img-host/raw/master/image/20210813164742.png)

  注: 通常会有一些选项参数可以设置,这里列举一些

  + `--name <容器名称>`:用来指定容器的名称
  + `-it`: 以交互模式连接到容器
  + `-d `: 后台运行容器
  + `--rm`:容器挂掉后自动删除
  + `-p <主机端口>:<容器端口>`: 开放容器端口
  + `-v`:指定挂载点
  + `--link <name or id>:alias`: 与另一个主机互访并且设置别名。

  这里以启动一个 centos 容器为例子

  `docker run -it centos此时如果你现在能上网的话,就会在dockerhub上面拉取`centos`镜像的`latest`版本

+ 查看**运行中**的容器

  + `docker ps `

    + 查看全部容器(包括已经死掉了的): `docker ps -a`
    + 常用操作:删除掉所有正在运行的容器

      `docker rm -f $(docker ps -aq)`

+ 离开容器的终端,但是不退出，区别于直接 exit 退出容器
  
  ​	快捷键 `Crtl + pq `
  
+ 查看容器的详细信息

  `docker inspect <容器名>`

+ 查看容器的日志

  `docker logs <容器名>`

+ **进入正在运行的容器当中**

  `docker exec -it <容器名> /bin/bash`

### 简单的演练

+ 起一个  `nginx` 的容器

  + 暴露容器的 80 端口->主机上的 8080 端口
  + 将容器的 `/usr/share/nginx/html` 目录挂载到当前文件夹下
  + 在文件夹下创建一个文件,然后进入容器中查看该文件是否存在
  + 访问 8080 端口

  ```shell
  docker run --name nginx -p 10000:80 -v <本地目录>:<容器中目录> -d --rm nginx:latest
  
  # If you intended to pass a host directory, use absolute path.
  ```

### 将容器打包成镜像

> 在我们还不清楚具体应该如何配置的时候,我们可以先起一个容器,进到里面去试着配置以下,觉得达到效果了之后就打包成镜像

`docker commit <容器名> <镜像名:版本号>`

打包好的镜像在本地, 可以继续向远端推送至 `dockerhub`

+ 实操: 创建一个容器在里面安装 `ping` 命令

  ```shell
  # 先换源
  sed -i "s/archive.ubuntu.com/mirrors.aliyun.com/g" /etc/apt/sources.list
  # 再更新源
  apt update && apt install iputils-ping
  # 再试试ping能不能用了
  ping --help
  # 最后退出容器去打包
  docker commit 
  ```

## 镜像

+ 镜像的分层设计

这样的分层设计结构可以大大简化镜像在本地的存储空间。

比如我们有镜像A和镜像B都依赖于下图中的第一层和第二层，那么它们可以公用这两层的数据而不用再额外地复制一份出来。

我们可以通过 `docker history <镜像名>` 来查看镜像的分层以及各层所进行的操作。

![Docker镜像](http://c.biancheng.net/uploads/allimg/190416/4-1Z416163955K0.gif)

对我们的启示：当我们制作自己的镜像的时候，尽量考虑可以制作出可复用的底层镜像，可以更多地进行复用，同时为了减少镜像的层数如使用`&&`将多个 `RUN ` 指令合成一个。

### 储存卷

+ Docker 中的容器一旦删除，容器本身的根文件系统就会被删除，容器内部的数据将会被删除。有时候我们不希望文件随着容器的删除而丢失。

> 储存卷提供了将容器内特定路径的文件映射回主机的功能。
>
> 因此如果我们将数据挂载到本地的某个目录，当容器启动的时候都挂载上这个目录，那数据就会一直在，不管容器重启多少次。

+ 创建**命名存储卷**`docker volume create app-db`

  命名挂载点**只需要在容器内指定容器的挂载点**是什么，而被绑定宿主机下的那个目录，是**由容器引擎daemon自行创建一个空的目录**，或者使用一个已经存在的目录，与存储卷建立存储关系，这种方式极大解脱用户在使用卷时的耦合关系，缺陷是用户无法指定那些使用目录，临时存储比较适合。

+ 使用`docker volume inspect <数据卷名>`来查看具体的数据卷信息

  ![](https://gitee.com/lzd-1230/img-host/raw/master/image/20210813202811.png)

+ 运行容器的时候将这个储存卷挂载到相应目录即可

    `docker run -dp 3000:3000 -v todo-db:/etc/todos <镜像名>`

    注:构建的时候如果 -v 后面的存储卷没有创建,`docker` 会自动帮你创建命名挂载点。

+ 删除该容器并以该命令重启

      最终发现,上次存储的记录还在,这是因为容器启动时挂在了该文件,因此应用程序得以读取到文件内容。

    ![](https://gitee.com/lzd-1230/img-host/raw/master/image/20210813203653.png)

+ docker的另一种储存卷:**绑定挂载卷**

  绑定挂在卷可以在宿主机上自行指定一个目录,并且在容器内指定一个目录,使得两者之间建立一一映射关系。
  
  `docker run -v <宿主机路径>:<容器内的路径>` 注：路径必须为绝对路径。
  
  这种情况通常用于需要向文件内添加额外的文件的情况,而不仅仅是被动地接受容器内的数据。
  
  比如我们可以将源代码以存储卷的形式与容器绑定, 这样即可完成
  
+ 二者的区别与对比

  |                | **Named Volumes**         | **Bind Mounts**           |
  | -------------- | ------------------------- | ------------------------- |
  | 在主机中的位置 | 自动选定                  | 由我们手动指定            |
  | 使用方法       | <存储卷名字>:<容器内路径> | <主机内路径>:<容器内路径> |

### 容器间通信

+ 通常我们会为一个APP配合上一个 database，比如一个 wordpress 配合上一个数据库。

  因此我们需要打造两个容器的情况如下:

  ![](https://gitee.com/lzd-1230/img-host/raw/master/image/20210813214552.png)
  
  ​    一般我们会使用创建 network 或者 link 的方法，这样可以让容器之间使用容器名/别名进行通信。

## 实践

完整的应用容器化过程可以主要分为以下几个步骤。

- 编写应用代码。
- 创建一个 Dockerfile，其中包括当前应用的描述、依赖以及该如何运行这个应用等镜像构建的过程描述。
- 对该 Dockerfile 执行 docker build 命令完成镜像的构建。
- 等待 Docker 将应用程序构建到 Docker 镜像中。一旦应用容器化完成（即应用被打包为一个 Docker 镜像），就能以镜像的形式交付并以容器的方式运行了。
- 最后可以将镜像推送到远程仓库。

### 准备步骤

+ 首先将代码文件上传至服务器中
+ 然后编写 `Dockerfile` 来构建镜像

### 初步构建

+ 编写 `Dockerfile`

```dockerfile
FROM node:12-alpine
# 换源
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories
# 安装工具
RUN apk add --no-cache g++ make
# 切换工作目录
WORKDIR /app
# 将项目文件复制到刚才的工作目录
COPY . .
# 安装项目依赖
RUN yarn install --production
# 执行容器进程 格式: CMD ["命令","param1"," "]
CMD ["node", "src/index.js"] # 可以替换成 CMD 命令 param1 param2
```

+ 运行命令构建镜像

`docker build -t <镜像名> .`

+ 启动容器进行测试

`docker run -dp 3000:3000 --name test <镜像名>`

### 一种存储卷

首先回忆一下之前讲的内容,每一个容器使用镜像中的各个层来组成他的文件系统，作为一个独立的小系统存在。因此如果不进行任何操作，它是相对封闭的。而存储卷给我们提供了打通容器内目录与主机目录的能力。

本次实践中的数据库文件位于 `/etc/todos` 目录下,因此我们需要在运行容器的时候将之前备份的数据提供给它。

+ 首先创建一个 docker 管理类型的存储卷

  说白了就是一个只需要知道存储卷名字,而存储卷的位置由docker帮你创建的一种存储卷类型。docker 还有一种叫绑定存储卷。

+ 在运行容器的时候显式指定一下该卷。`docker run -dp 3000:3000 -v todo-db:/etc/todos <镜像名>`

```shell
"Mounts": [
    {
        "Type": "volume",
        "Name": "todo-db",
        "Source": "/var/lib/docker/volumes/todo-db/_data",
        "Destination": "/etc/todos",
        "Driver": "local",
        "Mode": "z",
        "RW": true,
        "Propagation": ""
    }
]
```

### 另一种存储卷

+ `docker run -dp 3000:3000 -w /app -v "$(pwd):/app" node:12-alpine sh -c "yarn install && yarn run dev" `

这行代码主要是为了测试一下我们将当前目录的内容,挂入容器中,然后修改主机中的代码,然后测试一下容器内应用程序的变动。

### 多容器的 app

现在我们想要给刚刚的 app 弄一个 mysql 的数据库，那么现在问题来了，我究竟是想办法在刚才那个容器里面安装一个，还是说单独起一个容器作为数据库呢？

```shell
# 官方推荐
Separate containers let you version and update versions in isolation

Running multiple processes will require a process manager (the container only starts one process), which adds complexity to container startup/shutdown
```

![Todo App connected to MySQL container](https://docs.docker.com/get-started/images/multi-app-architecture.png)

+ 如何让彼此独立的容器之间可以通信? 

  ` docker network create todo-app` 来创建一个网络叫做 `todo-app`

  然后我们将准备启动的 mysql 容器和 app 容器都与这个网络进行绑定,这样子我们就可以实现容器间的通信。 

+ 首先让注意mysql容器注意启动时必须跟上一下几个环境变量

  + `MYSQL_HOST` - the hostname for the running MySQL server
  + `MYSQL_USER` - the username to use for the connection
  + `MYSQL_PASSWORD` - the password to use for the connection
  + `MYSQL_DB` - the database to use once connected

  具体信息大家可以去到 dockerhub 中来查看
  
  ```shell
  docker run -d \
       --network todo-app --network-alias mysql \ # 给容器在network下起一个别名
       -v todo-mysql-data:/var/lib/mysql \
       -e MYSQL_ROOT_PASSWORD=secret \
       -e MYSQL_DATABASE=todos \
     mariadb
  ```

  然后就可以进入mysql中查看效果
  
  + `docker exec -it <容器id> mysql -uroot -p` <数据表名>
+ `show databases;`
  
+ `select *from todo_items;`
  
+ 然后将数据库的信息作为环境变量传给app容器

  ```shell
  # 这个是如果我们刚才没有通过制作镜像,执行容器时需要的命令
  docker run -dp 3000:3000 \
     -w /app -v "$(pwd):/app" \
     --network todo-app \
     -e MYSQL_HOST=mysql \
     -e MYSQL_USER=root \
     -e MYSQL_PASSWORD=secret \
     -e MYSQL_DB=todos \
     node:12-alpine \
     sh -c "yarn install && yarn run dev"
  
  # 当我们制作好了镜像之后只需要
   docker run -dp 3000:3000 \
     --network todo-app \
     -e MYSQL_HOST=mysql \
     -e MYSQL_USER=root \
     -e MYSQL_PASSWORD=secret \
     -e MYSQL_DB=todos \
     myapp
  ```

### 推送镜像到远程

  如果我们制作镜像是需要可以给其它人使用的,那么我们需要推送到远程服务器中,以便它人可以像拉取官方镜像那样,拉去我们制作的镜像。

+ 创建一个`dockerhub`仓库

<img src="https://gitee.com/lzd-1230/img-host/raw/master/image/20211111163642.png" style="zoom:50%;" />

+ 在本地登录一下这个仓库

`docker login <仓库名称>`

+ 尝试 push 一下

```shell
  # docker push adam1230/test
  Using default tag: latest
  The push refers to repository [docker.io/adam1230/test]
  An image does not exist locally with the tag: adam1230/test
  
  # 发现没有成功,因为我们需要给本地的镜像打上一个标签,然后才能推送到远端去
```

  + 给刚才的镜像打一个标签

  ```
  docker tag <本地镜像> <dockerhub 账户>/<仓库名>
  docker push <dockerhub 账户>/<仓库名>
  docker login -u <你的dockerhub账号名>
  ```

## docker compose

+ 我们能否一次性启动多个容器，而不是一个个单独启动

利用`docker-compose`来修改我们刚才创建的两个容器

`docker-compose` 需要单独安装,安装起来也很方便。[Install Docker Compose](https://docs.docker.com/compose/install/)

+ 创建`docker-compose.yml`

```yaml
version: "3.7"

services:
  app:
    image: myapp
    ports:
      - 3000:3000
    working_dir: /app
    volumes:
      - ./:/app
    environment:
      MYSQL_HOST: mysql
      MYSQL_USER: root
      MYSQL_PASSWORD: secret
      MYSQL_DB: todos
  database:
    image: mariadb
    volumes:
      - todo-mysql-data:/var/lib/mysql
    environment:
      MYSQL_ROOT_PASSWORD: secret
      MYSQL_DATABASE: todos
volumes:
  todo-mysql-data:
```

+ 启动命令:`docker-compose up -d`
+ 停止命令:`docker-compose down [--volumes]`

## dockerfile

​    刚才在上文中我们使用了dockerfile来构建todo应用的App镜像,现在我们来看一下`dockerfile`的具体语法细节。

在学习 `dockerfile` 语法的时候大家需要区分一下两个过程 ①构建镜像时执行的命令②容器启动后执行的命令

### From

+ 为后面的镜像提供基础,该镜像可以是本地的,也可以是远端的任何有效镜像
+ **该命令必须为`Dockerfile`中的第一条命令**

`FROM <image>[:tag]`

比如我们可以将刚才镜像中配置依赖项的部分单独抽出来做成镜像,然后以后需要在环境中配置依赖的话直接使用本命令即可。

### RUN

+ 两种调用格式

  + ·`RUN <cmd+parameters>`
  + `RUN ["cmd","param1","param2"...`

  该指令的效果就是,在当前镜像的最新层中执行命令,然后执行的结果拿来生成新的层。**是在构建镜像时候需要执行的命令**

`RUN apt update && apt install vim -y`

### CMD

+ 其效果等价于在docker run的时候为其添加更多的执行内容

  ​	**是在启动容器之后才执行的内容**

+ 具体命令格式由三种

  ① CMD ["executable","param1","param2"] 使用 exec 执行，推荐方式；

  ② CMD command param1 param2 在 /bin/sh 中执行，提供给需要交互的应用；

  ③ CMD ["param1","param2"] 提供给 ENTRYPOINT 的默认参数；

  但`CMD`中可以仅包含命令的参数而没有指令,这样的结果就是将`CMD ["param1","param2"...]`面的参数传递给`ENTRYPOINT`

+ 一个`Dockerfile`中只有一个`CMD`,如果存在多个`CMD`,则仅有最后一个生效!

+ 如果在docker run 中又添加了命令,则会被覆盖

### ENTRYPOINT

+ ENTRYPOINT与CMD非常类似，不同的是通过`docker run`执行的命令不会覆盖ENTRYPOINT，而docker run命令中指定的任何参数，都会被当做参数再次传递给ENTRYPOINT。

    ```
    ENTRYPOINT ["executable", "param1", "param2"]
    ENTRYPOINT command param1 param2
    ```

如果我们的镜像没有`ENTRYPOINT` 和 `CMD` 这样子容器会一瞬间消失。

### ADD & COPY

+ 这两个命令的作用均是将文件传入容器中
  + 区别在于`ADD`可以获取网上的资源,类似于`wget`并且,如果资源为tar类型的文件会进行自动解压。
  + 而`COPY`则仅能获取本地资源,将资源传入容器后不会进行解压

```
	ADD <src>... <dest>
	ADD ["<src>",... "<dest>"] 用于支持包含空格的路径
	# 注意复制目录的时候要写全
	COPY dir /data/html/dir
```

### WORKDIR

+ 设置进入容器内的工作目录

```
   	WORKDIR <路径>
```

### EXPOSE

+ EXPOSE 指令通知 Docker 容器在运行时监听指定的网络端口。
+ 可以指定端口是监听TCP还是UDP，如果不指定协议，默认为TCP。 
+ **EXPOSE 指令实际上并不发布端口,实际含义类似于打算暴露某些端口**

```
	EXPOSE 80 443 # 打算暴露容器的80和443端口
```

在`docker run`的时候如果加上`-P`参数,就表示随机暴露端口

### VOLUME

+ 在容器内的某个目录创建一个挂载点,无法指定主机上的目录

```
	VOLUME ["/data1","/data2"]
	# 在构建容器的时候容器内部就会多出这两个目录
```

+ 数据卷的共享

有时希望容器间的挂载点共享,则可以通过`docker run --volumes-from <容器名>`实现

### ENV

+ 设置环境变量

```
	ENV <key> <value>	# 这种只能一行一个环境变量
	ENV <key>=<value>	# 种个变量为一个"<key>=<value>"的键值对，如果<key>中包含空格，可以使用\来进行转义，也可以通过""来进行标示；另外，反斜线也可以用于续行
```

## docker 网络

+ 四种网络模式

  + host: 和主机使用一样的 `net` 名称空间
  + **bridge**:  默认的设置, 容器使用独立的`net` 名称空间,并且连接到 `docker0` 网桥,通过 `NAT` 的方式与宿主机通信
  + **container**: 可以跟别的容器共享一个 `net` 名称空间,新的容器不会创建自己的网卡,而是和原有的那个容器共享。
  + none: 关闭网络功能

  <img src="https://gitee.com/lzd-1230/img-host/raw/master/image/20211129223729.png" style="zoom:50%;" />

在默认情况下, Docker 使用 bridge 和 NAT 来完成容器的网络通信。Docker守护进程在默认启动的时候，会自动创建虚拟设备 Docker0， 并且配置IP为  `172.17.0.1/16`

当容器启动的时候会创建虚拟的网络设备对,一端连接在容器的网络名称空间中,另一端加入 docker0,这样在同一个Host的容器之间就可以完成通信了。

当我们需要容器端口能够被外部访问时，我们会使用`-p <主机端口:容器端口>`来暴露端口。其原理就是创建了如下的`iptables`规则。

```shell
# 以-p 80:80 来举例
iptables ... -p tcp --dport80 -j DNAT --to-destination 172.17.xxx.xxx:80
```

+ 实验: 容器内的网络和外面的网络

  ```
  # 1.进入容器内安装net-tools
  # 2.看看二者的 ifconfig 有啥区别
  ```

### 参考资料

+ docker官方文档:[Orientation and setup | Docker Documentation](https://docs.docker.com/get-started/)
+ blog:[Dockerfile文件详解 - 百衲本 - 博客园 (cnblogs.com)](https://www.cnblogs.com/panwenbin-logs/p/8007348.html)

sudo curl -L https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose

