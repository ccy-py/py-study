import requests
from bs4 import BeautifulSoup


class imaga():

    def __init__(self):
        self.urls = list()
        self.total = 1
        self.url = "https://tieba.baidu.com/p/6900733737?pn="
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) Chrome/59.0.3071.109 Safari/537.36'
        }
        self.s = requests.session()
        self.s.headers.update(self.headers)

    def getImage(self, page=1):
        print(page)
        html = requests.get(self.url + str(page))
        obj = BeautifulSoup(html.text, "lxml")
        if (page == 1):
            self.total = obj.select("li[class=l_reply_num] > span")[3::1][0].text
        for u in obj.findAll("img"):
            self.urls.append(u.attrs['src'])
        print(self.urls)

if __name__ == '__main__':
    img = imaga()
    img.getImage()
    if int(img.total) >1:
        for i in range(int(img.total)):
            if i >0:
                img.getImage(i+1)
    print(img.urls)
