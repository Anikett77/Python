# Automation of linkedin Login

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("https://in.linkedin.com/")
time.sleep(2)
elements = driver.find_element(By.XPATH, '/html/body/div[2]/nav/div/a[2]')
elements.click()
time.sleep(10)
number = driver.find_element(By.XPATH, '//*[@id="phone-number"]')
password = driver.find_element(By.XPATH,'//*[@id="password"]')
number.send_keys("7879482501")
password.send_keys("123456")
cont = driver.find_element(By.XPATH, '//*[@id="join-form-submit"]')
time.sleep(10)
cont.click()
driver.quit()