import redis,json
import telnetlib
import threading
import time
from urllib import request

from bs4 import BeautifulSoup

url = "https://www.kuaidaili.com/free/inha/{}/"
headers = {
    "User-Agent": " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
}

ipList = list()


def jxHtml(index=1):
    time.sleep(3)
    req = request.Request(url.format(index), headers=headers)
    html = request.urlopen(req).read()
    bfs = BeautifulSoup(html, 'lxml')
    for tdRow in bfs.find('table').find('tbody').findAll("tr"):
        ip = tdRow.find('td', attrs={"data-title": "IP"}).text
        port = tdRow.find('td', attrs={"data-title": "PORT"}).text
        lx = tdRow.find('td', attrs={"data-title": "类型"}).text
        threading.Thread(target=telnet1, args=(ip, port, lx)).start()


def telnet1(ip, port, lx):
    try:
        telnetlib.Telnet(ip, port=port, timeout=4)
    except:
        print('connect failed')
    else:
        print('connect success')
        r.lpush("dlip",json.dumps({lx : ip + ":" + port}))


if __name__ == '__main__':
    pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    for i in range(1, 3000):
        jxHtml(i)
