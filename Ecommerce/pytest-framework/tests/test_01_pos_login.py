import pytest
import time
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class TestPositiveLogin:
    def test_01_login_success(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(1)
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        
        # Positive Assertion
        assert "inventory.html" in driver.current_url, "Login Successful assertion failed"
        time.sleep(1)