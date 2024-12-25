import allure

from data.locators import forgot_page_login_button, forgot_page_email_field, reset_pass_save_button, \
    main_page_personal_account
from pages.base_page import BasePage


class ForgotPassword(BasePage):

    @allure.step("Клик по кнопке личный кабинет")
    def click_on_personal_account_button(self):
        self.click_on_element(main_page_personal_account)

    @allure.step("Клик по кнопке личный кабинет")
    def click_on_personal_account_button(self):
        self.click_on_element(main_page_personal_account)

    @allure.step("Текст кнопки Войти")
    def text_login_button(self):
        return self.return_text(forgot_page_login_button)

    @allure.step("Ввод email")
    def input_email(self, email):
        self.input_data(forgot_page_email_field, email)

    @allure.step("Клик по кнопке Восстановить")
    def click_reset_button(self):
        self.click_on_element(reset_pass_save_button)
