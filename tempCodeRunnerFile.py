from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException, TimeoutException
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Maximize window

# Set up WebDriver service with the correct path to chromedriver
service = Service()  # No need to specify the path as it's installed via pip

# Initialize WebDriver
try:
    driver = webdriver.Chrome(service=service, options=chrome_options)
    print("🚀 Chrome WebDriver initialized successfully!")

    # Set implicit wait before navigating to the URL
    driver.implicitly_wait(5)

    # Open the browser and navigate to the specified URL
    URL = "https://app-staging.nokodr.com/"
    print(f"🌐 Navigating to: {URL}")
    driver.get(URL)

    # Confirm if page loaded successfully
    if "404" in driver.page_source or "ResourceNotFound" in driver.page_source:
        print(f"❌ ERROR: The page '{URL}' does not exist. Check the URL.")
    else:
        print("✅ Website loaded successfully!")

    # Keep browser open indefinitely
    print("🚀 Browser will remain open. Manually close it when done.")
    while True:
        time.sleep(1)  # Prevents CPU overuse by running an infinite loop

except TimeoutException:
    print("⏳ ERROR: Page load timed out!")
except WebDriverException as e:
    print(f"❌ WebDriver Error: {e}")
except Exception as e:
    print(f"❌ Unexpected Error: {e}")
finally:
    # Ensure the browser quits in case of an error
    try:
        if 'driver' in locals():  # Check if driver is defined
            driver.quit()
    except Exception as e:
        print(f"❌ Error while quitting the browser: {e}")
