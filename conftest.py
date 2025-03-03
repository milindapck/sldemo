import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

#SAUCE_USERNAME = "oauth-milindapck-80262"
#SAUCE_ACCESS_KEY = "0f5e5607-dd62-4bf2-8b0f-2bfeaa24e92a"
SAUCE_USERNAME = os.getenv("SAUCE_USERNAME")
SAUCE_ACCESS_KEY = os.getenv("SAUCE_ACCESS_KEY")

# Verify Sauce Labs credentials
if not SAUCE_USERNAME or not SAUCE_ACCESS_KEY:
    raise Exception("Sauce Labs credentials are missing.")

SAUCE_URL = "https://ondemand.eu-central-1.saucelabs.com:443/wd/hub"

@pytest.fixture
def driver():
    # Setup Sauce Labs Selenium WebDriver.
    options = webdriver.ChromeOptions()
    sauce_options = {
        "username": SAUCE_USERNAME,
        "accessKey": SAUCE_ACCESS_KEY,
        "browserName": "chrome",
        "platformName": "Windows 10",
        "browserVersion": "latest",
        "name": "SauceLabs Automation for Walmart",
        "build": "Milinda"
    }
    options.set_capability("sauce:options", sauce_options)

    driver = webdriver.Remote(command_executor=SAUCE_URL, options=options)
    yield driver
    driver.quit()
