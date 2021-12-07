# Gerapy的介绍:
```python
gerapy是一款 分布式爬虫管理框架，支持python，基于Scrapy、Scrapyd、Scrapyd-Client、
Scrapy-Redis、Scrapy-API、Scrapy-Splash、Jinjia2、Django、Vue.js开发，
Gerapy可以帮助我们:
    1. 更方便地控制爬虫运行
    2. 更直观地查看爬虫状态
    3. 更实时地查看爬虫结果
    4. 更简单地实现项目部署
    5. 更统一地实现主机部署
```
# Gerapy的安装(算是集成包)
```python
1. 执行下面的命令，等待安装完毕
pip install gerapy
2. 验证是否安装成功
在终端中执行 gerapy 会出现如下命令
Gerapy 0.9.7 - Distributed Crawler Management Framework
```
# Gerapy配置启动
```python
1. 创建一个项目
gerapy init
2. 对数据库进行初始化(在gerapy目录中操作)
其实gerapy是基于django的，所以命令很像，小白的认知，gerapy migrate 数据库的生成
gerapy migrate
对数据库初始化之后会生成一个SQLite数据库，数据库保存主机配置信息和部署版本等
gerapy createsuperuser 创建用户名密码，程序运行后使用(后面登录使用)
```
![image-20211208001720575](D:\王D盘归属\都云\Reptile_练习\项目-Gerapy\image-20211208001720575.png)

# 启动Gerapy服务

```python
gerapy runserver
此时启动gerapy服务的这台机器的8000端口上开启了gerapy服务，在浏览器中输入http://localhost:8000就
能进入gerapy 的管理界面，在管理界面就可以进行主机管理和界面管理
```

![image-20211208001916437](D:\王D盘归属\都云\Reptile_练习\项目-Gerapy\image-20211208001916437.png)

![image-20211208002020740](D:\王D盘归属\都云\Reptile_练习\项目-Gerapy\image-20211208002020740.png)

![image-20211208002442460](D:\王D盘归属\都云\Reptile_练习\项目-Gerapy\image-20211208002442460.png)

# 通过Gerapy配置管理Scrapy项目

## 1. **配置主机**：添加scrapyd主机

![image-20211208002700043](D:\王D盘归属\都云\Reptile_练习\项目-Gerapy\image-20211208002700043.png)

![image-20211208003008670](D:\王D盘归属\都云\Reptile_练习\项目-Gerapy\image-20211208003008670.png)

**需要添加IP、端口，以及名称，点击创建即可完成添加，点击返回即可看到当前添加的Scrapyd服务列表，创建成功后，我们可以在列表中查看已经添加的服务。**

****

## 2. 执行爬虫，就点击调度，然后运行。(前提是：我们配置的scrapyd中已经发布了爬虫项目。)

![image-20211208003758386](D:\王D盘归属\都云\Reptile_练习\项目-Gerapy\image-20211208003758386.png)

开启指定端口6800

![image-20211208005653280](D:\王D盘归属\都云\Reptile_练习\项目-Gerapy\image-20211208005653280.png)

1. 配置Projects 1.我们可以讲scrapy项目直接放到/gerapy/projects下。

   ![image-20211208004428858](D:\王D盘归属\都云\Reptile_练习\项目-Gerapy\image-20211208004428858.png)

2. 可以在gerapy后台可以看到这个项目

![image-20211208004603059](D:\王D盘归属\都云\Reptile_练习\项目-Gerapy\image-20211208004603059.png)

​	3.点击部署按钮进行打包和部署，在右下角我们可以输入打包时的描述信息，类似GIT的commit 信息，然后点击打包按钮，即可发现Gerapy会提示打包成功，同时在左侧显示打包的结果和打包名称。

​	![image-20211208005138782](D:\王D盘归属\都云\Reptile_练习\项目-Gerapy\image-20211208005138782.png)

![image-20211208005238710](D:\王D盘归属\都云\Reptile_练习\项目-Gerapy\image-20211208005238710.png)

打包后再点击部署就可以了

# Gerapy 与 scrapyd 有什么关联吗?

**我们仅仅使用scrapyd是可以调用scrapy进行爬虫. 只是 需要使用命令行开启爬虫**

```python
curl http://127.0.0.1:6800/schedule.json -d project=工程名 -d spider=爬虫名
```

