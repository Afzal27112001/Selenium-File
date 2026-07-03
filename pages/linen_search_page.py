import allure
from pages.base_page import BasePage


class Search_Bar(BasePage):

    search_input = ("id", "minisearch-input-top-search")
    search_button = ("xpath", "//button[@title='Search']")   # Verify this locator

    @allure.step("Searching Product: {product_name}")
    def search_product(self, product_name):
        self.send_keys(self.search_input, product_name)
        self.click(self.search_button)