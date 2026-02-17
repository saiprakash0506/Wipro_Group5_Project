import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def do_click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.smooth_scroll(element)
        time.sleep(0.5)
        element.click()

    def do_send_keys(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.smooth_scroll(element)
        element.clear()
        element.send_keys(text)
        time.sleep(0.5)

    def get_element_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.smooth_scroll(element)
        return element.text

    def smooth_scroll(self, element):
        """Standard smooth scroll to center an element."""
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", 
            element
        )
        time.sleep(1.2) 

    def slow_scroll_detailed(self):
        """Specially designed slow scroll for the price/summary page."""
        # Scrolls from top to bottom slowly to show price/tax
        for i in range(0, 500, 5):
            self.driver.execute_script(f"window.scrollTo(0, {i});")
            time.sleep(0.02)
        time.sleep(2) # Hold at the bottom to see the price