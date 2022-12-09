from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\SeleniumClient\chromedriver.exe")
driver.get("https://gmail.com")

user = driver.find_element_by_id("identifierId")
user.send_keys("amauryarmando@gmail.com")
user.send_keys(Keys.ENTER)

pwd = driver.find_element_by_name("password")
pwd.send_keys(".callofduty.")
pwd.send_keys(Keys.ENTER)