from selenium import webdriver
import time

driver = webdriver.Chrome("./vendor/chromedriver") 

TARGET_URL = "https://www.google.co.jp"


print("1")

driver.get(TARGET_URL)

time.sleep(2)

driver.find_element_by_id('lst-ib').send_keys("text")

time.sleep(3) 

driver.quit()
#print("3")
