import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data.locators import personal_account_history_button, personal_account_exit_button, login_page_login_button
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):

    @allure.step("Клик по кнопке История заказов")
    def click_history_button(self):
        self.driver.find_element(*personal_account_history_button).click()

    @allure.step("Клик по кнопке Выход")
    def click_exit_button(self):
        self.driver.find_element(*personal_account_exit_button).click()

    @allure.step("Ожидание появление кнопки Сохранить")
    def waiting_save_button_to_visible(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(login_page_login_button))

    @allure.step("Ожидание, когда кнопка выхода станет кликабельной")
    def waiting_recover_password_button_to_click(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(personal_account_exit_button))
