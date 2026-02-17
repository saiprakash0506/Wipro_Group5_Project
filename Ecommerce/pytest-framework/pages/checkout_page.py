import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")
    SUCCESS_MSG = (By.CLASS_NAME, "complete-header")
    BACK_HOME_BTN = (By.ID, "back-to-products")

    def fill_checkout_info(self, fname, lname, zip_code):
        self.do_send_keys(self.FIRST_NAME, fname)
        self.do_send_keys(self.LAST_NAME, lname)
        self.do_send_keys(self.POSTAL_CODE, zip_code)
        self.do_click(self.CONTINUE_BTN)

    def finish_checkout(self):
        self.slow_scroll_detailed() # Showing prices and tax
        finish_element = self.driver.find_element(*self.FINISH_BTN)
        self.smooth_scroll(finish_element)
        time.sleep(1)
        finish_element.click()

    def get_success_message(self):
        return self.get_element_text(self.SUCCESS_MSG)

    def click_back_home(self):
        self.do_click(self.BACK_HOME_BTN)