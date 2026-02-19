import pytest
import os
import logging
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager

def pytest_addoption(parser):
    """Allows passing --browser from the command line."""
    parser.addoption("--browser", action="store", default="chrome", help="chrome, firefox, or edge")

@pytest.fixture(scope="function")
def setup(request):
    """
    Initializes the driver in Incognito/Private mode with a fixed resolution.
    Sets up a unique logger for every single test case/CSV row.
    """
    browser_name = request.config.getoption("--browser").lower()
    
    # Identify paths for local drivers
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    drivers_path = os.path.join(base_path, "drivers")
    
    firefox_exe = os.path.join(drivers_path, "geckodriver.exe")
    edge_exe = os.path.join(drivers_path, "msedgedriver.exe")

    driver = None

    # --- 1. BROWSER INITIALIZATION ---
    if browser_name == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-features=PasswordLeakDetection")
        # Experimental options to kill the password manager popup
        prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
        chrome_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    elif browser_name == "firefox":
        ff_options = FirefoxOptions()
        ff_options.add_argument("-private")
        # Fixed size at launch to prevent 'Browsing context discarded' crash
        ff_options.add_argument("--width=1920")
        ff_options.add_argument("--height=1080")
        # Preferences from yesterday's stable run + Layout centering
        ff_options.set_preference("browser.startup.homepage_override.mstone", "ignore")
        ff_options.set_preference("startup.homepage_welcome_url.additional", "")
        ff_options.set_preference("sidebar.visible", False) 
        ff_options.set_preference("dom.disable_beforeunload", True)
        ff_options.set_preference("fission.autostart", False)
        
        driver = webdriver.Firefox(service=FirefoxService(executable_path=firefox_exe), options=ff_options)

    elif browser_name == "edge":
        edge_options = EdgeOptions()
        edge_options.add_argument("-inprivate")
        edge_options.add_argument("--window-size=1920,1080")
        driver = webdriver.Edge(service=EdgeService(executable_path=edge_exe), options=edge_options)
    
    else:
        raise ValueError(f"Browser {browser_name} is not supported.")

    # --- 2. STABILITY WAIT ---
    # Critical: Give the browser 2 seconds to initialize before sending commands
    time.sleep(2)
    
    # Do not call maximize_window() on Firefox as it causes the discard crash
    if browser_name != "firefox":
        try:
            driver.maximize_window()
        except:
            pass
            
    driver.implicitly_wait(10)

    # --- 3. INDIVIDUAL LOGGING PER TEST ---
    # Create unique name for the log file (handles CSV parametrization rows)
    node_name = request.node.name.replace("[", "_").replace("]", "_").replace(":", "_")
    log_dir = os.path.join(base_path, "reports", "logs")
    os.makedirs(log_dir, exist_ok=True)
    
    logger = logging.getLogger(node_name)
    logger.setLevel(logging.INFO)
    
    # Ensure no duplicate log entries
    if logger.hasHandlers():
        logger.handlers.clear()
        
    log_file_path = os.path.join(log_dir, f"{node_name}.log")
    file_handler = logging.FileHandler(log_file_path, mode='w')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Attach driver and logger to the class instance
    request.cls.driver = driver
    request.cls.logger = logger
    
    yield driver
    
    # --- 4. TEARDOWN ---
    try:
        driver.quit()
    except:
        pass # Handle cases where browser already crashed
    file_handler.close()
    logger.removeHandler(file_handler)

# --- SCREENSHOT HOOK FOR HTML REPORT ---
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Captures screenshots on test failure and embeds them in the HTML report.
    Includes try-except to prevent Pytest internal crashes.
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if (report.when == 'call' or report.when == "setup") and report.failed:
        # Safely get driver from the test class instance
        driver = getattr(item.instance, "driver", None) if item.instance else None
        
        if driver:
            try:
                # Setup folders
                os.makedirs("reports/screenshots", exist_ok=True)
                
                # File naming
                timestamp = datetime.now().strftime("%H%M%S")
                file_name = f"fail_{item.name}_{timestamp}.png"
                full_path = os.path.join("reports", "screenshots", file_name)
                
                # Capture
                driver.save_screenshot(full_path)
                
                # HTML Embedding
                if pytest_html:
                    relative_path = f"screenshots/{file_name}"
                    html = f'<div><img src="{relative_path}" alt="screenshot" style="width:300px;height:200px;" ' \
                           f'onclick="window.open(this.src)" align="right"/></div>'
                    extra.append(pytest_html.extras.html(html))
            except Exception as e:
                print(f"\nScreenshot Failed: {e}")
                
    report.extra = extra