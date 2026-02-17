import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@pytest.fixture(scope="class")
def setup(request):
    chrome_options = Options()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_argument("--incognito")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture()
def log_in_setup(request):
    driver = request.cls.driver
    driver.get("https://www.saucedemo.com/")
    
    # We pull the login details directly from the current test row
    current_row = request.node.callspec.params.get("test_info")
    
    driver.find_element(By.ID, "user-name").send_keys(current_row['username'])
    time.sleep(0.5)
    driver.find_element(By.ID, "password").send_keys(current_row['password'])
    time.sleep(0.5)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(1.5)