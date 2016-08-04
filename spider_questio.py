# -*- coding:utf-8 -*-
import re
import urllib
import urllib2
from bs4 import BeautifulSoup
import sys
reload(sys)
d={}

#获取网页数据
page = 3
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
#需要添加user_agent和headers，否则无法请求到源码
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
#请求网页
request = urllib2.Request(url,headers = headers)
#打开网页
response = urllib2.urlopen(request)
#读取数据
#使用bs4 库，读取<div class=content ></div>中的内容
html_doc = response.read()
soup =BeautifulSoup(html_doc, 'html.parser')
contents=soup.find_all('div',class_='content')
for content in contents:
    text = content.get_text()
    print text
#如何使用beautifulsoup获取作者，内容，时间等一组内容？








# #注意文件打开的模式，使用追加可以多次添加，如果使用‘w’，则只会出现一条信息
# #open的文件，可以有具体的路径，如果没有该文件，则会创建一个这样的文件
#     file = open(r'C:\Users\123456\Desktop\2.txt', 'a+')
#     print text
#     file.write(str(text))
#
# file.close()




