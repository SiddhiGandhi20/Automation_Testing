from utils.browser_setup import get_driver
import time
def test_open_browser():
    driver = get_driver()
    driver.get("https://app-staging.nokodr.com/")
    time.sleep(3)  
    driver.quit()
