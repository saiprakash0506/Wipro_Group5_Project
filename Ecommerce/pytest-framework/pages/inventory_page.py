import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage(BasePage):
    ADD_BUTTONS = (By.XPATH, "//button[text()='Add to cart']")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def add_five_items(self):
        buttons = self.driver.find_elements(*self.ADD_BUTTONS)
        for i in range(5):
            self.smooth_scroll(buttons[i])
            buttons[i].click()
            time.sleep(0.8)

    def go_to_cart(self):
        self.do_click(self.CART_ICON)

    def logout(self):
        self.do_click(self.BURGER_MENU)
        logout_btn = self.wait.until(EC.element_to_be_clickable(self.LOGOUT_LINK))
        time.sleep(1)
        logout_btn.click()