import allure
from config.environment import Environment
from pages.linen_login_page import LoginPage
from pages.linen_search_page import Search_Bar
from tests.base_test import BaseTest
from time import sleep


@allure.feature("Product Search")
class Test_Search_Page(BaseTest):

    @allure.title("Verify user can login and search for a product")
    def test_login_and_search(self):

        env = Environment("Linen")

        # Open application
        self.driver.get(env.get_base_url())

        # Login
        login = LoginPage(self.driver)
        login.login(
            env.get_username(),
            env.get_password()
        )
        sleep(10)
        # Search Product
        search = Search_Bar(self.driver)
        sleep(5)
        search.search_product("Shirts")