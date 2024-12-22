import allure

from data.locators import main_page_personal_account, constructor_button, feed_order_button
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Клик по кнопке Войти в аккаунт")
    def click_on_login_to_account(self):
        self.driver.find_element(*main_page_personal_account).click()

    @allure.step("Клик по кнопке Личный кабинет")
    def click_on_personal_account_button(self):
        self.driver.find_element(*main_page_personal_account).click()

    @allure.step("Клик по кнопке Конструктор")
    def click_on_constructor(self):
        self.driver.find_element(*constructor_button).click()

    @allure.step("Клик по кнопке Лента заказов")
    def click_on_feed(self):
        self.driver.find_element(*feed_order_button).click()

    @allure.step("Ожидание, что кнопка Конструктор станет кликабельна")
    def waiting_constructor_button_to_be_clickable(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(constructor_button))

    @allure.step("Проверка текущего url")
    def check_current_url(self):
        return self.driver.current_url
