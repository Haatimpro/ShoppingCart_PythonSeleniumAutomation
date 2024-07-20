import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from uploadDownload.update_excel import excel_update_data

driver_path="D:\\Selenium_Training\\drivers\\chromedriver-win64 (1)\\chromedriver-win64\\chromedriver.exe"
service_object = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service_object)
driver.implicitly_wait(3)
url="https://rahulshettyacademy.com/upload-download-test/"
driver.get(url)
driver.maximize_window()
time.sleep(5)
#downloading a file
#----------------------------------------------------------------------------
#driver.find_element(By.XPATH,"//button[@id='downloadButton']").click()
dowlnoaded_file_path = "C:\\Users\\Sandesh\\Downloads\\download.xlsx"

#update excel
#------------------------------------------------------------------
excel_update_data(dowlnoaded_file_path,"Apple","Price","500")

# #uploading a file
#-------------------------------------------------------------------------------------------------
upload_file = driver.find_element(By.XPATH,"//input[@type='file']")
upload_file.send_keys(dowlnoaded_file_path)
fruit_name = "Apple"
price_columnNumber = driver.find_element(By.XPATH,"//div[text()='Price']").get_attribute("data-column-id")
actual_price = driver.find_element(By.XPATH,"//div[text()='"+fruit_name+"']/parent::div/parent::div/div[@data-column-id='"+price_columnNumber+"']").text

assert actual_price == "500"
# #wait till confirmation message displays
# confirm_msg_locator = (By.XPATH,"//div[@class='Toastfy__toast-body']/div[2]")
# wait = WebDriverWait(driver,5)
# wait.until(expected_conditions.presence_of_element_located(confirm_msg_locator))
#
# #extracting text from confiramtion message
# # confirm_message = driver.find_element(*confirm_msg_locator).text
# # print(confirm_message)
# time.sleep(3)
