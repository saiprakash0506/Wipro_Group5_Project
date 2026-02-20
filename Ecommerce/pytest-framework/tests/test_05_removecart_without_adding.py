import pytest
import time
import os
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class TestRemoveWithoutAdding:

    def slow_type(self, element, text, delay=0.05):
        if text:
            for char in text:
                element.send_keys(char)
                time.sleep(delay)

    def test_05_remove_without_adding(self):

        driver, log = self.driver, self.logger

        log.info("--- STARTING NEGATIVE TEST: REMOVE WITHOUT ADDING ---")

        driver.get("https://www.saucedemo.com/")

        # 1️⃣ LOGIN
        self.slow_type(driver.find_element(By.ID, "user-name"), "standard_user")
        self.slow_type(driver.find_element(By.ID, "password"), "secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

        # 2️⃣ GO TO CART WITHOUT ADDING ANY ITEM
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(2)

        log.info("Trying to remove product without adding...")

        # 3️⃣ TRY REMOVE (THIS SHOULD FAIL)
        try:
            remove_btn = driver.find_element(By.ID, "remove-sauce-labs-backpack")
            remove_btn.click()

            log.error("Remove button found without adding product!")

            # ❌ INTENTIONAL FAILURE
            assert False, "Remove button should not exist without adding product."

        except Exception as e:

            log.info("Expected failure occurred. Item was never added.")

            # 🔥 SAME LOGIC AS NEG LOGIN TEST
            current_run = os.environ.get("CURRENT_RUN_DIR", "reports")
            error_dir = os.path.join(current_run, "errors")

            os.makedirs(error_dir, exist_ok=True)

            ss_path = os.path.join(error_dir, "remove_without_adding.png")

            try:
                driver.save_screenshot(ss_path)
                log.info(f"Manual error screenshot saved: {ss_path}")
            except Exception as ss_err:
                log.warning(f"Could not save screenshot: {ss_err}")

            pytest.fail("Remove attempted without adding product — Expected Failure.")

        time.sleep(1)