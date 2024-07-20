import time

from selenium import webdriver
#import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest

from POM.Checkoutpage import Checkoutpage
from POM.Confirmationpage import Confirmationpage
from POM.Homepage import Homepage
from POM.Productpage import Product
from UTILITIES.baseclass import BaseClass


# @pytest.mark.usefixtures("setup")
class TestApp(BaseClass):
    def test_End2End(self):
        Home_object = Homepage(self.driver)
        Home_object.email()
        Home_object.password()
        Home_object.checkbox()
        Home_object.gender_dropdown()
        Home_object.employementstatus_radiobutton()
        Home_object.submit_button()
        time.sleep(3)
        Home_object.shop_link()

        #product page
        #select balackbery and click on it
        #all_products_webelement = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        Product_Object = Product(self.driver)
        all_products_webelement  = Product_Object.allproducts()

        for i in all_products_webelement:
            #product_name = i.find_element(By.XPATH, "div/h4/a").text  #action chaining using base address
            product_name = Product_Object.each_product(i)  #pass i as we use it inside the method
            if product_name == "Blackberry":
                #i.find_element(By.XPATH, "div/button").click()         #action chaining using base address
                Product_Object.compare_product(i)  #pass i as we use it inside the method

        #click on checkout button
        #self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
        Product_Object.checkout_button()

        #checkout page, clcik on check out button
        #self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        Checkoutpage_Object = Checkoutpage(self.driver)
        Checkoutpage_Object.checkout_button()

        #confirmation page
        Confirmationpage_Object = Confirmationpage(self.driver)
        #Handling auto sugegstive dropdown
        Confirmationpage_Object.location_textbox()
        #wait untill dropdown list dsiplays-use explicit wait
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((Confirmationpage_Object.Country_Dropdownlist)))  #add one extra bracket to locator,
        # as presence_of_element takes only one argument
        #slect IndiA from drop down list
        Confirmationpage_Object.country_dropdownlist()
        #select check box, wss not working so cmmented
        # driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
        #click on Purchase button
        # Confirmationpage_Object.purchase_button()
        #capure success message and validate it
        success_message = Confirmationpage_Object.sucessfull_message()
        assert "Success! Thank you!" in success_message

        time.sleep(3)
        # driver.close()
