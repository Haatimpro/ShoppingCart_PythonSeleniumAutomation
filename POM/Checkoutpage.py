from selenium.webdriver.common.by import By


class Checkoutpage:

    Checkout_Button = (By.XPATH, "//button[@class='btn btn-success']")

    def __init__(self,driver):
        self.driver = driver

    def checkout_button(self):
        #self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        self.driver.find_element(*Checkoutpage.Checkout_Button).click()