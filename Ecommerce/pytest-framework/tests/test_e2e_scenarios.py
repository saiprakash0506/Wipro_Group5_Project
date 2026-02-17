import pytest
import csv
import os
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

    @pytest.mark.parametrize("test_info", get_csv_data(), ids=[f"Scenario_{i+1}" for i in range(len(get_csv_data()))])
    @pytest.mark.usefixtures("log_in_setup")
    def test_visual_e2e_flow(self, test_info):
        print(f"\nRunning test for customer: {test_info['first_name']}")
        
        self.inventoryPage = InventoryPage(self.driver)
        self.cartPage = CartPage(self.driver)
        self.checkoutPage = CheckoutPage(self.driver)

        # 1. Add 5 items
        self.inventoryPage.add_five_items()
        self.inventoryPage.go_to_cart()

        # 2. Remove 1 item (Dynamic based on CSV)
        product_to_del = test_info['product_to_remove']
        self.cartPage.remove_item_by_name(product_to_del)

        # 3. Checkout (Dynamic based on CSV)
        self.cartPage.click_checkout()
        self.checkoutPage.fill_checkout_info(
            test_info['first_name'], 
            test_info['last_name'], 
            test_info['zip_code']
        )
        self.checkoutPage.finish_checkout()

        # 4. Success Verification & Logout
        assert "Thank you" in self.checkoutPage.get_success_message()
        self.checkoutPage.click_back_home()
        self.inventoryPage.logout()