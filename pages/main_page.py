import allure
from selenium.webdriver import ActionChains

from data.locators import ingredient, modal_ingredient_text, close_modal, move_place
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Закрытие модального окна")
    def close_modal_ingredient(self):
        self.driver.find_element(*close_modal).click()

    @allure.step("Получение текста калории у модалки")
    def text_calories(self):
        return self.driver.find_element(*modal_ingredient_text).text

    @allure.step("Перенос булочки в заказ")
    def move_and_drop(self):
        take = self.driver.find_element(*ingredient)
        move = self.driver.find_element(*move_place)
        ActionChains(self.driver).drag_and_drop(take, move).perform()
