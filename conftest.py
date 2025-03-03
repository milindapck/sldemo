import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from dotenv import load_dotenv

# Load Sauce Labs credentials from .env file
load_dotenv()
SAUCE_USERNAME = os.getenv("SAUCE_USERNAME")
SAUCE_ACCESS_KEY = os.getenv("SAUCE_ACCESS_KEY")

@pytest.fixture
def driver():
    """Setup Selenium WebDriver for Sauce Labs (Chrome)"""
    sauce_url = f"https://{SAUCE_USERNAME}:{SAUCE_ACCESS_KEY}@ondemand.us-west-1.saucelabs.com/wd/hub"

    # Sauce Labs desired capabilities
    capabilities = {
        "browserName": "chrome",
        "browserVersion": "latest",
        "platformName": "Windows 10",
        "sauce:options": {
            "name": "SauceDemo Test",
            "build": "SauceLabs-Selenium",
        },
    }

    driver = webdriver.Remote(command_executor=sauce_url, desired_capabilities=capabilities)
    driver.maximize_window()
    yield driver
    driver.quit()
