import allure

from data.locators import forgot_page_login_button, forgot_page_email_field, reset_pass_save_button
from pages.base_page import BasePage


class ForgotPassword(BasePage):

    @allure.step("Текст кнопки Войти")
    def text_login_button(self):
        return self.driver.find_element(*forgot_page_login_button).text

    @allure.step("Ввод email")
    def input_email(self, email):
        self.driver.find_element(*forgot_page_email_field).send_keys(email)

    @allure.step("Клик по кнопке Восстановить")
    def click_reset_button(self):
        self.driver.find_element(*reset_pass_save_button).click()
