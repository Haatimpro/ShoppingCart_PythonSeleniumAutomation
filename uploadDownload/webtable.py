#requirement: extract the price of Apple from the webtable

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver_path="D:\\Selenium_Training\\drivers\\chromedriver-win64 (1)\\chromedriver-win64\\chromedriver.exe"
service_object = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service_object)
driver.implicitly_wait(3)
url="https://rahulshettyacademy.com/upload-download-test/"
driver.get(url)
driver.maximize_window()
time.sleep(5)

#requirement: get the price of Apple
#1.Reach the required fruit based on fruit name: Apple
    # driver.find_element(By.XPATH,"//div[text()='Apple']")
#2.reach to price colum, for which need to move back twice back to parent
    # driver.find_element(By.XPATH,"//div[text()='Apple']/parent::div/parent::div")
#3.Now move inside to child for the Price of Apple
    # actual_price = driver.find_element(By.XPATH,"//div[text()='Apple']/parent::div/parent::div/div[@data-column-id='4']").text
#4.remove hardcoding of fruit name
fruit_name = "Apple"
    # actual_price = driver.find_element(By.XPATH,"//div[text()='"+fruit_name+"']/parent::div/parent::div/div[@data-column-id='4']").text
#5.Remove hardcoding of price column(ata-column-id='4')
#column number may change in future, so pass it dynamically
#So get the price column number using text() and get_attribute()
price_columnNumber = driver.find_element(By.XPATH,"//div[text()='Price']").get_attribute("data-column-id")
actual_price = driver.find_element(By.XPATH,"//div[text()='"+fruit_name+"']/parent::div/parent::div/div[@data-column-id='"+price_columnNumber+"']").text
print(f"Actual price = {actual_price}")
