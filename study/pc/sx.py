import asyncio
import gzip
import http.cookiejar
import json
import os
import random
import redis
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from io import BytesIO
from urllib import request, parse

from bs4 import BeautifulSoup

url = "http://www.xbiquge.la/36/36820/"
headers = {
    "User-Agent": " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
    'Accept-encoding': 'gzip'
}

user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/61.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
    ]
# 创建一个最大容量为1的线程
executor = ThreadPoolExecutor(max_workers=16)

proxy_list = [
]


def main():
    cookies = http.cookiejar.CookieJar()
    handler = request.HTTPCookieProcessor(cookies)
    opener = request.build_opener(handler)

    ht = jixHtml(opener, url)

    tasks = []
    index = 0
    for zj in ht.find(id='list').findAll("a"):
        index += 1
        task = executor.submit(getHtml, opener, index, zj.text,
                               parse.urlparse(url).scheme + "://" + parse.urlparse(url).netloc + zj['href'])
        tasks.append(task)

    for future in as_completed(tasks):
        # spider方法无返回，则返回为None
        data = future.result()
        print(f"main:{data}")

    textFilsh = True
    while textFilsh:
        files = os.listdir("txt")
        files.sort(key=lambda x: int(x[:-4]))
        if len(ht.find(id='list').findAll("a")) == len(files):
            textFilsh = False
            with open("hj.txt", 'a', encoding="UTF-8") as f:
                for t in files:
                    lines = open("txt\\" + t, 'r', encoding="UTF-8").readlines()
                    f.writelines(lines)
                    f.write("\r\n")
                    f.write("\r\n")


def jixHtml(opener, URL):
    headers['User-Agent'] = random.choice(user_agent_list)
    req = request.Request(URL, headers=headers)
    resp = openurl(opener, req)
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
    ht = BeautifulSoup(htmls, "lxml")
    return ht


def openurl(opener, req):
    s = r.lindex("dlip", random.randint(1, r.llen("dlip")))
    # 这里要用到我们的request.ProxyHandler代理管理器
    proxy_handler = request.ProxyHandler(json.loads(s))
    # 制作发起请求管理器request.build_opener ，把我们管理器都放进去
    openr = request.build_opener(proxy_handler)
    resp = None
    jx = False
    try:
        resp = openr.open(req)
    except Exception as e:
        print(e)
        jx = True
    finally:
        print('最后执行')
        if jx:
            time.sleep(1)
            resp = openurl(opener, req)

    return resp


def getHtml(opener, index, title, URL):
    ht = jixHtml(opener, URL)
    text = ht.find(id="content").text
    ght = ht.find(id="content").find("p").text
    print(title)
    if not os.path.exists("txt"):
        os.mkdir('txt')
    with open(os.getcwd() + "/txt/" + str(index) + ".txt", 'a', encoding="UTF-8") as f:
        f.write(title)
        f.write("\r\n")
        f.write(text)
        f.write("\r\n")
        f.write("\r\n")
        f.write("\r\n")
        f.write("\r\n")

    # prop = {"title": title, "text": text.replace(ght, "")}
    # list.insert(index,prop)


if __name__ == '__main__':
    list = list()
    pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    asyncio.run(main())
