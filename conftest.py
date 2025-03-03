import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def pytest_addoption(parser):
    """Add command-line options for browser selection."""
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on")

@pytest.fixture
def browser(request):
    """Fixture to get the browser option from CLI."""
    return request.config.getoption("--browser")

@pytest.fixture
def driver(browser):
    """Setup Selenium WebDriver with Sauce Labs."""
    sauce_username = os.getenv("SAUCE_USERNAME")
    sauce_access_key = os.getenv("SAUCE_ACCESS_KEY")

    sauce_url = f"https://{sauce_username}:{sauce_access_key}@ondemand.us-west-1.saucelabs.com/wd/hub"

    capabilities = {
        "browserName": browser,
        "platformName": "Windows 10",
        "browserVersion": "latest",
        "sauce:options": {
            "name": "SauceDemo Selenium Test"
        }
    }

    driver = webdriver.Remote(command_executor=sauce_url, options=webdriver.ChromeOptions() if browser == "chrome" else webdriver.FirefoxOptions())
    driver.maximize_window()
    
    yield driver
    driver.quit()
