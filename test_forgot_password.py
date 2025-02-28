from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

# Prevents browser from closing automatically
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-extensions")  # Disable extensions
options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
options.add_argument("--incognito")  # Open Chrome in incognito mode
# options.add_argument("--headless")  # Uncomment to run in headless mode

# Use webdriver_manager to automatically manage the ChromeDriver binary
service = ChromeService(ChromeDriverManager().install())

driver = None  # Initialize driver as None

try:
    driver = webdriver.Chrome(service=service, options=options)
    print("🚀 Chrome WebDriver initialized successfully!")

    # Navigate to the Forgot Password page
    URL = "https://app-staging.nokodr.com/super/apps/auth/v1/index.html#/forgot-password"
    driver.get(URL)
    print(f"🌐 Opened URL: {URL}")

    # Function to submit forgot password request
    def forgot_password(email):
        try:
            wait = WebDriverWait(driver, 10)

            # Wait for the email input field
            email_field = wait.until(EC.presence_of_element_located((By.NAME, "email")))
            email_field.clear()
            email_field.send_keys(email)

            # Wait for and click the submit button
            submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Submit')]")))
            submit_button.click()

            time.sleep(2)  # Small delay for UI update
        except TimeoutException:
            print(f"❌ ERROR: Forgot Password form elements not found.")
        except NoSuchElementException as e:
            print(f"❌ ERROR: Element not found: {e}")
        except Exception as e:
            print(f"❌ ERROR: {e}")

    # Function to check for success/error messages
    def check_message():
        try:
            wait = WebDriverWait(driver, 5)
            message_element = wait.until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'message') or contains(text(), 'success') or contains(text(), 'error')]"))
            )
            return message_element.text if message_element else "No message displayed"
        except TimeoutException:
            return "No message displayed"

    # Test Cases
    test_cases = [
        ("registereduser@example.com", "Test 1 (Valid Email)"),
        ("invalid-email", "Test 2 (Invalid Email Format)"),
        ("unregistereduser@example.com", "Test 3 (Unregistered Email)"),
        ("", "Test 4 (Blank Email Field)"),
        ("test!@#$%^&*.com", "Test 5 (Special Characters in Email)"),
        ("a" * 100 + "@example.com", "Test 6 (Very Long Email)")
    ]

    # Run test cases
    for email, test_name in test_cases:
        print(f"\n🔹 Running {test_name}...")
        forgot_password(email)
        print(f"🔍 {test_name} Result: {check_message()}")
        print("-" * 50)

    # Keep browser open for debugging
    input("Press Enter to close the browser...")

except Exception as e:
    print(f"❌ ERROR: An unexpected error occurred. Details: {e}")
finally:
    # Ensure the browser quits in case of an error
    if driver:
        try:
            driver.quit()
        except Exception as e:
            print(f"❌ Error while quitting the browser: {e}")
