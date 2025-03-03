import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

BASE_URL = "https://www.saucedemo.com"

def test_login(driver):
    # Test successful login
    driver.get(BASE_URL)
    driver.maximize_window()
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    #assert "inventory.html" in driver.current_url, "Login failed"
    result = "inventory.html" in driver.current_url
    jobStatus = "passed" if result else "failed"
    driver.execute_script("sauce:job-result=" + jobStatus)

def test_invalid_login(driver):
    # Test invalid login
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys("wrong_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()
    error_msg = driver.find_element(By.CLASS_NAME, "error-message-container").text
    result = "Epic sadface" in error_msg
    jobStatus = "passed" if result else "failed"
    driver.execute_script("sauce:job-result=" + jobStatus)

def test_add_item_to_cart(driver):
    # Test adding an item to cart
    test_login(driver)
    driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack").click()
    cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    jobStatus = "passed" if cart_count == "1" else "failed"
    driver.execute_script("sauce:job-result=" + jobStatus)

def test_remove_item_from_cart(driver):
    # Test removing an item from cart
    test_add_item_to_cart(driver)
    driver.find_element(By.NAME, "remove-sauce-labs-backpack").click()
    jobStatus = "passed" if not driver.find_elements(By.CLASS_NAME, "shopping_cart_badge") else "failed"
    driver.execute_script("sauce:job-result=" + jobStatus)

def test_logout(driver):
    # Test logout functionality
    test_login(driver)
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    driver.find_element(By.ID, "logout_sidebar_link").click()
    jobStatus = "passed" if driver.find_elements(By.CLASS_NAME, "login_logo") else "failed"
    driver.execute_script("sauce:job-result=" + jobStatus)

def test_sort_items(driver):
    # Test sorting items
    test_login(driver)
    dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
    dropdown.send_keys(Keys.DOWN)
    result = "inventory.html" in driver.current_url
    jobStatus = "passed" if result else "failed"
    driver.execute_script("sauce:job-result=" + jobStatus)

def test_view_product_details(driver):
    # Test viewing a product details
    test_login(driver)
    driver.find_element(By.CLASS_NAME, "inventory_item_name").click()
    result = "inventory-item.html?id=" in driver.current_url
    jobStatus = "passed" if result else "failed"
    driver.execute_script("sauce:job-result=" + jobStatus)

def test_checkout_process(driver):
    # Test checkout process
    test_add_item_to_cart(driver)
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.CLASS_NAME, "checkout_button").click()
    result = "checkout-step-one.html" in driver.current_url
    jobStatus = "passed" if result else "failed"
    driver.execute_script("sauce:job-result=" + jobStatus)

def test_continue_shopping(driver):
    # Test continue shopping button
    test_checkout_process(driver)
    driver.find_element(By.CLASS_NAME, "cart_cancel_link").click()
    driver.find_element(By.NAME, "continue-shopping").click()
    result = "inventory.html" in driver.current_url
    jobStatus = "passed" if result else "failed"
    driver.execute_script("sauce:job-result=" + jobStatus)

def test_complete_order(driver):
    # Test completing an order
    test_checkout_process(driver)
    driver.find_element(By.ID, "first-name").send_keys("Milinda")
    driver.find_element(By.ID, "last-name").send_keys("Perera")
    driver.find_element(By.ID, "postal-code").send_keys("DA15GB")
    driver.find_element(By.NAME, "continue").click()
    driver.find_element(By.NAME, "finish").click()
    result = "checkout-complete.html" in driver.current_url
    jobStatus = "passed" if result else "failed"
    driver.execute_script("sauce:job-result=" + jobStatus)
