import gzip
import http.cookiejar
import time
import matplotlib.pyplot as plt
from io import BytesIO
from urllib import request
from wordcloud import WordCloud
import jieba
import numpy
import pandas
from PIL import Image
from bs4 import BeautifulSoup
import matplotlib
matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)

url = "https://movie.douban.com/subject/25779217/comments?start={}&limit=20"
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


def main(index=0, content=""):
    cookies = http.cookiejar.CookieJar()
    handler = request.HTTPCookieProcessor(cookies)
    opener = request.build_opener(handler)

    ht = jixHtml(opener, url.format(index))

    tasks = []
    index = 0
    for t in ht.findAll(class_='comment-content'):
        content += str(ht.findAll(class_='comment-content')[0].text).strip().replace(" ","")
    return content


def jixHtml(opener, URL):
    # headers['User-Agent'] = random.choice(user_agent_list)
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
    resp = None
    jx = False
    try:
        resp = opener.open(req)
    except Exception as e:
        print(e)
        jx = True
    finally:
        print('最后执行')
        if jx:
            time.sleep(1)
            resp = openurl(opener, req)

    return resp



if __name__ == '__main__':
    content = ""
    for i in range(10):
        time.sleep(1)
        content = main(i*20, content)
    cs = jieba._lcut(content)
    words_df = pandas.DataFrame({"segment": cs})
    stopwords = pandas.read_csv('stopwords.txt', index_col=False, quoting=3, sep='\t', names=['stopword'],
                                encoding='gbk')  # quoting=3全部引用
    words_df = words_df[~words_df.segment.isin(stopwords.stopword)]
    words_stat = words_df.groupby('segment').agg(计数=pandas.NamedAgg(column='segment', aggfunc='size')).reset_index().sort_values(
        by='计数', ascending=False)
    print(words_stat.head())
    img=numpy.array(Image.open("11.png"))
    wordcloud=WordCloud(font_path="SimHei.ttf",mask=img,background_color="white",max_font_size=80,min_font_size=6,scale=10)
    word_frequence = {x[0]:x[1] for x in words_stat.head(1000).values}

    word_frequence_list = []
    for key in word_frequence:
        temp = (key,word_frequence[key])
        word_frequence_list.append(temp)

    wordcloud=wordcloud.fit_words( dict(word_frequence_list))
    plt.figure()
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


