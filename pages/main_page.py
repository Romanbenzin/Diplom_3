import allure

from data.locators import login_page_email_field, login_page_password_field, \
    login_page_login_button, personal_account_history_button, personal_account_exit_button, ingredient, \
    modal_ingredient_text
from pages.base_page import BasePage

class MainPage(BasePage):
    @allure.step("Клик по ингредиенту")
    def click_on_ingredient(self):
        self.driver.find_element(*ingredient).click()

    @allure.step("Получение текста калории у модалки")
    def text_calories(self):
        return self.driver.find_element(*modal_ingredient_text).text
