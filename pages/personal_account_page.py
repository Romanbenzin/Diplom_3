import allure

from data.locators import login_page_email_field, login_page_password_field, \
    login_page_login_button, personal_account_history_button, personal_account_exit_button
from pages.base_page import BasePage

class PersonalAccountPage(BasePage):
    @allure.step("Заполнение поля email")
    def input_email(self, email):
        self.driver.find_element(*login_page_email_field).send_keys(email)

    @allure.step("Заполнение поля email")
    def input_password(self, password):
        self.driver.find_element(*login_page_password_field).send_keys(password)

    @allure.step("Клик по кнопке войти")
    def click_login_button(self):
        self.driver.find_element(*login_page_login_button).click()

    @allure.step("Клик по кнопке История заказов")
    def click_history_button(self):
        self.driver.find_element(*personal_account_history_button).click()

    @allure.step("Клик по кнопке Выход")
    def click_exit_button(self):
        self.driver.find_element(*personal_account_exit_button).click()
