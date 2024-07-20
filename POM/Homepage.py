from selenium.webdriver.common.by import By
from UTILITIES.baseclass import BaseClass


class Homepage(BaseClass):

    Email = (By.XPATH, "//input[@name='email']")
    Password = (By.XPATH,"//input[@type='password']")
    Checkbox = (By.XPATH,"//input[@type='checkbox']")
    Gender_Dropdown = (By.XPATH, "//select[@class='form-control']")
    Employementstatus_Radiobutton = (By.XPATH,"//input[@type='radio' and @value='option2']")
    Submit_Button = (By.XPATH, "//input[@type='submit']")
    Shop_Link = (By.LINK_TEXT, 'Shop')

    def __init__(self,driver):
        self.driver = driver
    def email(self):
        #self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("sandy@gmail.com")
        self.driver.find_element(*Homepage.Email).send_keys("sandy@gmail.com")
    def password(self):
        #self.driver.find_element(By.XPATH,"//input[@type='password']").send_keys("12345")
        self.driver.find_element(*Homepage.Password).send_keys("12345")
    def checkbox(self):
        #self.driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
        self.driver.find_element(*Homepage.Checkbox).click()
    def gender_dropdown(self):
        #self.driver.find_element(By.XPATH, "//select[@class='form-control']").click()
        self.driver.find_element(*Homepage.Gender_Dropdown).click()
    def employementstatus_radiobutton(self):
        #self.driver.find_element(By.XPATH,"//input[@type='radio' and @value='option2']").click()
        self.driver.find_element(*Homepage.Employementstatus_Radiobutton).click()
    def submit_button(self):
        #self.driver.find_element(By.XPATH,"//input[@type='submit']").click()
        self.driver.find_element(*Homepage.Submit_Button).click()
    def shop_link(self):
        #self.driver.find_element(By.LINK_TEXT, 'Shop').click()
        return self.driver.find_element(*Homepage.Shop_Link).click()

