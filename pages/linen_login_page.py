#Performs a full login action using methods inherited from BasePage.

from pages.base_page import BasePage

class LoginPage(BasePage):

    account_link = ("id", "login-form-link")
    email_input = ("id", "email-popup-login")
    password_input = ("id", "popup-login-password")
    login_button = ("id", "popup-ajax-login-btn")

    def __init__(self, driver):
        super().__init__(driver)

    def click_account_link(self):
        self.click(self.account_link)

    def enter_email(self, email):
        self.send_keys(self.email_input, email)

    def enter_password(self, password):
        self.send_keys(self.password_input, password)

    def click_login_button(self):
        self.click(self.login_button)

    def login(self, email, password):
        self.click_account_link()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
    