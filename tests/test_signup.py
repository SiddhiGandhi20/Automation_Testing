from utils.browser_setup import BrowserSetup
from selenium.webdriver.common.by import By
import time

class TestSignup:
    def setup(self):
        self.browser = BrowserSetup()
        self.browser.navigate_to("https://app-staging.nokodr.com/super/apps/auth/v1/index.html#/login")
        signup_link = self.browser.wait_for_clickable((By.XPATH, "//div[@class='slds-float_right']/a[contains(text(), 'Sign up')]"))
        signup_link.click()

    def fill_signup_form(self, name, email, password, confirm_password):
        name_field = self.browser.wait_for_element((By.CSS_SELECTOR, "input[name='name'].slds-input"))  
        name_field.send_keys(name)
        email_field = self.browser.wait_for_element((By.CSS_SELECTOR, "input[name='email'].slds-input"))  
        email_field.send_keys(email)
        password_field = self.browser.wait_for_element((By.CSS_SELECTOR, "input[name='password'].slds-input"))  # 
        password_field.send_keys(password)
        confirm_password_field = self.browser.wait_for_element((By.CSS_SELECTOR, "input[name='confirm_password'].slds-input"))  
        confirm_password_field.send_keys(confirm_password)
        submit_button = self.browser.wait_for_clickable((By.XPATH, "//button[contains(text(), 'Sign Up')]")) 
        submit_button.click()

    def get_message(self):
        message = self.browser.wait_for_element((By.CLASS_NAME, "message"))  
        return message.text

    def test_signup(self):
        print("Testing valid inputs...")
        self.fill_signup_form("Saurabh Pande", "pandesaurabh4596@gmail.com", "Pass@1234", "Pass@1234")
        assert "Account created successfully!" in self.get_message(), "Valid signup failed"
        time.sleep(2)

        print("Testing invalid email...")
        self.browser.navigate_to("https://app-staging.nokodr.com/super/apps/auth/v1/index.html#/login")
        signup_link = self.browser.wait_for_clickable((By.XPATH, "//div[@class='slds-float_right']/a[contains(text(), 'Sign up')]"))
        signup_link.click()
        self.fill_signup_form("xyz", "xyx@gmail.com", "Password123!", "Password123!")
        assert "Invalid email" in self.get_message(), "Invalid email test failed"
        time.sleep(2)

        print("Testing password mismatch...")
        self.browser.navigate_to("https://app-staging.nokodr.com/super/apps/auth/v1/index.html#/login")
        signup_link = self.browser.wait_for_clickable((By.XPATH, "//div[@class='slds-float_right']/a[contains(text(), 'Sign up')]"))
        signup_link.click()
        self.fill_signup_form("John Doe", "john.doe@example.com", "Password123!", "WrongPass!")
        assert "Passwords do not match" in self.get_message(), "Password mismatch test failed"
        time.sleep(2)

        print("Testing blank fields...")
        self.browser.navigate_to("https://app-staging.nokodr.com/super/apps/auth/v1/index.html#/login")
        signup_link = self.browser.wait_for_clickable((By.XPATH, "//div[@class='slds-float_right']/a[contains(text(), 'Sign up')]"))
        signup_link.click()
        self.fill_signup_form("", "", "", "")
        assert "required" in self.get_message(), "Blank fields test failed"
        time.sleep(2)

        
        print("Testing special characters in name...")
        self.browser.navigate_to("https://app-staging.nokodr.com/super/apps/auth/v1/index.html#/login")
        signup_link = self.browser.wait_for_clickable((By.XPATH, "//div[@class='slds-float_right']/a[contains(text(), 'Sign up')]"))
        signup_link.click()
        self.fill_signup_form("John@#$%", "john.doe@example.com", "Password123!", "Password123!")
        message = self.get_message()
        print(f"Message: {message}")

    def teardown(self):
        self.browser.quit()

if __name__ == "__main__":
    test = TestSignup()
    test.setup()
    test.test_signup()
    test.teardown()