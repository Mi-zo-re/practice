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
if __name__ == '__main__':
    url = 'https://movie.douban.com/top250?start=0&filter='
    crawl(url)