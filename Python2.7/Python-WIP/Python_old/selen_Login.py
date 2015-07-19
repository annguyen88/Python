import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('http://webmail.iprogram.info')

elem = browser.find_element_by_name("user")
elem.send_keys("code@iprogram.info")

elem = browser.find_element_by_name("pass")
elem.send_keys("test123")

elem = browser.find_element_by_name("login").click()

time.sleep(3)

browser.close()

#username = selenium.find_element_by_id("user")
#password = selenium.find_element_by_id("pass")

#username.send_keys("test@iprogram.info")
#password.send_keys("test123")

#selenium.find_element_by_name("login").click()
