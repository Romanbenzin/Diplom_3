import allure

from data.locators import find_order_number_in_list, total_count_all_time, total_today_count, text_feed_order, \
    first_order, text_field_in_modal, order_in_work, main_page_personal_account, feed_order_button
from pages.base_page import BasePage


class FeedPage(BasePage):

    @allure.step("Клик по ленте заказов")
    def click_on_feed(self):
        self.click_on_element(feed_order_button)

    @allure.step("Клик по кнопке личный кабинет")
    def click_on_personal_account_button(self):
        self.click_on_element(main_page_personal_account)

    @allure.step("Ожидание и проверка, что заказы есть на странице")
    def waiting_orders_on_page(self):
        self.waiting_element_to_presence(find_order_number_in_list)

    @allure.step("Найти ордер в списке заказов")
    def find_order(self, order):
        order_numbers_list = self.find_elements(find_order_number_in_list)
        order_numbers = [number.text.strip() for number in order_numbers_list]
        if f"#0{order}" in order_numbers:
            return "Заказ есть в ленте"
        else:
            return "Заказа нет в ленте"

    @allure.step("Выполнено за все время")
    def total_count(self):
        return self.return_text(total_count_all_time)

    @allure.step("Выполнено за сегодня")
    def today_count(self):
        return self.return_text(total_today_count)

    @allure.step("Ожидание, когда пропадет модалка Загрузка")
    def waiting_loader_end(self):
        self.waiting_element_to_visibility(text_feed_order)

    @allure.step("Клик на верхний заказ")
    def click_on_first_order(self):
        self.click_on_element(first_order)

    @allure.step("Текст в модалке заказа")
    def text_in_modal_order(self):
        return self.return_text(text_field_in_modal)

    @allure.step("Текст номер заказа в статусе в работе")
    def text_status_order_in_work(self):
        return self.return_text(order_in_work)
