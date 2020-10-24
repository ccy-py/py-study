from urllib  import  request,parse
import chardet


# cookie_hdr = request.HTTPCookieProcessor()
# opener = request.build_opener(cookie_hdr)
# req=request.Request("http://www.baidu.com/",headers={"User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"})
#
# with request.urlopen(req) as f:
#     # bla...bla...bla
#     html = f.read()
#     uncode=chardet.detect(html)
#     print(uncode)
#     print(f'f1:{html}')

value={'query':"1234"}
data=parse.urlencode(value).encode('UTF-8')
req=request.Request("https://fanyi.baidu.com/langdetect",data=data,headers={"User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"})
resp=request.urlopen(req)
print(resp.read())
