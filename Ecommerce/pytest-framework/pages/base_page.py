import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

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

    def get_element_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.smooth_scroll(element)
        return element.text

    def smooth_scroll(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", 
            element
        )
        time.sleep(0.8)