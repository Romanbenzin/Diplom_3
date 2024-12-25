import allure

from data.locators import login_page_recover_password_button, login_page_email_field, login_page_password_field, login_page_login_button, register_button_in_personal_account
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step("Ожидание, когда будет доступна для клика кнопка Восстановить пароль")
    def waiting_recover_password_button_to_click(self):
        self.waiting_element_to_be_clickable(login_page_recover_password_button)

    @allure.step("Клик по кнопке Восстановить пароль")
    def click_recover_password_button_to(self):
        self.click_on_element(login_page_recover_password_button)

    @allure.step("Ввод email")
    def input_email(self, email):
        self.input_data(login_page_email_field, email)

    @allure.step("Ввод пароля")
    def input_password(self, password):
        self.input_data(login_page_password_field, password)

    @allure.step("Клик по кнопке Войти")
    def click_login_button(self):
        self.click_on_element(login_page_login_button)

    @allure.step("Текст кнопки Войти")
    def text_login_button(self):
        return self.return_text(login_page_login_button)

    @allure.step("Ожидание, когда будет доступна Зарегистрироваться")
    def waiting_register_button_to_click(self):
        self.waiting_element_to_be_clickable(register_button_in_personal_account)
