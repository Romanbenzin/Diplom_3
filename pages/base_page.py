import allure

from locators import main_page_login_button

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Клик по кнопке Войти в аккаунт")
    def click_on_login_to_account(self):
        self.driver.find_element(*main_page_login_button).click()
