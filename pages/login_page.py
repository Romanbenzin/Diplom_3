import allure

from data.locators import login_page_recover_password_button, forgot_page_email_field, \
    forgot_page_recover_button, reset_pass_page_field, reset_pass_hidden_button, reset_pass_pass_field, \
    reset_pass_second_field, reset_pass_save_button
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step("Клик по кнопке Восстановить пароль")
    def click_on_recover_password_button(self):
        self.driver.find_element(*login_page_recover_password_button).click()

class ForgotPassPage(LoginPage):
    @allure.step("Ввести почту в поле email")
    def input_email_recover(self, email):
        self.driver.find_element(*forgot_page_email_field).send_keys(email)

    @allure.step("Клик по кнопке Восстановить")
    def click_recover_password(self):
        self.driver.find_element(*forgot_page_recover_button).click()

    @allure.step("Клик по кнопке Восстановить")
    def click_recover_password_reset_button(self):
        self.driver.find_element(*reset_pass_save_button).click()

class ResetPassword(ForgotPassPage):
    @allure.step("Ввести пароль в поле Пароль")
    def input_password(self, password):
        self.driver.find_element(*reset_pass_page_field).send_keys(password)

    @allure.step("Кликнуть на глазик для открытия пароля")
    def click_on_hidden_button(self):
        self.driver.find_element(*reset_pass_hidden_button).click()

    @allure.step("Получить тип скрытого поля пароля")
    def attribute_type(self):
        return self.driver.find_element(*reset_pass_pass_field).get_attribute("type")

    @allure.step("Тест из второго поля восстановления пароля")
    def text_second_pass_field(self):
        return self.driver.find_element(*reset_pass_second_field).text
