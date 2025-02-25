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

# ✅ SIGNUP PAGE URL
SIGNUP_URL = "https://app-staging.nokodr.com/super/apps/auth/v1/index.html#/signup"

# ✅ FUNCTION TO OPEN SIGNUP PAGE
def open_signup_page():
    """Opens the signup page and validates if it exists."""
    print(f"🌐 Navigating to: {SIGNUP_URL}")
    driver.get(SIGNUP_URL)

    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # Check if the page contains "404" or "Not Found"
        if "404" in driver.page_source or "not found" in driver.page_source.lower():
            print(f"❌ ERROR: Signup page '{SIGNUP_URL}' not found. Check the URL.")
            return False  # ❌ Page did not load, but browser stays open

        print("✅ Signup page loaded successfully!")
        return True  # ✅ Page loaded, continue tests

    except TimeoutException:
        print("⏳ ERROR: Page took too long to load! Server might be slow.")
        return False
    except Exception as e:
        print(f"❌ ERROR: Unable to load signup page. Details: {e}")
        return False


# ✅ FUNCTION TO HANDLE SIGNUP TEST CASES
def signup(name, email, password, confirm_password, expected_message):
    """Performs a signup attempt and checks for success or error messages."""
    try:
        wait = WebDriverWait(driver, 10)

        # Enter Name
        name_field = wait.until(EC.presence_of_element_located((By.NAME, "name")))
        name_field.clear()
        name_field.send_keys(name)

        # Enter Email
        email_field = wait.until(EC.presence_of_element_located((By.NAME, "email")))
        email_field.clear()
        email_field.send_keys(email)

        # Enter Password
        password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))
        password_field.clear()
        password_field.send_keys(password)

        # Enter Confirm Password
        confirm_password_field = wait.until(EC.presence_of_element_located((By.NAME, "confirm_password")))
        confirm_password_field.clear()
        confirm_password_field.send_keys(confirm_password)

        # Click Signup Button
        signup_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Sign Up')]")))
        signup_button.click()

        # Wait for response message
        time.sleep(3)
        try:
            message = driver.find_element(By.XPATH, "//*[contains(text(), 'Account created successfully') or contains(text(), 'Error')]").text
        except NoSuchElementException:
            message = "❌ No response message found!"

        # ✅ CHECK EXPECTED RESULT
        if expected_message in message:
            print(f"✅ Test Passed: {expected_message}")
        else:
            print(f"❌ Test Failed: Expected '{expected_message}', but got '{message}'")

    except Exception as e:
        print(f"❌ ERROR during signup: {e}")


# ✅ RUN TEST CASES
if not open_signup_page():
    print("❌ Tests could not run as the signup page did not load.")
    print("✅ Browser remains open for manual verification.")
else:
    print("\n🚀 Running Signup Tests...\n")

    # ✅ Test 1: Valid Signup
    print("🔹 Test 1 (Valid Data):")
    signup("John Doe", "johndoe@example.com", "StrongPass@123", "StrongPass@123", "Account created successfully!")

    # ✅ Test 2: Invalid Email Format
    print("🔹 Test 2 (Invalid Email Format):")
    signup("John Doe", "invalid-email", "StrongPass@123", "StrongPass@123", "Error: Invalid email format.")

    # ✅ Test 3: Passwords Not Matching
    print("🔹 Test 3 (Mismatched Passwords):")
    signup("John Doe", "johndoe@example.com", "StrongPass@123", "WrongPass@123", "Error: Passwords do not match.")

    # ✅ Test 4: Missing Name
    print("🔹 Test 4 (Missing Name):")
    signup("", "johndoe@example.com", "StrongPass@123", "StrongPass@123", "Error: Name is required.")

    # ✅ Test 5: Missing Email
    print("🔹 Test 5 (Missing Email):")
    signup("John Doe", "", "StrongPass@123", "StrongPass@123", "Error: Email is required.")

    # ✅ Test 6: Missing Passwords
    print("🔹 Test 6 (Missing Passwords):")
    signup("John Doe", "johndoe@example.com", "", "", "Error: Password is required.")

    # ✅ Test 7: Edge Case - Special Characters in Name
    print("🔹 Test 7 (Special Characters in Name):")
    signup("J@hn D#e!", "johndoe@example.com", "StrongPass@123", "StrongPass@123", "Error: Invalid name format.")

    # ✅ Test 8: Edge Case - Excessively Long Inputs
    print("🔹 Test 8 (Excessively Long Inputs):")
    long_name = "A" * 300  # 300 characters long
    long_email = "longemail" + ("a" * 200) + "@example.com"
    long_password = "P@ssword" + ("1" * 100)
    signup(long_name, long_email, long_password, long_password, "Error: Input exceeds character limit.")

    # ✅ OPTIONAL: Email/OTP Verification Test (If applicable)
    print("🔹 Test 9 (Email/OTP Verification - Optional):")
    signup("John Doe", "otpuser@example.com", "StrongPass@123", "StrongPass@123", "Enter the OTP sent to your email.")

# ✅ Browser stays open for manual debugging
print("\n✅ Signup Tests Completed! The browser remains open for manual verification.")
