from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from DownloadUpdateExcelUploadWebtable.excel_update import Excel

driver_path = "D:\\Selenium_Training\\drivers\\chromedriver-win64 (1)\\chromedriver-win64\\chromedriver.exe"
service_obj = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service_obj)
url = "https://rahulshettyacademy.com/upload-download-test/"
driver.get(url)
driver.maximize_window()
time.sleep(5)

#1.dowloading the excel
#------------------------------------------------------------------------------------
driver.find_element(By.XPATH,"//button[@id='downloadButton']").click()

#2.Access the downloaded excel and update Banana price to 1000
excel_obj = Excel()
excel_obj.test_ExcelUpdate()

#3.upload the updated excel
#------------------------------------------------------------------------------------
#for uploading attribute "type = file" should be available in the html code else speak with dev team for it
driver.find_element(By.XPATH,"//input[@type='file']").send_keys("C:\\Users\\Sandesh\\Downloads\\download.xlsx")
time.sleep(5)
#4.validation by accessing he webtable and using assertion
#inspect for banana fruit, then navigate back to its parent untill complete row data is available
#then naviage to find the price column
# driver.find_element(By.XPATH,"//div[text()='Banana']/parent::div/parent::div/div[@data-column-id='4']").text
#remove hardcoding of frfuitname
fruit_name = 'Banana'
# driver.find_element(By.XPATH,"//div[text()='"+fruit_name+"']/parent::div/parent::div/div[@data-column-id='4']").text
#remove hardcoding of price column id, as it will change in case on new column addition or removal of column
#To achieve that get the column id dynamicaaly based on the column name = Price
price_column_id = driver.find_element(By.XPATH,"//div[text()='Price']").get_attribute("data-column-id")
actual_value = driver.find_element(By.XPATH,"//div[text()='"+fruit_name+"']/parent::div/parent::div/div[@data-column-id='"+price_column_id+"']").text

#assertion
assert actual_value == "1000"
time.sleep(3)

