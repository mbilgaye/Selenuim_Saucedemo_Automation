import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Fixtures for browser setup
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# Parameterization: multiple usernames
@pytest.mark.parametrize("username", [
"standard_user",
"locked_out_user",
"problem_user",
"performance_glitch_user",
"error_user",
"visual_user"
])

def test_login(driver, username):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)

# Validation
    if username == "locked_out_user":
        error = driver.find.element(By.CLASS_NAME, "error message container").text
        assert "locked out" in error
    else:
        assert "inventory" in driver.current_url