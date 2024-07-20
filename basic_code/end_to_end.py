import time

from selenium import webdriver
#import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver_path = "D:\\Selenium_Training\\drivers\\chromedriver-win64 (1)\\chromedriver-win64\\chromedriver.exe"
service_object = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service_object)
driver.implicitly_wait(5)

url = "https://rahulshettyacademy.com/angularpractice/"
driver.get(url)
driver.maximize_window()


driver.find_element(By.XPATH,"//input[@name='email']").send_keys("sandy@gmail.com")
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("12345")
driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
driver.find_element(By.XPATH,"//select[@class='form-control']").click()
driver.find_element(By.XPATH,"//input[@type='radio' and @value='option2']").click()
# to doctest-----------------
    #1.name is not done
    # 2.gnder drop down list selection
    #2.DOB selection
driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(3)
driver.find_element(By.LINK_TEXT, 'Shop').click()

#select balackbery and click on it
all_products_webelement = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for i in all_products_webelement:
    product_name = i.find_element(By.XPATH, "div/h4/a").text  #action chaining using base address
    if product_name == "Blackberry":
        i.find_element(By.XPATH, "div/button").click()         #action chaining using base address

#click on check out button
driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()

#click on another checkout button
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
#Handling auto sugegstive dropdown
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("IND")

#wait untill dropdown list dsiplays-use explicit wait
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))  #add one extra bracket to locator,
# as presence_of_element takes only one argument

#slect IndiA from drop down list
driver.find_element(By.LINK_TEXT, "India").click()

#select check box, wss not working so cmmented
# driver.find_element(By.XPATH,"//input[@type='checkbox']").click()

#click on Purchase button
driver.find_element(By.XPATH, "//input[@type='submit']").click()

#capure success message and validate it
success_message = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text

assert "Success! Thank you!" in success_message

time.sleep(3)
driver.close()
