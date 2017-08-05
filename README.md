# spider
这是我学习python爬虫时所写的一些代码和总结
# http超文本传输协议
* 一个url对应网络上的一个资源
* 浏览器通过http协议进行相应的资源传输
* 通过url和命令管理资源， 每次操作独立无状态， 网络通道及服务器成为了黑盒子
# Requests库的使用
说明：Requests库中的7个方法分别对应http协议中的7个方法
## 安装
1. 命令 pip install requests
## 库的原理
1. 模块最基本的方法是request方法，其它6个方法都是以该方法作为基本方法，并设定一定的默认参数所形成的方法，所以也可以说request库中只有一个方法
2. request的执行过程是，构造一个向服务器请求资源的request对象，然后服务器响应返回一个包含服务器资源的response对象, 由于其它6个方法都是以request为基本的方法，所以其它6个方法的流程也是如此
## response对象
### 属性
1. status_code:http请求的返回状态 200代表连接成功，其它和404都是失败
2. text: url对应页面内容文本形式
3. encoding: 从http header中猜测的响应内容的编码方式（charset字段标明，如果没有则为iso-8859-1）
4. apparent_encoding: 从内容中分析出编码方式，通常更可靠
5. content http响应内容的2进制形式
​
## 主要方法
1. request()构造一个请求， 支撑该模块中的其它方法
2. get() 原型：`request.get(url, params=None, ** kwargs)`
params **是url中的额外参数**， kwarges是12个控制访问参数
原理 源码
`
def get(url, params=None, **kwargs)
kwargs,setdefault('allow redirects', True
return request('get', params=params, **kwargs)
`
获取html网页的主要方法,对应http协议的GET()
3. head()获取html网页的头信息的方法
4. post()向网页中提交post请求的方法
5. put向网页中提交put请求的方法
6. patch() 向网页中提交局部修改请求的方法
7. delete() 向网页中提交删除请求的方法
## 常用控制访问参数
1. params 用params = {'key1':'value1'}, 这样就可以在url后面构造参数
2. headers = hd, 可以在字典hd总制定需要更改的headers属性，常常更改user-agent字段来伪装成浏览器 
## 异常
* 通常是使用response对象中的raise_for_status()方法检测，如果不是200，则抛出异常
1. ConnectionError 网络连接错误，dns查询失败，拒绝连接等
2. HttpError http错误异常
3. URLRequired url缺失异常
4. TooManyRedirects 重定向异常
5. 等等
