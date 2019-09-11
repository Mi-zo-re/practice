from bs4 import BeautifulSoup
import re
import urllib.request

def craw(url):
    page = urllib.request.urlopen(url)
    view = page.read()
    view = view.decode("UTF-8")
    soup = BeautifulSoup(view, "html.parser")
    dep = soup.find(attrs={"class": "overthrow table_container"})
    for nuc in dep.find_all("tbody"):
        for tag in nuc.find_all("tr"):
            no = tag.find(attrs={"data-stat": "number"})
            no = no.get_text()
            print("号码："+no)
            name = tag.find(attrs={"data-stat": "player"})
            name = name.get_text()
            print("姓名: "+name)
            pos = tag.find(attrs={"data-stat": "pos"})
            pos = pos.get_text()
            print("位置： "+pos)
            print('\n')

if __name__ == "__main__":
    url ="https://www.basketball-reference.com/teams/MEM/2019.html"
    craw(url)