from time import sleep


from locators.locators import LogInLocators
from utils.usefull_elements import SignIn


class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(LogInLocators.URL)
        sleep(3)

    def type_email(self, username):
        self.browser.find_element(*LogInLocators.login_email_box).send_keys(username)

    def type_password(self, password):
        self.browser.find_element(*LogInLocators.login_password_box).send_keys(password)

    def click_sign_in(self):
        sleep(3)
        self.browser.find_element(*LogInLocators.login_button).click()

    def get_error_message(self, error_type):
        if error_type == "login_error":
            return self.browser.find_element(*LogInLocators.login_error_message).text
        elif error_type == "email_error":
            return self.browser.find_element(*LogInLocators.email_error_message).text
        elif error_type == "password_error":
            return self.browser.find_element(*LogInLocators.password_error_message).text

    def set_user_inputs(self):
        self.browser.find_element(*LogInLocators.login_email_box).send_keys(SignIn.TEST_ACCOUNT)
        self.browser.find_element(*LogInLocators.login_password_box).send_keys(SignIn.TEST_PASSWORD)
        self.browser.find_element(*LogInLocators.login_button).click()

    def click_delivery_button(self):
        self.browser.find_element(*LogInLocators.delivery_button).click()
