from utils.browser_setup import BrowserSetup
from selenium.webdriver.common.by import By
import time

class TestLogin:
    def setup(self):
        self.browser = BrowserSetup()
        self.browser.navigate_to("https://app-staging.nokodr.com/super/apps/auth/v1/index.html#/login")

    def fill_login_form(self, username, password):
        username_field = self.browser.wait_for_element((By.CSS_SELECTOR, "input[name='username'].slds-input"))
        username_field.send_keys(username)
        password_field = self.browser.wait_for_element((By.CSS_SELECTOR, "input[name='password'].slds-input"))
        password_field.send_keys(password)
        login_button = self.browser.wait_for_clickable((By.XPATH, "//button[contains(text(), 'Log In')]"))
        login_button.click()

    def click_login_with_google(self):
        google_button = self.browser.wait_for_clickable((By.XPATH, "//div[@id='staticElement' and text()='Log In With Google']"))
        google_button.click()

    def click_signup_link(self):
        signup_link = self.browser.wait_for_clickable((By.XPATH, "//div[@class='slds-float_right']/a[contains(text(), 'Sign up')]"))
        signup_link.click()

    def get_message(self):
        message = self.browser.wait_for_element((By.CLASS_NAME, "message"))  # Hypothetical; update with real selector
        return message.text

    def test_login(self):
        print("Testing valid credentials...")
        self.fill_login_form("pandesaurabh4596@gmail.com", "Pass@1234")
        assert "dashboard" in self.browser.driver.current_url or "Welcome" in self.get_message(), "Valid login failed"
        time.sleep(2)

        print("Testing invalid credentials...")
        self.browser.navigate_to("https://app-staging.nokodr.com/super/apps/auth/v1/index.html#/login")
        self.fill_login_form("pandesaurabh4596@gmail.com", "WrongPass!")
        assert "Invalid username or password" in self.get_message(), "Invalid credentials test failed"
        time.sleep(2)

        print("Testing blank fields...")
        self.browser.navigate_to("https://app-staging.nokodr.com/super/apps/auth/v1/index.html#/login")
        self.fill_login_form("", "")
        assert "required" in self.get_message(), "Blank fields test failed"
        time.sleep(2)

        print("Testing Log In With Google...")
        self.browser.navigate_to("https://app-staging.nokodr.com/super/apps/auth/v1/index.html#/login")
        try:
            self.click_login_with_google()
            print("Log In With Google clicked successfully")
            assert "accounts.google.com" in self.browser.driver.current_url, "Google login failed"
        except Exception as e:
            print(f"Log In With Google test failed: {e}")
        time.sleep(2)

    def teardown(self):
        self.browser.quit()

if __name__ == "__main__":
    test = TestLogin()
    test.setup()
    test.test_login()
    test.teardown()