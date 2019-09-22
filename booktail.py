import urllib.request
import urllib
from bs4 import BeautifulSoup
import urllib.error

def book(url):
    headers = ('user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/77.0.3865.90 Safari/537.36')
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    html = opener.open(url)
    bs = BeautifulSoup(html, 'html.parser')
    dep = bs.find(attrs={"id": "main"})
    for nuc in dep.find_all(attrs={"class": "kratos-entry-border-new clearfix"}):
        name = nuc.find(attrs={"class": "kratos-entry-title-new"})
        print("书名： " + name.text)
        conent = nuc.find(attrs={"class": "kratos-entry-content-new"})
        print("内容： " + conent.text)
        print("\n")


if __name__ == "__main__":
    url = 'https://www.d4j.cn/'
    book(url)
    i = 2
    while i <= 154:
        url = 'https://www.d4j.cn/page/'+str(i)
        book(url)
        i += 1