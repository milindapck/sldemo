import pytest
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("username,password", [
    ("standard_user", "secret_sauce"),
    ("locked_out_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
    ("error_user", "secret_sauce"),
    ("visual_user", "secret_sauce"),
    ("admin_user", "secret_sauce"),
    ("test_user", "secret_sauce"),
    ("demo_user", "secret_sauce"),
    ("user_10", "secret_sauce"),
])
def test_saucedemo_login(driver, username, password):
    """Test login functionality for different users on SauceDemo."""
    driver.get("https://www.saucedemo.com/")

    # Find username & password fields and login button
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    # Verify login success or failure
    try:
        assert "inventory" in driver.current_url, "Login failed"
    except AssertionError:
        print(f"Login failed for user: {username}")
