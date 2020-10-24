import urllib
import gzip
from io import BytesIO
from urllib import request, parse
from bs4 import BeautifulSoup
import time
import os
from PIL import Image
import matplotlib.pyplot as plt

class LoginWx:
    def __init__(self,opener,wxLoginUrl,wxheaders):
        self.opener=opener
        self.wxLoginUrl=wxLoginUrl
        self.wxheaders=wxheaders
        self.uuid=""

    def getCode(self):
       url="https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb&redirect_uri=https%3A%2F%2Fwx.qq.com%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&fun=new&lang=zh_CN&_="+str(int(time.time()))
       req = request.Request(url, headers=self.wxheaders)
       resp = self.opener.open(req)
       acceptEncoding = resp.info().get('Content-Encoding')
       htmls = ''
       if acceptEncoding == 'gzip':
           htmls = resp.read()
           buff = BytesIO(htmls)
           f = gzip.GzipFile(fileobj=buff)
           htmls = f.read().decode('utf-8')
       else:
           htmls = resp.read().decode('utf-8')
       # print(htmls)
       # ht = BeautifulSoup(htmls, "lxml")
       ud=htmls.split('window.QRLogin.uuid = "')[1]
       self.uuid=ud.replace('";',"")
       print(self.uuid)


    def getLoginImg(self):
        url="https://login.weixin.qq.com/qrcode/"+self.uuid
        req = request.Request(url, headers=self.wxheaders)
        request.urlretrieve(url, r'{}\{}'.format(os.getcwd(), "test.jpg"))

        pil_im = Image.open( "test.jpg")
       # plt.figure("dog")
        plt.imshow(pil_im)
        plt.show()

    def getLogin(self):
        self.getCode()
        self.getLoginImg()
        # req = request.Request(self.wxLoginUrl, headers=self.wxheaders)
        # resp = self.opener.open(req)
        # acceptEncoding = resp.info().get('Content-Encoding')
        # htmls = ''
        # if acceptEncoding == 'gzip':
        #     htmls = resp.read()
        #     buff = BytesIO(htmls)
        #     f = gzip.GzipFile(fileobj=buff)
        #     htmls = f.read().decode('utf-8')
        # else:
        #     htmls = resp.read().decode('utf-8')
        # # print(htmls)
        # ht = BeautifulSoup(htmls, "lxml")
        # ht.find(".qrcode")
        # print(ht)


print(time.time())
