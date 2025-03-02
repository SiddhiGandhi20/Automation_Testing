# noKodr Automation Testing Project With Selenium and python

- This project contains automated tests for the [noKodr](https://app-staging.nokodr.com/) platform using **Selenium with Python**, as part of the **Enzigma's** Automation Testing Assignment. The tests validate the functionality of the **login**, **signup** and **forgot password** features, as well as a basic script to navigate to the platform.

---

## 📂 Project Structure
``` bash
selenium_automation_project/
│── tests/
│   ├── open_browser.py 
│   ├── test_signup.py
│   ├── test_login.py
│   ├── test_forgot_password.py
│── utils/
│   ├── browser_setup.py
│── requirements.txt
```
---

## ⚙️ **Setup and Installation**
- Before running the automation scripts, install the required dependencies.

### **1️⃣ Install Dependencies**
- Run the following command to install Selenium and WebDriver Manager:
```bash
pip install -r requirements.txt
```

## **How to Run the Tests**

### **1️⃣ Run All Tests**
```bash
pytest tests/
```
- or test with python
  

### **2️⃣ Run a Specific Test**
- To test opening browser and navigate to noKodr
 ``` bash
    python open_browser.py
```
- To test Signup Page Validation-
 ```bash
    python tests/test_signup.py
```
- To test Login Page Validation-
 ```bash
    python tests/test_login.py
```
- To test Forgot Password Validation-
```bash
    python tests/test_forgot_password.py
```
## 🖥 **Automation Tasks**
### **1️⃣ Basic Script**
- Open a browser.
- Navigate to [noKodr](https://app-staging.nokodr.com/).

### **2️⃣ Signup Page Validation**
- Validate mandatory fields (Name, Email, Password, Confirm Password).
- Test valid and invalid inputs like -
   - Invalid email format.
   - Passwords not matching.
   - Missing fields.
   - Edge cases (special characters, long inputs).
- Verifying submission response -
   - Success message for valid inputs.
   - Error messages for invalid inputs.

### **3️⃣ Login Page Validation**
- Validate username and password fields.
- Test valid and invalid login attempts-
   - Incorrect credentials.
   - Blank fields.
   - Special characters in fields.
- Verify submission response
   - Successful login redirects to the dashboard.
   - Invalid login shows an error message.


### **4️⃣ Forgot Password Validation**
- Validate email field (mandatory check and format validation)
- Test valid and invalid email inputs -
   - Non-registered email.
   - Invalid email format.
   - Blank input.
- Verify response -
   - Success message for valid email.
   - Error message for invalid email.


## **Technologies used** ##
- [python](https://www.python.org/)
- [selenium](https://selenium-python.readthedocs.io/)

## License
This repo is licensed under the [MIT License](LICENSE).



