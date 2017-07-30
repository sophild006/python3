#-*- coding:utf-8 -*-
import re
import requests
from urllib import request

url = 'http://image.baidu.com/search/flip?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1460997499750_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%B0%8F%E9%BB%84%E4%BA%BA'


html = request.urlopen(url)
pic_url = re.findall('"objURL":"(.*?)",',html,re.S)
print(pic_url)
i = 0
for each in pic_url:
    print (each)
    try:
        pic= requests.get(each, timeout=10)
    except requests.exceptions.ConnectionError:
		print ('failed')
        continue
    string = 'static\\'+str(i) + '.jpg'
    fp = open(string,'wb')
    fp.write(pic.content)
    fp.close()
    i += 1