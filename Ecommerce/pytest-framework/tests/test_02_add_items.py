import pytest
import time
from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup", "log_in_setup")
class TestAddItems:
    def test_02_verify_five_items(self):
        inv = InventoryPage(self.driver)
        inv.add_five_items() 
        time.sleep(1)
        
        badge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        # Positive and Negative Assertions
        assert badge == "5", f"Positive Assert Failed: Expected 5, found {badge}"
        assert badge != "0", "Negative Assert Failed: Cart is empty"
        time.sleep(1)