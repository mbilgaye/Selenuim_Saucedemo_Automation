from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from selenium.webdriver.support.ui import Select

def test_homepage():
    # 1. Launch browser
    driver = webdriver.Chrome()
    driver.maximize_window()

    # 2. Navigate to url
    driver.get("http://www.automationexercise.com/")
    time.sleep(2)

    # 3. Check webpage visibility
    assert "Automation Exercise" in driver.title

    # 4.Click "Signup/Login"
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()
    time.sleep(2)

    # 5. Verify "New User Signup!" is visible
    assert "New User Signup!" in driver.page_source

    # 6. Enter name and email
    name = 'TestUser'
    email = f"user{random.randint(1000,9999)}@gmail.com"

    driver.find_element(By.NAME, "name").send_keys(name)
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-email']").send_keys(email)
    time.sleep(2)

    # 7. Click "Signup" button
    driver.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']").click()
    time.sleep(2)

    # 8. Verify "ENTER ACCOUNT INFORMATION"
    assert "Account Information" in driver.page_source
    time.sleep(2)

    # 9. Fill account details
    driver.find_element(By.ID, "id_gender1").click()
    driver.find_element(By.ID, "password").send_keys("password123")

    # Date of birth
    driver.find_element(By.ID, "days").send_keys("10")
    driver.find_element(By.ID, "months").send_keys("June")
    driver.find_element(By.ID, "years").send_keys("1990")

    # 10. Select newsletter
    driver.find_element(By.ID, "newsletter").click()

    # 11. Select special offers
    driver.find_element(By.ID, "optin").click()

    # 12. Fill address details
    driver.find_element(By.ID, "first_name").send_keys("Test")
    driver.find_element(By.ID, "last_name").send_keys("User")
    driver.find_element(By.ID, "company").send_keys("TestCompany")
    driver.find_element(By.ID, "address1").send_keys("Street1")
    driver.find_element(By.ID, "address2").send_keys("Street2")

    Select(driver.find_element(By.ID, "country")).select_by_visible_text("India")

    driver.find_element(By.ID, "state").send_keys("Berlin")
    driver.find_element(By.ID, "city").send_keys("Berlin")
    driver.find_element(By.ID, "zipcode").send_keys("12345")
    driver.find_element(By.ID, "mobile_number").send_keys("1234567890")

    time.sleep(2)

    # 13. Click Create Account
    driver.find_element(By.CSS_SELECTOR, "button[data-qa='create-account']").click()
    time.sleep(5)

    # 14. Verify Account Created
    assert "Account Created!" in driver.page_source

    # 15. Click Continue
    driver.find_element(By.CSS_SELECTOR, "a[data-qa='continue-button']").click()
    time.sleep(6)

    # 16. Verify Logged in as username
    assert "Logged in as" in driver.page_source

    # 17. Click Delete Account
    driver.find_element(By.LINK_TEXT, "Delete Account").click()
    time.sleep(2)

    # 18. Close browser
    driver.quit()