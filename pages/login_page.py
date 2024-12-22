import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data.locators import login_page_recover_password_button, login_page_email_field, login_page_password_field, login_page_login_button, register_button_in_personal_account
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step("Ожидание, когда будет доступна для клика кнопка Восстановить пароль")
    def waiting_recover_password_button_to_click(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(login_page_recover_password_button))

    @allure.step("Клик по кнопке Восстановить пароль")
    def click_recover_password_button_to(self):
        self.driver.find_element(*login_page_recover_password_button).click()

    @allure.step("Ввод email")
    def input_email(self, email):
        self.driver.find_element(*login_page_email_field).send_keys(email)

    @allure.step("Ввод пароля")
    def input_password(self, password):
        self.driver.find_element(*login_page_password_field).send_keys(password)

    @allure.step("Клик по кнопке Войти")
    def click_login_button(self):
        self.driver.find_element(*login_page_login_button).click()

    @allure.step("Текст кнопки Войти")
    def text_login_button(self):
        return self.driver.find_element(*login_page_login_button).text

    @allure.step("Ожидание, когда будет доступна Зарегистрироваться")
    def waiting_register_button_to_click(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(register_button_in_personal_account))
