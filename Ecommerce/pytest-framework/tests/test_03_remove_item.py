import pytest
import time
from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup", "log_in_setup")
class TestRemoveContent:
    def test_03_verify_and_remove(self):
        driver = self.driver
        inv = InventoryPage(driver)
        
        # Content Verification
        names = [el.text for el in driver.find_elements(By.CLASS_NAME, "inventory_item_name")]
        assert "Sauce Labs Backpack" in names, "Backpack (Batch Item) not found"
        
        inv.add_five_items()
        inv.go_to_cart()
        time.sleep(1)
        
        # Removal logic
        driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
        time.sleep(1)
        
        badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert badge == "4", f"Removal failed. Count is {badge}"