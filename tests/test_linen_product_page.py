import allure
from config.environment import Environment
from pages.linen_login_page import LoginPage
from pages.linen_search_page import Search_Bar
from pages.linen_product_page import ProductPage
from tests.base_test import BaseTest
from  time import sleep

@allure.feature("Add Product To Bag")
class Test_Add_To_Bag(BaseTest):

    @allure.title("Login, Search Product and Add to Bag")
    def test_add_product_to_bag(self):

        env = Environment("Linen")

        self.driver.get(env.get_base_url())
        sleep(5)

        login = LoginPage(self.driver)
        login.login(
            env.get_username(),
            env.get_password()
        )
        sleep(5)

        search = Search_Bar(self.driver)
        search.search_product("Shirts")
        sleep(5)

        product = ProductPage(self.driver)
        sleep(4)

        product.select_product()
        sleep(10)