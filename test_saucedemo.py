from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_saucedemo_login_and_product_check():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(6)

    title = driver.find_element(By.CLASS_NAME, "title").text
    assert title == "Products"

    product_name = driver.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']")
    assert product_name.is_displayed()

    driver.quit()