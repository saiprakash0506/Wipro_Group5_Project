import pytest
import time
from selenium.webdriver.common.by import By
from pages.inventory_page import InventoryPage

@pytest.mark.usefixtures("setup")
class TestRemoveContent:
    def slow_type(self, element, text):
        for char in text:
            element.send_keys(char)
            time.sleep(0.05)

    def apply_border(self, driver, element):
        driver.execute_script("arguments[0].style.border='3px solid red';", element)
        time.sleep(0.3)

    def test_03_remove_item(self):
        driver = self.driver
        log = self.logger
        inv = InventoryPage(driver)

        log.info("--- STARTING TEST CASE: Remove Item Flow ---")
        
        # --- STEP 1: LOGIN FIRST ---
        driver.get("https://www.saucedemo.com/")
        self.slow_type(driver.find_element(By.ID, "user-name"), "standard_user")
        self.slow_type(driver.find_element(By.ID, "password"), "secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # --- STEP 2: ADD 5 ITEMS ---
        for i in range(5):
            items = driver.find_elements(By.CLASS_NAME, "inventory_item")
            item_btn = items[i].find_element(By.CSS_SELECTOR, ".btn_inventory")
            
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", items[i])
            time.sleep(0.6)
            self.apply_border(driver, item_btn)
            item_btn.click()
            log.info(f"Added item {i+1}")

        # --- STEP 3: GO TO CART & REMOVE ---
        inv.go_to_cart()
        time.sleep(1)
        
        log.info("Locating Sauce Labs Backpack for removal...")
        backpack_remove_btn = driver.find_element(By.ID, "remove-sauce-labs-backpack")
        
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", backpack_remove_btn)
        self.apply_border(driver, backpack_remove_btn)
        backpack_remove_btn.click()
        
        # --- STEP 4: VERIFY ---
        final_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert final_badge == "4"
        log.info("POSITIVE ASSERT: Count is exactly 4.")