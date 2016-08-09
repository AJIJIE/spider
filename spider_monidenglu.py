
import urllib
import urllib2
from bs4 import  BeautifulSoup


login_url='https://www.zhihu.com/login/email'
login_data={'_xsrf':'0a6ed8b54088e829e12474fa443e11fc',
            'password':'595jzj901121','captcha_type':'cn',
            'remember_me':'true',
            'email':'931473342@qq.com'}
login_headers={'Accept':'*/*',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'no-cache',
'Connection':'keep-alive',
'Content-Length':'118',
'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie':'d_c0="ABCAeWj_rgmPTrjtJccpV9T6M4-aIt5lLBA=|1459142718"; _za=a58d1a2b-c497-4088-8392-bca90e7f45f0; _zap=01f8fc5e-ff4c-4c15-84af-5d19571ea5b7; _xsrf=0a6ed8b54088e829e12474fa443e11fc; q_c1=130c9688e07648058515e71379d0cebb|1470626443000|1467865262000; __utmt=1; l_cap_id="YTc3ODcyNWM3NTkxNGViMWJkMmM0MjM5NmRlM2EzOTE=|1470727981|c2255fe3952391f47520b037ade9ac37de2f91da"; cap_id="ZDI2YjU5NTMyNWUxNGIxY2JjZGNlY2M2NjQ1M2QwOTg=|1470727981|6a6cfc544b2a68519522f377d933b52150ebdce5"; login="YTIxNjhiNDM5YmY1NDFmNmIwNmY5Y2IyMDVmOGJmYmM=|1470727998|434c473f11004d5ddeafba0206c16352241451d3"; __utma=51854390.1691867628.1470279691.1470629922.1470727311.8; __utmb=51854390.24.10.1470727311; __utmc=51854390; __utmz=51854390.1470727311.8.8.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=51854390.000--|2=registration_date=20150119=1^3=entry_date=20160707=1; n_c=1',
'Host':'www.zhihu.com',
'Origin':'https://www.zhihu.com',
'Pragma':'no-cache',
'Referer':'https://www.zhihu.com/',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
'X-Requested-With':'XMLHttpRequest',
'X-Xsrftoken':'0a6ed8b54088e829e12474fa443e11fc'}
page=urllib2.Request(login_url,data=login_data,headers=login_headers)
html=urllib2.urlopen('https://www.zhihu.com/question/49385999#answer-41765926')
data=html.read()
soup = BeautifulSoup(data, 'html.parser')
print data


