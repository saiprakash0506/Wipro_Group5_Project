import pytest
import time
import csv
import os
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def get_csv_data():
    data = []
    path = os.path.join("data", "test_data.csv")
    with open(path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

@pytest.mark.usefixtures("setup")
class TestEcommerceE2E:

    @pytest.mark.parametrize("test_info", get_csv_data())
    def test_full_scenario_csv(self, test_info):
        self.loginPage = LoginPage(self.driver)
        self.inventoryPage = InventoryPage(self.driver)
        self.cartPage = CartPage(self.driver)
        self.checkoutPage = CheckoutPage(self.driver)
        
        # 1. Login using CSV credentials
        self.loginPage.login(test_info['username'], test_info['password'])
        time.sleep(2)
        
        # 2. Add 4 items
        self.inventoryPage.add_four_items()
        
        # 3. Go to cart and remove 1 item
        self.inventoryPage.go_to_cart()
        product_to_del = test_info['product_to_remove']
        self.cartPage.remove_item_by_name(product_to_del)
        
        # 4. Checkout
        self.cartPage.click_checkout()
        self.checkoutPage.fill_checkout_info(
            test_info['first_name'], 
            test_info['last_name'], 
            test_info['zip_code']
        )
        self.checkoutPage.finish_checkout()
        
        # 5. Home and Logout
        assert "Thank you" in self.checkoutPage.get_success_message()
        self.checkoutPage.click_back_home()
        self.inventoryPage.logout()
        
        assert "inventory.html" not in self.driver.current_url