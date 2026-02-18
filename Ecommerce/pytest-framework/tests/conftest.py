import pytest
import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Options: chrome, edge, firefox")

@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("--browser").lower()
    
    # Logic to find the 'drivers' folder relative to this file
    current_dir = os.path.dirname(os.path.abspath(__file__)) 
    project_root = os.path.dirname(current_dir) 
    drivers_path = os.path.join(project_root, "drivers")

    driver = None

    if browser == "chrome":
        opts = webdriver.ChromeOptions()
        # Fix for "Change your password" popup
        prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
        opts.add_experimental_option("prefs", prefs)
        opts.add_argument("--disable-features=SafeBrowsingPasswordCheck")
        opts.add_argument("--incognito")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=opts)

    elif browser == "edge":
        exe_path = os.path.join(drivers_path, "msedgedriver.exe")
        if not os.path.exists(exe_path):
            pytest.exit(f"ERROR: msedgedriver.exe not found at {exe_path}")
        
        opts = webdriver.EdgeOptions()
        opts.add_argument("--inprivate")
        driver = webdriver.Edge(service=EdgeService(exe_path), options=opts)

    elif browser == "firefox":
        exe_path = os.path.join(drivers_path, "geckodriver.exe")
        if not os.path.exists(exe_path):
            pytest.exit(f"ERROR: geckodriver.exe not found at {exe_path}")
            
        opts = webdriver.FirefoxOptions()
        opts.add_argument("-private")
        
        # --- FIREFOX STABILITY FIXES (Prevents 'Browsing context discarded') ---
        opts.set_preference("browser.tabs.remote.autostart", False)
        opts.set_preference("fission.autostart", False)
        opts.set_preference("dom.disable_beforeunload", True)
        # ----------------------------------------------------------------------
        
        driver = webdriver.Firefox(service=FirefoxService(exe_path), options=opts)

    driver.maximize_window()
    driver.implicitly_wait(10)
    
    # Attach driver to the class instance
    if request.cls is not None:
        request.cls.driver = driver
    
    yield driver
    
    # Final cleanup
    time.sleep(1)
    driver.quit()

@pytest.fixture(scope="function")
def log_in_setup(request):
    """Fixture to handle standard login before specific test functions."""
    driver = request.cls.driver
    driver.get("https://www.saucedemo.com/")
    
    driver.find_element("id", "user-name").send_keys("standard_user")
    driver.find_element("id", "password").send_keys("secret_sauce")
    driver.find_element("id", "login-button").click()
    time.sleep(1) # Wait for transitions to finish

# --- Screenshot Logic: Captures and Embeds into HTML Report ---
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' and report.failed:
        # Get driver from the test class instance
        driver = getattr(item.instance, 'driver', None)
        
        if driver:
            # Ensure reports/screenshots directory exists
            os.makedirs("reports/screenshots", exist_ok=True)
            
            # Create unique filename
            timestamp = datetime.now().strftime("%H%M%S")
            file_name = f"{item.name}_{timestamp}.png"
            full_path = os.path.join("reports", "screenshots", file_name)
            
            driver.save_screenshot(full_path)
            
            # Embed image in HTML report
            if pytest_html:
                relative_path = os.path.join("screenshots", file_name)
                html = '<div><img src="%s" alt="screenshot" style="width:300px;height:200px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % relative_path
                extra.append(pytest_html.extras.html(html))
    
    report.extra = extra