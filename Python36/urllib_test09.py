# -*- coding: UTF-8 -*-

import ssl
import random
from urllib import request

if __name__ == "__main__":
    ssl._create_default_https_context = ssl._create_unverified_context
    #访问网址
    url = 'https://www.baidu.com'
    #这是代理IP
    proxy = {'http':'113.121.254.244:808'}
    
    #创建ProxyHandler
    proxy_support = request.ProxyHandler(proxy)
    
    #创建Opener
    opener = request.build_opener(proxy_support)
    #添加User Angent
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36')]
    #安装OPener
    request.install_opener(opener)
    #使用自己安装好的Opener
    response = request.urlopen(url)
    #读取相应信息并解码
    html = response.read().decode("utf-8")
    #打印信息
    print(html)
