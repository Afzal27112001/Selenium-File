import allure
from pages.base_page import BasePage
from time import sleep

class ProductPage(BasePage):

    first_product = ("xpath", "(//div[contains(@class,'product-item-info')])[1]")

    size_l = ("xpath", "//div[text()='L']")   # Verify this locator

    add_to_bag = ("xpath", "//button[@title='Add to Bag']")   # Verify this locator

    @allure.step("Click first product")
    # def click_first_product(self):
    #     self.click(self.first_product)
    #
    # @allure.step("Select Size L")
    # def select_size_l(self):
    #     self.click(self.size_l)
    #
    # @allure.step("Click Add to Bag")
    # def click_add_to_bag(self):
    #     self.click(self.add_to_bag)


    def select_product(self):
        self.click(self.first_product)
        sleep(2)
        self.click(self.size_l)
        sleep(2)
        self.click(self.add_to_bag)
        sleep(2)