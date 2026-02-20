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

# --- LOGIC 1: DYNAMIC RUN FOLDER GENERATION ---
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """This runs once before everything else."""
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    run_dir = os.path.join("reports", f"run_{now}")
    
    # This environment variable is the "Logic" that lets your other files
    # know where to save manual screenshots.
    os.environ["CURRENT_RUN_DIR"] = run_dir
    
    config.run_dir = run_dir
    
    # LOGIC 2: Create sub-folders INSIDE the new run folder
    os.makedirs(os.path.join(run_dir, "logs"), exist_ok=True)
    os.makedirs(os.path.join(run_dir, "screenshots"), exist_ok=True)
    os.makedirs(os.path.join(run_dir, "errors"), exist_ok=True)

    # LOGIC 3: Automatically move the HTML report into this folder
    browser = config.getoption("--browser")
    config.option.htmlpath = os.path.join(run_dir, f"{browser}.html")
    config.option.self_contained_html = True

@pytest.fixture(scope="function")
def setup(request):
    """Initializes browser and sets up logging inside the current run folder."""
    browser_name = request.config.getoption("--browser").lower()
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    drivers_path = os.path.join(base_path, "drivers")
    
    firefox_exe = os.path.join(drivers_path, "geckodriver.exe")
    edge_exe = os.path.join(drivers_path, "msedgedriver.exe")

    driver = None

    if browser_name == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-features=PasswordLeakDetection")
        prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
        chrome_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    elif browser_name == "firefox":
        ff_options = FirefoxOptions()
        ff_options.add_argument("-private")
        ff_options.add_argument("--width=1920")
        ff_options.add_argument("--height=1080")
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

    time.sleep(2)
    
    if browser_name != "firefox":
        try: driver.maximize_window()
        except: pass
            
    driver.implicitly_wait(10)

    # --- LOGGING PATH LOGIC ---
    run_dir = request.config.run_dir
    node_name = request.node.name.replace("[", "_").replace("]", "_").replace(":", "_")
    log_dir = os.path.join(run_dir, "logs")
    
    logger = logging.getLogger(node_name)
    logger.setLevel(logging.INFO)
    
    if logger.hasHandlers():
        logger.handlers.clear()
        
    log_file_path = os.path.join(log_dir, f"{node_name}.log")
    file_handler = logging.FileHandler(log_file_path, mode='w')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    request.cls.driver = driver
    request.cls.logger = logger
    request.cls.run_dir = run_dir 
    
    yield driver
    
    try: driver.quit()
    except: pass 
    file_handler.close()
    logger.removeHandler(file_handler)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Failure screenshot logic."""
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if (report.when == 'call' or report.when == "setup") and report.failed:
        driver = getattr(item.instance, "driver", None) if item.instance else None
        
        if driver:
            try:
                run_dir = item.config.run_dir
                screenshot_dir = os.path.join(run_dir, "screenshots")
                
                timestamp = datetime.now().strftime("%H%M%S")
                file_name = f"fail_{item.name}_{timestamp}.png"
                full_path = os.path.join(screenshot_dir, file_name)
                
                driver.save_screenshot(full_path)
                
                if pytest_html:
                    relative_path = f"screenshots/{file_name}"
                    html = f'<div><img src="{relative_path}" alt="screenshot" style="width:300px;height:200px;" ' \
                           f'onclick="window.open(this.src)" align="right"/></div>'
                    extra.append(pytest_html.extras.html(html))
            except Exception as e:
                print(f"\nScreenshot Failed: {e}")
                
    report.extra = extra