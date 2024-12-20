import allure

from data.locators import main_page_personal_account, constructor_button, feed_order_button


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

