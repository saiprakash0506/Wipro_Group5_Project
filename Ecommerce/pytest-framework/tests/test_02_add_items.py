import pytest
import time
from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup") # Note: Removed log_in_setup to show the smooth login inside the test
class TestAddItems:

    def slow_type(self, element, text, delay=0.1):
        """Helper to type characters one by one."""
        for char in text:
            element.send_keys(char)
            time.sleep(delay)

    def apply_border(self, driver, element):
        """Applies a 2px red border to an element."""
        driver.execute_script("arguments[0].style.border='2px solid red';", element)
        time.sleep(0.5)

    def test_02_add_items(self):
        driver = self.driver
        log = self.logger
        inv = InventoryPage(driver)

        # --- STEP 1: SMOOTH LOGIN ---
        log.info("Navigating to site for smooth login...")
        driver.get("https://www.saucedemo.com/")
        
        user_input = driver.find_element(By.ID, "user-name")
        pass_input = driver.find_element(By.ID, "password")
        login_btn = driver.find_element(By.ID, "login-button")

        log.info("Entering username smoothly...")
        self.slow_type(user_input, "standard_user")
        
        log.info("Entering password smoothly...")
        self.slow_type(pass_input, "secret_sauce")
        
        time.sleep(0.5)
        login_btn.click()
        log.info("Login clicked.")

        # --- STEP 2: ADD 5 ITEMS WITH SCROLL & BORDER ---
        log.info("--- STARTING: Item Addition with Borders ---")
        
        # We find the inventory items to iterate through them
        for i in range(5):
            # Re-locate items to avoid stale element exceptions
            items = driver.find_elements(By.CLASS_NAME, "inventory_item")
            item_name = items[i].find_element(By.CLASS_NAME, "inventory_item_name").text
            add_button = items[i].find_element(By.CSS_SELECTOR, ".btn_inventory")

            # 1. Smoothly scroll to the item
            log.info(f"Scrolling to item {i+1}: {item_name}")
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", items[i])
            time.sleep(1.0) 

            # 2. Apply red border ONLY to the Add to Cart button
            log.info(f"Highlighting button for: {item_name}")
            self.apply_border(driver, add_button)

            # 3. Click the button
            add_button.click()
            log.info(f"Added {item_name} to cart.")
            
            # Brief pause to see the action
            time.sleep(0.5)

        # --- STEP 3: ASSERTIONS ---
        # Scroll back to top to see the badge clearly
        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", cart_badge)
        time.sleep(1)

        badge_text = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        log.info(f"Cart badge value found: {badge_text}")

        # Positive Assertion
        assert badge_text == "5", f"Expected 5, found {badge_text}"
        log.info("POSITIVE ASSERT: Badge correctly shows 5.")

        # Negative Assertion
        assert badge_text != "0", "Negative Assert Failed: Cart is empty"
        log.info("NEGATIVE ASSERT: Cart is not empty.")

        log.info("--- TEST CASE COMPLETED PASSED ---")
        time.sleep(2)