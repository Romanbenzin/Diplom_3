import allure
from selenium.webdriver import ActionChains

from data.locators import main_page_personal_account, constructor_button, feed_order_button
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Поиск элемента")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Поиск элементов")
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Клик по локатору")
    def click_on_element(self, locator):
        self.find_element(locator).click()

    @allure.step("Ожидание, что элемент станет кликабельным")
    def waiting_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(locator))

    @allure.step("Ожидание исчезновения объекта")
    def waiting_element_to_invisibility(self, locator):
        WebDriverWait(self.driver, 20).until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step("Ожидание появления объекта")
    def waiting_element_to_visibility(self, locator):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step("Ожидание, что элемент есть на странице")
    def waiting_element_to_presence(self, locator):
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(locator))

    @allure.step("Проверка текущего url")
    def check_current_url(self):
        return self.driver.current_url

    @allure.step("Ввести текст в поле")
    def input_data(self, locator, data):
        self.find_element(locator).send_keys(data)

    @allure.step("Получить текст элемента")
    def return_text(self, locator):
        return self.find_element(locator).text

    @allure.step("Зацепить, перенести и отпустить элемента")
    def move_and_drop_element(self, what, where):
        take = self.driver.find_element(*what)
        move = self.driver.find_element(*where)
        ActionChains(self.driver).drag_and_drop(take, move).perform()

    @allure.step("Получить тип локатора")
    def return_type_of_locator(self, locator, type_of_locator):
        return self.driver.find_element(*locator).get_attribute(type_of_locator)
