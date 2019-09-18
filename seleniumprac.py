import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("http://www.baidu.com/")
assert "百度" in driver.title  #使用断言判定title是否有百度字段
print(driver.title)
elem = driver.find_element_by_name("wd")
elem.send_keys(u"数据分析")
elem.send_keys(Keys.RETURN)  #回车键

time.sleep(10)
driver.save_screenshot('baidu.png')
driver.close() #关闭驱动
driver.quit() #推出驱动
