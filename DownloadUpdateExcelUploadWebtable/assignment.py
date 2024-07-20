from selenium import  webdriver

import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver_path = "D:\\Selenium_Training\\drivers\\chromedriver-win64 (1)\\chromedriver-win64\\chromedriver.exe"
service_obj = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
url = "https://rahulshettyacademy.com/loginpagePractise/"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.XPATH,"//a[@class='blinkingText']").click()
#opens new window/tab, so capture it
window_id = driver.window_handles
# print(window_id)
parentWindow_id = window_id[0]
childWindow_id = window_id[1]
#switch to child window
driver.switch_to.window(childWindow_id)
#capture the text
required_text = driver.find_element(By.XPATH,"//p[@class='im-para red']").text
#print(required_text)
#extract username from the text captured
# username = required_text[19:48]
firstsplit = required_text.split("at")
# print(firstsplit[0])
secondsplit = firstsplit[1].split("with")
# print(secondstring[1])
username = secondsplit[0].strip()
# print(username)

#switch to parent window
driver.switch_to.window(parentWindow_id)
#username textbox
driver.find_element(By.XPATH,"//input[@id='username']").send_keys(username)
#password textbox
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("12345")
#Signin Button
driver.find_element(By.XPATH,"//input[@id='signInBtn']").click()
#wait till alert message pops up and capture and print it
wait = WebDriverWait(driver ,5)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//form[@id='login-form']/div[@class='alert alert-danger col-md-12']")))
alert_message = driver.find_element(By.XPATH,"//form[@id='login-form']/div[@class='alert alert-danger col-md-12']").text
print(alert_message)

driver.quit()



