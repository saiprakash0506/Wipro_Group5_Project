from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.add_btns = (By.XPATH, "//button[text()='Add to cart']")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")
        self.menu_btn = (By.ID, "react-burger-menu-btn")

    def add_five_items(self):
        buttons = self.driver.find_elements(*self.add_btns)
        for i in range(min(5, len(buttons))):
            buttons[i].click()

    def go_to_cart(self):
        self.click(self.cart_icon)

    def logout(self):
        self.click(self.menu_btn)
        self.click((By.ID, "logout_sidebar_link"))