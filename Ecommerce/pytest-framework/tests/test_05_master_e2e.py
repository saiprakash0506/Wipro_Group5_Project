import pytest
import csv
import os
import time
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

# Helper function to read the CSV file
def get_csv_data():
    data = []
    # Assumes your CSV is in: Pytest-framework/data/test_data.csv
    path = os.path.join("data", "test_data.csv")
    if not os.path.exists(path):
        pytest.exit(f"CSV Data file not found at: {path}")
        
    with open(path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data

@pytest.mark.usefixtures("setup")
class TestMasterE2E:

    @pytest.mark.parametrize("row", get_csv_data())
    def test_master_flow(self, row):
        driver = self.driver
        inv = InventoryPage(driver)
        cart = CartPage(driver)
        chk = CheckoutPage(driver)

        # --- FIREFOX STABILITY RESET ---
        # Instead of logout, we clear session and go to login page fresh
        driver.delete_all_cookies()
        driver.get("https://www.saucedemo.com/")
        time.sleep(1) # Small pause to let Firefox settle the window context

        # 1. Login using CSV data
        # We use driver.find_element directly here for the login screen
        driver.find_element("id", "user-name").send_keys(row['username'])
        driver.find_element("id", "password").send_keys(row['password'])
        driver.find_element("id", "login-button").click()

        # 2. Add 5 items to cart
        inv.add_five_items()
        inv.go_to_cart()

        # 3. Remove the specific product mentioned in CSV 'product_to_remove' column
        product_to_del = row['product_to_remove']
        cart.remove_item_by_name(product_to_del)

        # 4. Proceed to Checkout
        cart.click_checkout()

        # 5. Fill Details from CSV
        chk.fill_details(
            row['first_name'], 
            row['last_name'], 
            row['zip_code']
        )
        
        # 6. Finish Order
        chk.finish_order()

        # 7. Assertion 
        # If this fails, conftest.py hook will automatically take a screenshot
        success_msg = chk.get_confirmation()
        assert "Thank you" in success_msg, f"Flow failed for user {row['first_name']}"

        # 8. Cleanup for next row
        # We don't click logout here because Firefox often crashes during redirect.
        # The delete_all_cookies() at the start of the next row handles the "logout".
        time.sleep(1)