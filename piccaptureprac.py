import urllib.request
from selenium import webdriver

def cbk(a,b,c):
    per = 100.0*a*b/c
    if per>100:
        per=100
    print('%.2f%%'% per)

drive = webdriver.Firefox()
drive.get("https://www.quanjing.com/creative/topic/9")
pas = drive.find_element_by_xpath('/html/body/section/div[2]/section/div/a[1]/img')
url = pas.get_attribute('src')
urllib.request.urlretrieve(url, 'test13.png',cbk)