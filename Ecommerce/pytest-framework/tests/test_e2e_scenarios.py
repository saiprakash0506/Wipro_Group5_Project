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

    @pytest.mark.parametrize("test_info", get_csv_data())
    @pytest.mark.usefixtures("log_in_setup")
    def test_visual_e2e_flow(self, test_info):
        self.inventoryPage = InventoryPage(self.driver)
        self.cartPage = CartPage(self.driver)
        self.checkoutPage = CheckoutPage(self.driver)

        # Step 1: Add 5 items
        self.inventoryPage.add_five_items()
        self.inventoryPage.go_to_cart()

        # Step 2: Remove specific item
        product_to_del = test_info['product_to_remove']
        self.cartPage.remove_item_by_name(product_to_del)

        # Step 3: Checkout with slow summary scroll
        self.cartPage.click_checkout()
        self.checkoutPage.fill_checkout_info(
            test_info['first_name'], 
            test_info['last_name'], 
            test_info['zip_code']
        )
        self.checkoutPage.finish_checkout()

        # Step 4: Verify and Logout
        assert "Thank you" in self.checkoutPage.get_success_message()
        self.checkoutPage.click_back_home()
        self.inventoryPage.logout()