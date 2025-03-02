from utils.browser_setup import BrowserSetup
from selenium.webdriver.common.by import By
import time

class TestForgotPassword:
    def setup(self):
        self.browser = BrowserSetup()
        self.browser.navigate_to("https://app-staging.nokodr.com/super/apps/auth/v1/index.html#/login")
        forgot_password_link = self.browser.wait_for_clickable((By.XPATH, "//a[text()='Forgot Password?']"))
        forgot_password_link.click()

    def fill_forgot_password_form(self, email):
        email_field = self.browser.wait_for_element((By.CSS_SELECTOR, "input[name='email'].slds-input"))  
        email_field.send_keys(email)
        submit_button = self.browser.wait_for_clickable((By.XPATH, "//button[contains(text(), 'Submit')]"))  
        submit_button.click()

    def get_message(self):
        message = self.browser.wait_for_element((By.CLASS_NAME, "message"))  
        return message.text

    def test_forgot_password(self):
        print("Testing valid email...")
        self.fill_forgot_password_form("pandesauabh4596@gmail.com")  ##actaul mail address
        assert "Reset link sent" in self.get_message(), "Valid email test failed"
        time.sleep(2)

        print("Testing non-registered email...")
        self.browser.navigate_to("https://app-staging.nokodr.com/super/apps/auth/v1/index.html#/login")
        forgot_password_link = self.browser.wait_for_clickable((By.XPATH, "//a[text()='Forgot Password?']"))
        forgot_password_link.click()
        self.fill_forgot_password_form("unknown@example.com")
        assert "not registered" in self.get_message(), "Non-registered email test failed"
        time.sleep(2)

        print("Testing invalid email...")
        self.browser.navigate_to("https://app-staging.nokodr.com/super/apps/auth/v1/index.html#/login")
        forgot_password_link = self.browser.wait_for_clickable((By.XPATH, "//a[text()='Forgot Password?']"))
        forgot_password_link.click()
        self.fill_forgot_password_form("invalid-email")
        assert "Invalid email" in self.get_message(), "Invalid email test failed"
        time.sleep(2)

        print("Testing blank email...")
        self.browser.navigate_to("https://app-staging.nokodr.com/super/apps/auth/v1/index.html#/login")
        forgot_password_link = self.browser.wait_for_clickable((By.XPATH, "//a[text()='Forgot Password?']"))
        forgot_password_link.click()
        self.fill_forgot_password_form("")
        assert "required" in self.get_message(), "Blank email test failed"
        time.sleep(2)

    def teardown(self):
        self.browser.quit()

if __name__ == "__main__":
    test = TestForgotPassword()
    test.setup()
    test.test_forgot_password()
    test.teardown()