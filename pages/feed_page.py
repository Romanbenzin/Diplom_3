import allure

from data.locators import close_modal_order, find_order_number_in_list, total_count_all_time, total_today_count
from pages.main_page import MainPage


class FeedPage(MainPage):
    @allure.step("Клик закрытия модалки")
    def click_close_modal_order(self):
        self.driver.find_element(*close_modal_order).click()

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
