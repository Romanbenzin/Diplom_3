import allure

from data.locators import personal_account_history_button, personal_account_exit_button
from pages.base_page import BasePage

class PersonalAccountPage(BasePage):
    @allure.step("Клик по кнопке История заказов")
    def click_history_button(self):
        self.driver.find_element(*personal_account_history_button).click()

    @allure.step("Клик по кнопке Выход")
    def click_exit_button(self):
        self.driver.find_element(*personal_account_exit_button).click()
