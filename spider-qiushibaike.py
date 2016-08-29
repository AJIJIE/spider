#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib

import urllib2
from bs4 import BeautifulSoup
import sys
import MySQLdb

reload(sys)
sys.setdefaultencoding('utf8')
#抓取多页面网页内容
for page in range(0,5):
#获取网页数据
    page =page+1
    print page
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


        x=item.find('h2').get_text()

        y=item.find('div',{'class':'content'}).get_text()
#链接数据库，特别注意utf8,编码问题
        conn = MySQLdb.Connect("127.0.0.1", "root", "root", "test", 3306,charset='utf8')
#使用cursor（）获取操作游标

        cursor = conn.cursor()
#将数据插入数据库
        sql = """INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME) VALUES ('%s','%s')""" % (x,y)

        try:
            # 执行sql语句
            cursor.execute(sql)


            # 提交到数据库执行
            conn.commit()
        except BaseException:
            # Rollback in case there is any error

            conn.rollback()




    cursor.close()
    conn.close()

#注意文件打开的模式，使用追加可以多次添加，如果使用‘w’，则只会出现一条信息
#open的文件，可以有具体的路径，如果没有该文件，则会创建一个这样的文件
#     file = open(r'C:\Users\123456\Desktop\2.txt', 'a+')
#     print text
#     file.write(str(text))
#
# # file.close()




