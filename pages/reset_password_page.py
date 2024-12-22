import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data.locators import reset_pass_hidden_button, reset_pass_pass_field, reset_pass_second_field, \
    reset_pass_page_field
from pages.base_page import BasePage


class ResetPassword(BasePage):

    @allure.step("Кликнуть на глазик для открытия пароля")
    def click_on_hidden_button(self):
        self.driver.find_element(*reset_pass_hidden_button).click()

    @allure.step("Получить тип скрытого поля пароля")
    def attribute_type(self):
        return self.driver.find_element(*reset_pass_pass_field).get_attribute("type")

    @allure.step("Ожидание появление второго поля")
    def waiting_second_field_to_visible(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(reset_pass_second_field))

    @allure.step("Текст второго поля")
    def text_second_field(self):
        return self.driver.find_element(*reset_pass_second_field).text

    @allure.step("Ввести пароль")
    def input_password(self, password):
        self.driver.find_element(*reset_pass_page_field).send_keys(password)
