
# -*- coding:utf-8 -*-
import urllib
import urllib2
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')

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
#find_all 格式，中的attrs，可以更精确的定义<div class=content ></div>
items=soup.find_all('div',{'class':'article block untagged mb15'})

#总的循环中，寻找每一个条目时，再从中筛选出，内容和作者
for item in items:

    print item.find('h2').get_text(),item.find('div',{'class':'content'}).get_text()
#注意文件打开的模式，使用追加可以多次添加，如果使用‘w’，则只会出现一条信息
#open的文件，可以有具体的路径，如果没有该文件，则会创建一个这样的文件
#     file = open(r'C:\Users\123456\Desktop\2.txt', 'a+')
#     print text
#     file.write(str(text))
#
# # file.close()




