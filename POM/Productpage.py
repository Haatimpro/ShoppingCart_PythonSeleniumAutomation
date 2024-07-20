from selenium.webdriver.common.by import By


class Product:

    Allproducts = (By.XPATH, "//div[@class='card h-100']")
    Each_Product = (By.XPATH, "div/h4/a")
    Compare_Product = (By.XPATH, "div/button")
    Checkout_Button = (By.XPATH, "//a[@class='nav-link btn btn-primary']")

    def __init__(self,driver):
        self.driver = driver

    def allproducts(self):
        # select balackbery and click on it
        #self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        return self.driver.find_elements(*Product.Allproducts)

    def each_product(self, i):  #pass i here as we are using inside the method
        # product_name = i.find_element(By.XPATH, "div/h4/a").text  #action chaining using base address
        return i.find_element(*Product.Each_Product).text

    def compare_product(self,i):   #pass i here as we are using inside the method
        #i.find_element(By.XPATH, "div/button").click()
        return i.find_element(*Product.Compare_Product).click()

    def checkout_button(self):
        #self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
        self.driver.find_element(*Product.Checkout_Button).click()




