import pytest
import time
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class TestPositiveLogin:

    def slow_type(self, element, text, delay=0.1):
        """Helper function to type text character by character."""
        for character in text:
            element.send_keys(character)
            time.sleep(delay)

    def test_01_login_success(self):
        driver = self.driver
        log = self.logger # This now points to reports/logs/test_01_login_success.log

        log.info("--- STARTING TEST CASE: Positive Login Success ---")
        
        # Step 1: Navigate
        log.info("Navigating to SauceDemo homepage")
        driver.get("https://www.saucedemo.com/")
        time.sleep(1.5) 

        # Locate Elements
        user_field = driver.find_element(By.ID, "user-name")
        pass_field = driver.find_element(By.ID, "password")
        login_btn = driver.find_element(By.ID, "login-button")

        # Step 2: Username with Animation
        log.info("Entering username character by character...")
        self.slow_type(user_field, "standard_user")
        
        # Positive Assertion
        assert user_field.get_attribute("value") == "standard_user", "Positive Assert Failed: Username field mismatch"
        log.info("POSITIVE ASSERT: Username field verified correctly.")
        time.sleep(0.8)

        # Step 3: Password with Animation
        log.info("Entering password character by character...")
        self.slow_type(pass_field, "secret_sauce")
        
        # Positive Assertion
        assert pass_field.get_attribute("value") == "secret_sauce", "Positive Assert Failed: Password field mismatch"
        log.info("POSITIVE ASSERT: Password field verified correctly.")
        time.sleep(0.8)

        # Step 4: Click Login
        log.info("Clicking the login button...")
        login_btn.click()
        time.sleep(1.5)

        # Step 5: Final Validation Assertion
        current_url = driver.current_url
        log.info(f"Login complete. Current URL is: {current_url}")
        
        assert "inventory.html" in current_url, f"Login Failed! Redirected to wrong URL: {current_url}"
        log.info("SUCCESS ASSERT: Redirected to Inventory page successfully.")
        
        log.info("--- TEST CASE COMPLETED PASSED ---")
        time.sleep(1)