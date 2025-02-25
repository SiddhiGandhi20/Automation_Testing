from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException, TimeoutException

import time

# ✅ Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Maximize window

# ✅ Set up WebDriver service (Ensure correct path if needed)
service = Service()  # If needed, specify chromedriver path inside Service("path/to/chromedriver")

# ✅ Initialize WebDriver
try:
    driver = webdriver.Chrome(service=service, options=chrome_options)
    print("🚀 Chrome WebDriver initialized successfully!")

    # ✅ Open the browser and navigate to the specified URL
    URL = "https://app-staging.nokodr.com/"
    print(f"🌐 Navigating to: {URL}")
    driver.get(URL)

    # ✅ Wait for elements to load (Implicit Wait)
    driver.implicitly_wait(5)  

    # ✅ Confirm if page loaded successfully
    if "404" in driver.page_source or "ResourceNotFound" in driver.page_source:
        print(f"❌ ERROR: The page '{URL}' does not exist. Check the URL.")
    else:
        print("✅ Website loaded successfully!")

    # ✅ Keep browser open indefinitely
    print("🚀 Browser will remain open. Manually close it when done.")
    while True:
        time.sleep(1)  # Prevents CPU overuse by running an infinite loop

except TimeoutException:
    print("⏳ ERROR: Page load timed out!")
except WebDriverException as e:
    print(f"❌ WebDriver Error: {e}")
except Exception as e:
    print(f"❌ Unexpected Error: {e}")
