from selenium.webdriver.common.by import By


class Confirmationpage:

    Location_Textbox = (By.XPATH, "//input[@type='text']")
    Country_Dropdownlist = (By.LINK_TEXT, "India")
    Purchase_Button = (By.XPATH, "//input[@type='submit']")
    Sucessfull_Message= (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
    (By.LINK_TEXT, "India")

    def __init__(self,driver):
        self.driver = driver

    def location_textbox(self):
        #self.driver.find_element(By.XPATH, "//input[@type='text']").send_keys("IND")
        self.driver.find_element(*Confirmationpage.Location_Textbox).send_keys("IND")

    def country_dropdownlist(self):
        #self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(*Confirmationpage.Country_Dropdownlist).click()

    def purchase_button(self):
        #self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        self.driver.find_element(*Confirmationpage.Purchase_Button).click()

    def sucessfull_message(self):
        #self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
        self.driver.find_element(*Confirmationpage.Sucessfull_Message).text