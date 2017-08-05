#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
import requests as re

########爬虫通用框架
def getHtmlText(url):
    try:
        r = re.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '出错了'

####访问有防护措施的网页_亚马逊，修改request对象headers中user-agent字段,伪装成浏览器
def getHtmlText2(url):
    try:
        kv = {'user-agent':'Mozilla/5.0'}
        r = re.get(url, headers = kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '出错了'
####################百度搜索关键词提交接口，在url中添加关键词
def getHtmlText3(url, keyword):
    kv = {'wd':keyword}
    try:
        r = re.get(url, params = kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '出错了'

####################爬取图片，二进制资源：图片，视频，动画,可以把r.content写到文件来保存
def getHtmlText4(url, path, filename):
    try:
        import os
        r = re.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        with open(os.path.join(path, filename), 'wb') as f:
            f.write(r.content)
            print '文件保存成功'
        return r.text
    except:
        return '出错了'
if __name__ == '__main__':
    print (getHtmlText4('http://image.nationalgeographic.com.cn/2015/0608/20150608104508733.jpg', 'C:/Users/lenovo-pc/Desktop', 'a.jpg')[:1000])
