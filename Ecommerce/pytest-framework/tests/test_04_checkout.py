import pytest
import time
from selenium.webdriver.common.by import By
from pages.inventory_page import InventoryPage

@pytest.mark.usefixtures("setup")
class TestCheckoutRandom:
    def slow_type(self, element, text):
        for char in text:
            element.send_keys(char)
            time.sleep(0.05)

    def test_04_verify_random_checkout(self):
        driver = self.driver
        log = self.logger
        inv = InventoryPage(driver)

        log.info("--- STARTING TEST CASE: Full Checkout ---")

        # --- STEP 1: LOGIN ---
        driver.get("https://www.saucedemo.com/")
        self.slow_type(driver.find_element(By.ID, "user-name"), "standard_user")
        self.slow_type(driver.find_element(By.ID, "password"), "secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # --- STEP 2: ADD ITEMS ---
        log.info("Adding items to the cart...")
        for i in range(3): # Adding 3 items for this specific test
            items = driver.find_elements(By.CLASS_NAME, "inventory_item")
            items[i].find_element(By.CSS_SELECTOR, ".btn_inventory").click()
        
        # --- STEP 3: CHECKOUT ---
        inv.go_to_cart()
        driver.find_element(By.ID, "checkout").click()
        
        log.info("Entering Random Details...")
        self.slow_type(driver.find_element(By.ID, "first-name"), "John")
        self.slow_type(driver.find_element(By.ID, "last-name"), "Doe")
        self.slow_type(driver.find_element(By.ID, "postal-code"), "90210")
        
        driver.find_element(By.ID, "continue").click()
        
        # Finish
        finish_btn = driver.find_element(By.ID, "finish")
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", finish_btn)
        finish_btn.click()

        # Verify
        success_text = driver.find_element(By.CLASS_NAME, "complete-header").text
        assert "Thank you" in success_text
        log.info("Full checkout verified successfully.")