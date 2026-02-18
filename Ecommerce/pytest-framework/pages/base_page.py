import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.slow_delay = 0.6 

    def highlight(self, element, color="red"):
        self.driver.execute_script(f"arguments[0].style.border='3px solid {color}'", element)

    def click(self, locator):
        el = self.wait.until(EC.element_to_be_clickable(locator))
        self.highlight(el, "red")
        time.sleep(self.slow_delay)
        el.click()

    def type(self, locator, text):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        self.highlight(el, "blue")
        el.clear()
        time.sleep(self.slow_delay)
        el.send_keys(text)


    def smooth_scroll(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        time.sleep(0.5)