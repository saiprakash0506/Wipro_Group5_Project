import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    CART_ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BTN = (By.ID, "checkout")
    
    # Ensure this name matches the test call exactly
    def remove_item_by_name(self, product_name):
        # SauceDemo IDs for remove buttons are usually 'remove-product-name'
        formatted_name = product_name.lower().replace(" ", "-")
        remove_btn_locator = (By.ID, f"remove-{formatted_name}")
        self.do_click(remove_btn_locator)
        time.sleep(2) # Pause to see the item disappear from the cart

    def click_checkout(self):
        self.do_click(self.CHECKOUT_BTN)
        time.sleep(2)

    def is_item_in_cart(self, product_name):
        items = self.driver.find_elements(*self.CART_ITEM_NAMES)
        return any(item.text == product_name for item in items)