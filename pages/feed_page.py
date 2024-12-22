import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data.locators import find_order_number_in_list, total_count_all_time, total_today_count, text_feed_order, first_order, text_field_in_modal, order_in_work
from pages.base_page import BasePage


class FeedPage(BasePage):

    @allure.step("Ожидание и проверка, что заказы есть на странице")
    def waiting_orders_on_page(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(find_order_number_in_list))

    @allure.step("Найти ордер в списке заказов")
    def find_order(self, order):
        order_numbers_list = self.driver.find_elements(*find_order_number_in_list)
        order_numbers = [number.text.strip() for number in order_numbers_list]
        if f"#0{order}" in order_numbers:
            return "Заказ есть в ленте"
        else:
            return "Заказа нет в ленте"

    @allure.step("Выполнено за все время")
    def total_count(self):
        return self.driver.find_element(*total_count_all_time).text

    @allure.step("Выполнено за сегодня")
    def today_count(self):
        return self.driver.find_element(*total_today_count).text

    @allure.step("Ожидание, когда пропадет модалка Загрузка")
    def waiting_loader_end(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(text_feed_order))

    @allure.step("Клик на верхний заказ")
    def click_on_first_order(self):
        self.driver.find_element(*first_order).click()

    @allure.step("Текст в модалке заказа")
    def text_in_modal_order(self):
        return self.driver.find_element(*text_field_in_modal).text

    @allure.step("Текст в модалке заказа")
    def text_status_order_in_work(self):
        return self.driver.find_element(*order_in_work).text
