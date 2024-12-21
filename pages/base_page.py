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

    @allure.step("Ожидание исчезновения объекта")
    def waiting_object_to_disappear(self, locator):
        WebDriverWait(self.driver, 20).until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step("Ожидание появление объекта")
    def waiting_object_to_visible(self, locator):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step("Ожидание и проверка, что объект есть на странице")
    def waiting_object_present_on_page(self, locator):
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(locator))

    @allure.step("Ожидание, что элемент стал кликабельным")
    def waiting_object_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(locator))

    @allure.step("Проверка текущего url")
    def check_current_url(self):
        return self.driver.current_url

    @allure.step("Получить текст локатора")
    def return_locator_text(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step("Сделать клик")
    def click_on_button(self, button):
        self.driver.find_element(*button).click()

    @allure.step("Ввести в поле данные")
    def input_data_in_field(self, locator, input_data):
        self.driver.find_element(*locator).send_keys(input_data)
