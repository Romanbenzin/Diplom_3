import allure

from data.locators import ingredient, modal_ingredient_text, close_modal, move_place, main_page_order_button, \
    main_page_make_burger_text, counter_ingredient, create_order_modal, wait_order_number_modal, order_number_field, \
    close_modal_order, main_page_personal_account, constructor_button, feed_order_button
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Клик по кнопке личный кабинет")
    def click_on_personal_account_button(self):
        self.click_on_element(main_page_personal_account)

    @allure.step("Клик по ленте заказов")
    def click_on_feed(self):
        self.click_on_element(feed_order_button)

    @allure.step("Ожидание, когда кнопка конструктора будет кликабельна")
    def waiting_constructor_button_to_be_clickable(self):
        self.waiting_element_to_be_clickable(constructor_button)

    @allure.step("Получить текущий url")
    def current_url(self):
        return self.check_current_url()

    @allure.step("Клик по кнопке Конструктор")
    def click_on_constructor(self):
        self.click_on_element(constructor_button)

    @allure.step("Нажатие на кнопку Войти в аккаунт/Оформить заказ")
    def click_on_order_button(self):
        self.click_on_element(main_page_order_button)

    @allure.step("Клик на первый ингредиент на главной")
    def click_on_first_ingredient(self):
        self.click_on_element(ingredient)

    @allure.step("Ожидание, когда кнопка заказа будет доступна для клика")
    def waiting_order_button_to_be_clickable(self):
        self.waiting_element_to_be_clickable(main_page_order_button)

    @allure.step("Закрытие модального окна первого ингредиента")
    def close_modal_ingredient(self):
        self.click_on_element(close_modal)

    @allure.step("Получить текст локатора Соберите бургер")
    def return_make_burger_text(self):
        return self.return_text(main_page_make_burger_text)

    @allure.step("Получение текста калории у модалки")
    def text_calories(self):
        return self.return_text(modal_ingredient_text)

    @allure.step("Перенос булочки в заказ")
    def move_and_drop_bun(self):
        self.move_and_drop_element(ingredient, move_place)

    @allure.step("Получить Количество товара в корзине")
    def return_count_ingredient_in_cart(self):
        return self.return_text(counter_ingredient)

    @allure.step("Ожидание, когда первый ингредиент станет кликабельным")
    def waiting_ingredient_to_clickable(self):
        self.waiting_element_to_be_clickable(ingredient)

    @allure.step("Ожидание появления модального окна после оформления заказа")
    def waiting_modal_after_order_create(self):
        self.waiting_element_to_visibility(order_number_field)

    @allure.step("Текст успешности оформления заказа")
    def text_modal_after_order_create(self):
        return self.return_text(create_order_modal)

    @allure.step("Ожидание закрытия модалки после оформления заказа")
    def waiting_modal_after_order_create(self):
        self.waiting_element_to_visibility(wait_order_number_modal)

    @allure.step("Получить номер заказа")
    def text_order_number(self):
        return self.return_text(order_number_field)

    @allure.step("Закрыть модалку после оформления заказа")
    def close_modal_after_order_create(self):
        self.click_on_element(close_modal_order)
