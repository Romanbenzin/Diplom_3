import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data.locators import main_page_login_button, main_page_personal_account, reset_pass_hidden_button


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Клик по кнопке Войти в аккаунт")
    def click_on_login_to_account(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(main_page_personal_account))
        self.driver.find_element(*main_page_personal_account).click()

    @allure.step("Клик по кнопке Личный кабинет")
    def click_on_personal_account_button(self):
        self.driver.find_element(*main_page_personal_account).click()
