import allure
from config.environment import Environment
from tests.base_test import BaseTest
from time import sleep
from pages.linen_login_page import LoginPage
from pages.linen_search_page import Search_Bar
from pages.linen_product_page import ProductPage
from pages.linen_Bag_page import Bag_Linen_Page


@allure.feature("Removing Product")
class Test_Bag_Linen_Page(BaseTest):

    @allure.title("login,search ,product and add to bag and then remove from bag")
    def test_bag_page(self):
        env=Environment("Linen")
        self.driver.get(env.get_base_url())

        login = LoginPage(self.driver)

        login.login(
            env.get_username(),
            env.get_password()
        )

        search = Search_Bar(self.driver)
        search.search_product("Shirts")
        sleep(5)

        product = ProductPage(self.driver)
        product.select_product()
        sleep(5)

        remove_bag=Bag_Linen_Page(self.driver)
        remove_bag.bag()
        sleep(5)
