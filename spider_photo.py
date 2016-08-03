#coding=utf-8
import urllib
import re

#获取网页数据
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
#正则匹配，筛选图片
def getImg(html):
    # reg = r'src="(.+?\.jpg)" pic_ext'
    reg = r'[a-zA-z]+://[^\s]*.jpg'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
#将筛选出的图片保存到指定位置，urltetrieve下载图片到指定位置
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,r'C:/Users/123456/Desktop/3/%s.jpg' % x)
        x+=1

url='http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%88%98%E8%AF%97%E8%AF%97&oq=%E5%88%98%E8%AF%97%E8%AF%97&rsp=-1'
html = getHtml(url)

print getImg(html)
