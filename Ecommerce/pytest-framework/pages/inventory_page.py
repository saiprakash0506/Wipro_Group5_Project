import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage(BasePage):
    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    ADD_BUTTONS = (By.XPATH, "//button[text()='Add to cart']")

    def add_four_items(self):
        buttons = self.driver.find_elements(*self.ADD_BUTTONS)
        for i in range(4): # Loop exactly 4 times
            buttons[i].click()
            time.sleep(1) 

    def go_to_cart(self):
        self.do_click(self.CART_ICON)
        time.sleep(2)

    def logout(self):
        self.do_click(self.BURGER_MENU)
        logout_btn = self.wait.until(EC.visibility_of_element_located(self.LOGOUT_LINK))
        time.sleep(2) 
        self.driver.execute_script("arguments[0].click();", logout_btn)