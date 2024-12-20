import allure
from selenium.webdriver import ActionChains

from data.locators import login_page_email_field, login_page_password_field, \
    login_page_login_button, personal_account_history_button, personal_account_exit_button, ingredient, \
    modal_ingredient_text, close_modal, main_page_make_burger_text, move_place, counter_ingredient, \
    main_page_order_button, create_order_modal
from pages.personal_account_page import PersonalAccountPage


class MainPage(PersonalAccountPage):
    @allure.step("Клик по ингредиенту")
    def click_on_ingredient(self):
        self.driver.find_element(*ingredient).click()

    @allure.step("Закрытие модального окна")
    def close_modal_ingredient(self):
        self.driver.find_element(*close_modal).click()

    @allure.step("Получение текста калории у модалки")
    def text_calories(self):
        return self.driver.find_element(*modal_ingredient_text).text

    @allure.step("Получение текста Соберите Бургер")
    def text_burger(self):
        return self.driver.find_element(*main_page_make_burger_text).text

    @allure.step("Перенос булочки в заказ")
    def move_and_drop(self):
        take = self.driver.find_element(*ingredient)
        move = self.driver.find_element(*move_place)
        ActionChains(self.driver).drag_and_drop(take, move).perform()

    @allure.step("Узнать количество булочек в заказке")
    def counter_bun(self):
        return self.driver.find_element(*counter_ingredient).text

    @allure.step("Кнопку заказа на главной")
    def click_order_button(self):
        self.driver.find_element(*main_page_order_button).click()

    @allure.step("Текст Ваш заказ начали готовить")
    def prepareding_order(self):
        return self.driver.find_element(*create_order_modal).text
