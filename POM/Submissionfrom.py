from selenium.webdriver.common.by import By


class SubmitForm:

    email = By.XPATH, "//input[@name='email']"
    password = By.XPATH,"//input[@type='password']"
    checkbox =By.XPATH,"//input[@type='checkbox']"
    radiobutton =By.XPATH, "//input[@type='radio' and @value='option2']"
    submitbutton =By.XPATH, "//input[@type='submit']"
    successmessage = By.XPATH, "//div[@class='alert alert-success alert-dismissible']"

    def __init__(self,driver):
        self.driver = driver

    def getEmail(self):
        #self.driver.find_element(By.XPATH, "//input[@name='email']")
        return self.driver.find_element(*SubmitForm.email)


    def getPassword(self):
        #self.driver.find_element(By.XPATH,"//input[@type='password']")
        return self.driver.find_element(*SubmitForm.password)

    def getCheckbox(self):
        #self.driver.find_element(By.XPATH,"//input[@type='checkbox']")
        return self.driver.find_element(*SubmitForm.checkbox)

    def getRadioButton(self):
        #self.driver.find_element(By.XPATH, "//input[@type='radio' and @value='option2']")
        return self.driver.find_element(*SubmitForm.radiobutton)

    def getSubmitButton(self):
        #self.driver.find_element(By.XPATH, "//input[@type='submit']")
        return self.driver.find_element(*SubmitForm.submitbutton)

    def getSuccessMessage(self):
        #self.driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']")
        return self.driver.find_element(*SubmitForm.successmessage)








#checking git push