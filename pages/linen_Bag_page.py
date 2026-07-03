from pages.base_page import BasePage
import allure
from time import sleep
class Bag_Linen_Page(BasePage):

    bag_link=("xpath","//div[@class='minicart-wrapper']")
    remove_item=("xpath","//a[@title='Remove item']")


    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("removing the product")
    def bag(self):
        self.click(self.bag_link)
        sleep(5)
        self.click(self.remove_item)
        sleep(5)

