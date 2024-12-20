import allure

from data.locators import login_page_recover_password_button, forgot_page_email_field, \
    forgot_page_recover_button, reset_pass_page_field, reset_pass_hidden_button, reset_pass_pass_field, \
    reset_pass_second_field, main_page_order_button, first_order
from pages.base_page import BasePage

class FeedPage(BasePage):
    @allure.step("Клик по кнопке Восстановить пароль")
    def click_on_first_order(self):
        self.driver.find_element(*first_order).click()
