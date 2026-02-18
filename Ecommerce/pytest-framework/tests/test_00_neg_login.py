import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class TestNegativeLogin:
    @pytest.mark.parametrize("u, p, error", [
        ("locked_out_user", "secret_sauce", "Sorry, this user has been locked out"),
        ("standard_user", "", "Password is required"),
        ("invalid", "invalid", "Username and password do not match")
    ])
    def test_00_neg_logins(self, u, p, error):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID, "user-name").send_keys(u)
        self.driver.find_element(By.ID, "password").send_keys(p)
        self.driver.find_element(By.ID, "login-button").click()
        err_msg = self.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
        assert error in err_msg