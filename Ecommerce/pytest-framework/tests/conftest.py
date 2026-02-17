import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import csv
import os

@pytest.fixture(scope="class")
def setup(request):
    # Set Chrome Options to disable password pop-ups
    chrome_options = Options()
    
    # 1. Disable Password Manager and Leaked Password pop-ups
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    chrome_options.add_experimental_option("prefs", prefs)
    
    # 2. Disable "Automation" info bar and extension
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # FIXED: Changed 'add_use_experimental_option' to 'add_experimental_option'
    chrome_options.add_experimental_option("useAutomationExtension", False)
    
    # 3. Add Incognito mode for a fresh session
    chrome_options.add_argument("--incognito")

    # Setup Chrome with options
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture()
def log_in_setup(request):
    driver = request.cls.driver
    driver.get("https://www.saucedemo.com/")
    
    path = os.path.join("data", "test_data.csv")
    with open(path, mode='r') as file:
        reader = csv.DictReader(file)
        user_data = next(reader)
        
    driver.find_element("id", "user-name").send_keys(user_data['username'])
    driver.find_element("id", "password").send_keys(user_data['password'])
    driver.find_element("id", "login-button").click()
    yield