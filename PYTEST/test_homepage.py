import time

import pytest
from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from POM.Submissionfrom import SubmitForm
from TestData.HomePageTestData import HomePageTestData
from UTILITIES.baseclass import BaseClass
class TestHomePage(BaseClass):
    def test_submissionform(self,getTestData):
        log = self.getLogger()
        #fill the form
        #creating object for SubmitForm class
        homeformobj = SubmitForm(self.driver)
        log.info("entering Email Address")
        # self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("sandy@gmail.com")
        homeformobj.getEmail().send_keys(getTestData["email"])
        log.info("entering password")
        # self.driver.find_element(By.XPATH,"//input[@type='password']").send_keys("sandy123")
        homeformobj.getPassword().send_keys(getTestData["password"])
        log.info("Clicking on checkbox")
        # self.driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
        homeformobj.getCheckbox().click()
        log.info("Click on radio button")
        #self.driver.find_element(By.XPATH,"//input[@type='radio' and @value='option2']").click()
        homeformobj.getRadioButton().click()
        log.info("Click on Submit button")
        #self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        homeformobj.getSubmitButton().click()
        log.info("Validating the success message")
        # SuccessMessage = self.driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text
        SuccessMessage = homeformobj.getSuccessMessage().text
        assert 'success' in SuccessMessage
        log.info(f"Success message is,{SuccessMessage}")
        time.sleep(3)
        self.driver.refresh()

    @pytest.fixture(params= HomePageTestData.getTestData("testcase2"))
    def getTestData(self,request):
        return request.param
