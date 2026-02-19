import pytest
import time
import os
import csv
from selenium.webdriver.common.by import By

def get_csv_data():
    rows = []
    path = os.path.join("data", "invalidlogin_data.csv")
    if not os.path.exists(path): return rows
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader: rows.append(row)
    return rows

@pytest.mark.usefixtures("setup")
class TestNegativeLogin:

    def slow_type(self, element, text, delay=0.05):
        if text:
            for char in text:
                element.send_keys(char)
                time.sleep(delay)

    @pytest.mark.parametrize("u, p, expected_error", get_csv_data())
    def test_00_neg_logins(self, u, p, expected_error):
        driver, log = self.driver, self.logger

        log.info(f"--- TESTING NEGATIVE LOGIN: {u if u else '[EMPTY]'} ---")
        driver.get("https://www.saucedemo.com/")
        
        user_field = driver.find_element(By.ID, "user-name")
        pass_field = driver.find_element(By.ID, "password")
        login_btn = driver.find_element(By.ID, "login-button")

        # 1. Type
        self.slow_type(user_field, u)
        self.slow_type(pass_field, p)

        # 2. Border & Click
        driver.execute_script("arguments[0].style.border='3px solid red';", login_btn)
        time.sleep(0.5)
        login_btn.click()

        # 3. Handle Error & Manual Screenshot
        try:
            error_element = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
            actual_error = error_element.text
            log.info(f"Error caught: {actual_error}")

            # Manual screenshot for negative login
            if not os.path.exists("reports/errors"): os.makedirs("reports/errors")
            clean_name = "".join(x for x in u if x.isalnum()) if u else "empty_user"
            ss_path = f"reports/errors/login_err_{clean_name}.png"
            
            try:
                driver.save_screenshot(ss_path)
                log.info(f"Manual error screenshot saved: {ss_path}")
            except Exception as ss_err:
                log.warning(f"Could not save manual screenshot: {ss_err}")

            # Assertion
            assert expected_error.lower().replace(" ", "") in actual_error.lower().replace(" ", ""), \
                f"Expected {expected_error} but got {actual_error}"

        except Exception as e:
            log.error(f"Error message element not found for user {u}: {e}")
            raise e

        log.info(f"--- TEST PASSED FOR USER {u if u else '[EMPTY]'} ---")
        time.sleep(1)