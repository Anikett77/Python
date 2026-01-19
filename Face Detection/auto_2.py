# Automation of youtube shorts scroll

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver,20)
driver.get("https://www.youtube.com/")
# short = driver.find_element(By.XPATH, '//*[@title="Shorts"]')
# shorts = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@title="Shorts"]'))) 
# shorts.click()
# time.sleep(5)
try:
    shorts = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@title="Shorts"]'))) 
    shorts.click()
    time.sleep(5)
    search_box = driver.find_element(By.NAME,"search_query")
    search_query = "techsimplus learning"
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(10)
    first_short = driver.find_element(By.XPATH, '//*[@id="contents"]/grid-shelf-view-model[1]/div[1]/div')
    first_short.click()
    time.sleep(4)
    while True:
        error = 0
        while True:
            time.sleep(5)
            break
        try:
            nextBtn = driver.find_element(By.XPATH, '//*[@id="navigation-button-down"]/ytd-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div[2]')
            nextBtn.click()
            time.sleep(5)
        except:
            break
        time.sleep(1)
except:
    print("error")
driver.quit()