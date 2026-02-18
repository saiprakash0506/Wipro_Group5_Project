from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.fname = (By.ID, "first-name")
        self.lname = (By.ID, "last-name")
        self.zip = (By.ID, "postal-code")
        self.cont_btn = (By.ID, "continue")
        self.finish_btn = (By.ID, "finish")
        self.msg = (By.CLASS_NAME, "complete-header")

    def fill_details(self, f, l, z):
        self.type(self.fname, f)
        self.type(self.lname, l)
        self.type(self.zip, z)
        self.click(self.cont_btn)

    def finish_order(self):
        self.click(self.finish_btn)

    def get_confirmation(self):
        return self.driver.find_element(*self.msg).text
    
    # Ensures both get_message and get_confirmation work
    def get_message(self):
        return self.get_confirmation()