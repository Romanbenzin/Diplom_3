import allure

from data.locators import reset_pass_hidden_button, reset_pass_pass_field, reset_pass_second_field, \
    reset_pass_page_field
from pages.base_page import BasePage


class ResetPassword(BasePage):

    @allure.step("Кликнуть на глазик для открытия пароля")
    def click_on_hidden_button(self):
        self.click_on_element(reset_pass_hidden_button)

    @allure.step("Получить тип скрытого поля пароля")
    def attribute_type(self):
        return self.return_type_of_locator(reset_pass_pass_field, "type")

    @allure.step("Ожидание появление второго поля")
    def waiting_second_field_to_visible(self):
        self.waiting_element_to_visibility(reset_pass_second_field)

    @allure.step("Текст второго поля")
    def text_second_field(self):
        return self.return_text(reset_pass_second_field)

    @allure.step("Ввести пароль")
    def input_password(self, password):
        self.input_data(reset_pass_page_field, password)
