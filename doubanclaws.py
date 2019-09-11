from bs4 import BeautifulSoup
import re
import urllib.request

def crawl(url):
    content = urllib.request.urlopen(url)
    pull = content.read()
    pull = pull.decode("UTF-8")
    soup = BeautifulSoup(pull, "html.parser")
    print("豆瓣top250")
    for tag in soup.find_all(attrs={"class": "item"}):
        num = tag.find('em').get_text()
        print("序号: "+num)
        name = tag.find(attrs={'class': 'title'}).get_text()
        print("电影名: "+name)
        com = tag.find(attrs={'class': 'rating_num'}).get_text()
        com = com.replace("\n", "")
        print("评分："+com)
        info = tag.find(attrs={'class': 'inq'})
        if(info):
            content = info.get_text()
            print("影评： "+content)
        print('\n')

if __name__ == '__main__':
    i = 0 #计数器
    while i < 10:
        num = i*25
        url = 'https://movie.douban.com/top250?start=' + str(num) + '&filter='
        crawl(url)
        i += 1