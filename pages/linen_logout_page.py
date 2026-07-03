from pages.base_page import BasePage
import allure

@allure.step("Logout")
class Linen_Logout_Page(BasePage):
    account_icon=('xpath','//a[@class="account-link"]')
    logout_button=('xpath','//a[@class="popup-logout-icon"]')

    def __init__(self, driver):
        super().__init__(driver)

    @allure.title("Performing logout")
    def logout(self):
        self.click(self.account_icon)
        self.click(self.logout_button)



