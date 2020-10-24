import urllib
import requests
from urllib import  request,parse
import http.cookiejar
from study.wx.LoginWx import LoginWx

wxLoginUrl = "https://wx.qq.com/"
wxheaders = {
    "User-Agent": " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    'Referer': "wx.qq.com",
    'Host': "wx.qq.com",
    'Accept-encoding': 'gzip, deflate, br'
}
cookies=http.cookiejar.CookieJar()
handler=request.HTTPCookieProcessor(cookies)
opener = request.build_opener(handler)

login=LoginWx(opener,wxLoginUrl,wxheaders)
login.getLogin()

