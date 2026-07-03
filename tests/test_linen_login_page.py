from time import sleep
from config.environment import Environment
from pages.linen_login_page import LoginPage
from tests.base_test import BaseTest


class Test_login_Page(BaseTest):

    def test_successful_login(self):
        sleep(5)

        env = Environment("Linen")

        login_page = LoginPage(self.driver)

        login_page.navigate_to(env.get_base_url())

        login_page.login(
            env.get_username(),
            env.get_password()
        )
    sleep(9)