from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get('https:/youtube.com')
searchbox = driver.find_element("xpath", '/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
searchbox.send_keys('clasicos del regueton')
searchButton = driver.find_element("xpath", '/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button') 

searchButton.click()
time.sleep(60)

driver.quit()