import allure
from config.environment import Environment
from tests.base_test import BaseTest
from time import sleep
from pages.linen_login_page import LoginPage
from pages.linen_search_page import Search_Bar
from pages.linen_product_page import ProductPage
from pages.linen_Bag_page import Bag_Linen_Page
from pages.linen_logout_page import Linen_Logout_Page

class Test_Logout(BaseTest):


    @allure.title("Performing End to End Testing")
    def test_logout(self):

        env=Environment("Linen")
        self.driver.get(env.get_base_url())
        login = LoginPage(self.driver)
        sleep(4)
        login.login(
            env.get_username(),
            env.get_password()
        )
        sleep(2)

        search = Search_Bar(self.driver)
        search.search_product("Shirts")
        sleep(2)

        product = ProductPage(self.driver)
        product.select_product()
        sleep(2)

        remove_bag = Bag_Linen_Page(self.driver)
        remove_bag.bag()
        sleep(4)

        log=Linen_Logout_Page(self.driver)
        log.logout()
        sleep(2)

