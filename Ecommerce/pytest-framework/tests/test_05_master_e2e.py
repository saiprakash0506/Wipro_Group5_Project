import pytest
import csv
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_csv_data():
    path = os.path.join("data", "test_data.csv")
    with open(path, mode='r', encoding='utf-8') as f:
        return list(csv.DictReader(f))

@pytest.mark.usefixtures("setup")
class TestMasterE2E:
    def slow_type(self, element, text):
        if text:
            for char in text:
                element.send_keys(char); time.sleep(0.06)

    def apply_border(self, driver, element):
        driver.execute_script("arguments[0].style.border='3px solid red';", element)
        time.sleep(0.3)

    def apply_shadow(self, driver, element):
        driver.execute_script("arguments[0].style.boxShadow = '0 0 20px 5px rgba(0, 230, 118, 0.8)';", element)
        time.sleep(0.5)

    def smooth_scroll(self, driver, element):
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        time.sleep(0.6)

    @pytest.mark.parametrize("row", get_csv_data())
    def test_master_flow(self, row):
        driver, log = self.driver, self.logger
        wait = WebDriverWait(driver, 15)

        log.info(f"--- STARTING: User {row['first_name'] or 'EmptyName'} ---")
        driver.get("https://www.saucedemo.com/")

        # 1. Login
        self.slow_type(driver.find_element(By.ID, "user-name"), row['username'])
        self.slow_type(driver.find_element(By.ID, "password"), row['password'])
        driver.find_element(By.ID, "login-button").click()

        # 2. Add 5 Items
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))
        for i in range(5):
            items = driver.find_elements(By.CLASS_NAME, "inventory_item")
            btn = items[i].find_element(By.CSS_SELECTOR, ".btn_inventory")
            self.smooth_scroll(driver, items[i]); self.apply_border(driver, btn); btn.click()

        # 3. Cart & Removal
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        try:
            xpath = f"//div[text()='{row['product_to_remove']}']/ancestor::div[@class='cart_item']//button"
            rem_btn = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            self.smooth_scroll(driver, rem_btn); self.apply_border(driver, rem_btn); rem_btn.click()
        except: log.warning("Removal item not found.")

        # 4. Checkout
        driver.find_element(By.ID, "checkout").click()
        self.slow_type(driver.find_element(By.ID, "first-name"), row['first_name'])
        self.slow_type(driver.find_element(By.ID, "last-name"), row['last_name'])
        self.slow_type(driver.find_element(By.ID, "postal-code"), row['zip_code'])
        
        cont_btn = driver.find_element(By.ID, "continue")
        self.apply_border(driver, cont_btn); cont_btn.click()

        # --- DYNAMIC ERROR CHECKING ---
        errors = driver.find_elements(By.CSS_SELECTOR, "h3[data-test='error']")
        if len(errors) > 0:
            error_msg = errors[0].text
            log.error(f"DYNAMIC ERROR: {error_msg}")
            
            # Save Screenshot to specialized folder
            if not os.path.exists("reports/errors"): os.makedirs("reports/errors")
            ss_name = f"reports/errors/checkout_fail_{row['first_name'] or 'missing'}_{int(time.time())}.png"
            driver.save_screenshot(ss_name)
            
            log.info("Terminating current row and moving to next...")
            return  # This exits THIS row iteration and triggers the NEXT row in the CSV

        # 5. Finalize (Only reached if no errors)
        finish_btn = wait.until(EC.element_to_be_clickable((By.ID, "finish")))
        self.smooth_scroll(driver, finish_btn); self.apply_border(driver, finish_btn); finish_btn.click()
        
        # 6. Back Home (2s Gap)
        time.sleep(2)
        back_btn = wait.until(EC.element_to_be_clickable((By.ID, "back-to-products")))
        self.apply_border(driver, back_btn); back_btn.click()

        # 7. Logout (Neon Shadow)
        driver.execute_script("window.scrollTo(0, 0);")
        burger = wait.until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn")))
        self.apply_shadow(driver, burger); burger.click()
        
        logout = wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
        self.apply_shadow(driver, logout); logout.click()
        log.info(f"Successfully completed flow for {row['first_name']}")