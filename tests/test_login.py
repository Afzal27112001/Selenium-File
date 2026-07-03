from config.environment import Environment
from pages.login_page import LoginPage
from tests.base_test import BaseTest

class TestIndusLogin(BaseTest):
    def test_successful_login(self):
        login_page = LoginPage(self.driver)
        env = Environment()  # Uses ENV=demo by default if not set
        base_url = env.get_base_url()
        username = env.get_username()
        password = env.get_password()

