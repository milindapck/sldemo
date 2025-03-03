import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

BASE_URL = "https://www.saucedemo.com"

def test_login(driver):
    """Test successful login"""
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    assert "inventory.html" in driver.current_url, "Login failed"

def test_invalid_login(driver):
    """Test invalid login"""
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys("wrong_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()
    error_msg = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Epic sadface" in error_msg, "Error message not displayed"

def test_add_item_to_cart(driver):
    """Test adding an item to cart"""
    test_login(driver)
    driver.find_element(By.CLASS_NAME, "btn_inventory").click()
    cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert cart_count == "1", "Item was not added to cart"

def test_remove_item_from_cart(driver):
    """Test removing an item from cart"""
    test_add_item_to_cart(driver)
    driver.find_element(By.CLASS_NAME, "cart_button").click()
    assert not driver.find_elements(By.CLASS_NAME, "shopping_cart_badge"), "Item was not removed"

def test_logout(driver):
    """Test logout functionality"""
    test_login(driver)
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    driver.find_element(By.ID, "logout_sidebar_link").click()
    assert "login.html" in driver.current_url, "Logout failed"

def test_sort_items(driver):
    """Test sorting items"""
    test_login(driver)
    dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
    dropdown.send_keys(Keys.DOWN)
    assert "inventory.html" in driver.current_url, "Sorting failed"

def test_view_product_details(driver):
    """Test viewing a product details"""
    test_login(driver)
    driver.find_element(By.CLASS_NAME, "inventory_item_name").click()
    assert "inventory-item.html" in driver.current_url, "Product details not displayed"

def test_checkout_process(driver):
    """Test checkout process"""
    test_add_item_to_cart(driver)
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.CLASS_NAME, "checkout_button").click()
    assert "checkout-step-one.html" in driver.current_url, "Checkout process failed"

def test_continue_shopping(driver):
    """Test continue shopping button"""
    test_checkout_process(driver)
    driver.find_element(By.CLASS_NAME, "cart_cancel_link").click()
    assert "inventory.html" in driver.current_url, "Continue shopping failed"

def test_complete_order(driver):
    """Test completing an order"""
    test_checkout_process(driver)
    driver.find_element(By.CLASS_NAME, "cart_button").click()
    driver.find_element(By.CLASS_NAME, "btn_action").click()
    assert "checkout-complete.html" in driver.current_url, "Order was not completed"
