from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

# ✅ SETUP SELENIUM DRIVER
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# ✅ LOGIN PAGE URL
LOGIN_URL = "https://app-staging.nokodr.com/super/apps/auth/v1/index.html#/login"

# ✅ FUNCTION TO OPEN LOGIN PAGE
def open_login_page():
    """Opens the login page and validates if it exists."""
    print(f"🌐 Navigating to: {LOGIN_URL}")
    driver.get(LOGIN_URL)

    try:
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # Check if the page exists
        page_source = driver.page_source.lower()
        if "404" in page_source or "resource not found" in page_source:
            print("❌ ERROR: Login page not found (404). Check the URL.")
            return False  # Page does not exist, tests should not proceed

        print("✅ Login page loaded successfully!")
        return True  # Page loaded, continue tests

    except TimeoutException:
        print("⏳ ERROR: Login page took too long to load! Check if the site is down.")
        return False  # Page load timeout, tests should not proceed
    except Exception as e:
        print(f"❌ ERROR: Unable to load login page. Details: {e}")
        return False

# ✅ FUNCTION TO HANDLE LOGIN TEST CASES
def login(email, password, expected_message):
    """Performs a login attempt and checks for success or error messages."""
    try:
        wait = WebDriverWait(driver, 10)

        # Enter Email
        email_field = wait.until(EC.presence_of_element_located((By.NAME, "email")))
        email_field.clear()
        email_field.send_keys(email)

        # Enter Password
        password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))
        password_field.clear()
        password_field.send_keys(password)

        # Click Login Button
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Login')]")))
        login_button.click()

        # Wait for response message
        time.sleep(3)  # Allow time for the message to appear

        try:
            message_element = driver.find_element(By.XPATH, "//*[contains(text(), 'Welcome back') or contains(text(), 'Error')]")
            message = message_element.text
        except NoSuchElementException:
            message = "❌ No response message found!"

        # ✅ CHECK EXPECTED RESULT
        if expected_message in message:
            print(f"✅ Test Passed: {expected_message}")
        else:
            print(f"❌ Test Failed: Expected '{expected_message}', but got '{message}'")

    except Exception as e:
        print(f"❌ ERROR during login: {e}")

# ✅ RUN TEST CASES
if not open_login_page():
    print("❌ Tests could not run as the login page did not load.")
    print("✅ Browser remains open for manual verification.")
else:
    print("\n🚀 Running Login Tests...\n")

    # ✅ Test 1: Valid Login
    print("🔹 Test 1 (Valid Credentials):")
    login("johndoe@example.com", "StrongPass@123", "Welcome back!")

    # ✅ Test 2: Invalid Password
    print("🔹 Test 2 (Invalid Password):")
    login("johndoe@example.com", "WrongPassword", "Error: Incorrect password.")

    # ✅ Test 3: Unregistered Email
    print("🔹 Test 3 (Unregistered Email):")
    login("notregistered@example.com", "StrongPass@123", "Error: User does not exist.")

    # ✅ Test 4: Missing Email
    print("🔹 Test 4 (Missing Email):")
    login("", "StrongPass@123", "Error: Email is required.")

    # ✅ Test 5: Missing Password
    print("🔹 Test 5 (Missing Password):")
    login("johndoe@example.com", "", "Error: Password is required.")

    # ✅ Test 6: Edge Case - Special Characters in Email
    print("🔹 Test 6 (Special Characters in Email):")
    login("john!@doe.com", "StrongPass@123", "Error: Invalid email format.")

    # ✅ Test 7: Edge Case - Excessively Long Email/Password
    print("🔹 Test 7 (Excessively Long Inputs):")
    long_email = "longemail" + ("a" * 200) + "@example.com"
    long_password = "P@ssword" + ("1" * 100)
    login(long_email, long_password, "Error: Input exceeds character limit.")

# ✅ Browser stays open for manual debugging
print("\n✅ Login Tests Completed! The browser remains open for manual verification.")
