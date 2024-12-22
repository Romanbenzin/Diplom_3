import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data.locators import ingredient, modal_ingredient_text, close_modal, move_place, main_page_order_button, \
    main_page_make_burger_text, counter_ingredient, create_order_modal, wait_order_number_modal, order_number_field, \
    close_modal_order
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Нажатие на кнопку Войти в аккаунт/Оформить заказ")
    def click_on_order_button(self):
        self.driver.find_element(*main_page_order_button).click()

    @allure.step("Клик на первый ингредиент на главной")
    def click_on_first_ingredient(self):
        self.driver.find_element(*ingredient).click()

    @allure.step("Ожидание, когда кнопка заказа будет доступна для клика")
    def waiting_order_button_to_be_clickable(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(main_page_order_button))

    @allure.step("Закрытие модального окна первого ингредиента")
    def close_modal_ingredient(self):
        self.driver.find_element(*close_modal).click()

    @allure.step("Получить текст локатора Соберите бургер")
    def return_make_burger_text(self):
        return self.driver.find_element(*main_page_make_burger_text).text

    @allure.step("Получение текста калории у модалки")
    def text_calories(self):
        return self.driver.find_element(*modal_ingredient_text).text

    @allure.step("Перенос булочки в заказ")
    def move_and_drop(self):
        take = self.driver.find_element(*ingredient)
        move = self.driver.find_element(*move_place)
        ActionChains(self.driver).drag_and_drop(take, move).perform()

    @allure.step("Получить Количество товара в корзине")
    def return_count_ingredient_in_cart(self):
        return self.driver.find_element(*counter_ingredient).text

    @allure.step("Ожидание, когда первый ингредиент станет кликабельным")
    def waiting_ingredient_to_clickable(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(ingredient))

    @allure.step("Ожидание появления модального окна после оформления заказа")
    def waiting_modal_after_order_create(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(create_order_modal))

    @allure.step("Текст успешности оформления заказа")
    def text_modal_after_order_create(self):
        return self.driver.find_element(*create_order_modal).text

    @allure.step("Ожидание закрытия модалки после оформления заказа")
    def waiting_close_modal_after_order_create(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(wait_order_number_modal))

    @allure.step("Получить номер заказа")
    def text_order_number(self):
        return self.driver.find_element(*order_number_field).text

    @allure.step("Закрыть модалку после оформления заказа")
    def close_modal_after_order_create(self):
        self.driver.find_element(*close_modal_order).click()
