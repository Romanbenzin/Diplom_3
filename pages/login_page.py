import allure

from data.locators import reset_pass_hidden_button, reset_pass_pass_field
from pages.base_page import BasePage


class ResetPassword(BasePage):

    @allure.step("Кликнуть на глазик для открытия пароля")
    def click_on_hidden_button(self):
        self.driver.find_element(*reset_pass_hidden_button).click()

    @allure.step("Получить тип скрытого поля пароля")
    def attribute_type(self):
        return self.driver.find_element(*reset_pass_pass_field).get_attribute("type")
