import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup", "log_in_setup")
class TestCheckoutRandom:
    def test_04_verify_random_checkout(self):
        inv = InventoryPage(self.driver)
        cart = CartPage(self.driver)
        check = CheckoutPage(self.driver)

        # 1. Add items
        inv.add_five_items()
        inv.go_to_cart()

        # 2. Scroll and Remove one item manually to test scrolling
        rem_btn = self.driver.find_element(By.XPATH, "(//button[text()='Remove'])[1]")
        inv.smooth_scroll(rem_btn) # This now works because it's in BasePage
        rem_btn.click()

        # 3. Proceed to checkout
        cart.click_checkout()

        # 4. Fill details and finish
        check.fill_details("QA", "Engineer", "560001")
        check.finish_order()

        # 5. Assertion
        assert "Thank you" in check.get_confirmation()