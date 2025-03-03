import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from dotenv import load_dotenv

# Load Sauce Labs credentials from .env file
load_dotenv()
SAUCE_USERNAME = os.getenv("SAUCE_USERNAME")
SAUCE_ACCESS_KEY = os.getenv("SAUCE_ACCESS_KEY")

# Verify if credentials are being retrieved
if not SAUCE_USERNAME or not SAUCE_ACCESS_KEY:
    raise Exception("Sauce Labs credentials are missing! Ensure SAUCE_USERNAME and SAUCE_ACCESS_KEY are set.")

SAUCE_URL = "https://ondemand.eu-central-1.saucelabs.com:443/wd/hub"

@pytest.fixture
def driver():
    """Setup Sauce Labs Selenium WebDriver."""
    options = webdriver.ChromeOptions()
    sauce_options = {
        "username": SAUCE_USERNAME,
        "accessKey": SAUCE_ACCESS_KEY,
        "browserName": "chrome",
        "platformName": "Windows 10",
        "browserVersion": "latest",
        "name": "SauceLabs Test",
        "build": "Milinda"
    }
    options.set_capability("sauce:options", sauce_options)

    driver = webdriver.Remote(command_executor=SAUCE_URL, options=options)
    yield driver
    driver.quit()
