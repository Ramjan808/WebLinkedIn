from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import requests
from bs4 import BeautifulSoup

ser_obj = Service("D:/SP/Driver/chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)
driver.get("https://www.linkedin.com/home")


# Replace 'your_email' and 'your_password' with your LinkedIn credentials
email_input = driver.find_element(By.NAME,"session_key")
email_input.send_keys("miamalkova180@gmail.com")
wait = WebDriverWait(driver, 20)
password_input = driver.find_element(By.NAME,"session_password")
password_input.send_keys("miamal12309820")

password_input.send_keys(Keys.RETURN)

#Allow some time for the page to load and log in
time.sleep(90)