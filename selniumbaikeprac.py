import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://baike.baidu.com/")
elem_inp = driver.find_element_by_xpath('//*[@id="query"]')
elem_inp.clear()
elem_inp.send_keys(u"故宫")
elem_inp.send_keys(Keys.RETURN)
time.sleep(1)
sreach_window = driver.current_window_handle #此行代码用来定位当前页面
time.sleep(2)
elem_name = driver.find_elements_by_xpath('/html/body/div[4]/div[2]/div/div[2]/div[8]/dl[1]') 
for i in elem_name:
    print(i.text)
    print('\n')
driver.close()