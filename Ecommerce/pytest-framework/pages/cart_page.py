from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.checkout_btn = (By.ID, "checkout")

    def remove_item_by_name(self, item_name):
        xpath = f"//div[text()='{item_name}']/ancestor::div[@class='cart_item']//button"
        self.click((By.XPATH, xpath))

    def click_checkout(self):
        self.click(self.checkout_btn)