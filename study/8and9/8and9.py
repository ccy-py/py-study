import requests
from bs4 import BeautifulSoup


htmlText=requests.get("http://www.baidu.com")
bsObj=BeautifulSoup(htmlText.text,"lxml")    #将html对象转化为BeautifulSoup对象
ulList=bsObj.findAll("img")
print(ulList)
