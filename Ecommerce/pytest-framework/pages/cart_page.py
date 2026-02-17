import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    CHECKOUT_BTN = (By.ID, "checkout")
    
    def remove_item_by_name(self, product_name):
        # Finds the specific 'Remove' button based on product name
        formatted_name = product_name.lower().replace(" ", "-")
        remove_btn_locator = (By.ID, f"remove-{formatted_name}")
        self.do_click(remove_btn_locator)
        time.sleep(1.5)

    def click_checkout(self):
        self.do_click(self.CHECKOUT_BTN)