import allure
import pytest

from conftest import main_func


@pytest.mark.usefixtures("feed")
class TestOrderFeed:

    @allure.title("Тест: если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_click_order(self, feed, main_func):
        main_func.waiting_ingredient_to_clickable()
        feed.click_on_feed()
        feed.waiting_loader_end()
        feed.click_on_first_order()

        text_modal = feed.text_in_modal_order()
        assert "i-GMT+3" in text_modal

    @allure.title("Тест: заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_check_order_create(self, feed, main_func, login,test_user_create):
        user_data = next(test_user_create)
        main_func.waiting_ingredient_to_clickable()
        main_func.move_and_drop()
        main_func.waiting_order_button_to_be_clickable()
        main_func.click_on_order_button()
        login.waiting_recover_password_button_to_click()
        login.input_email(user_data["email"])
        login.input_password(user_data["password"])
        login.click_login_button()
        main_func.waiting_order_button_to_be_clickable()
        main_func.click_on_order_button()
        main_func.waiting_modal_after_order_create()
        main_func.waiting_close_modal_after_order_create()
        order_number = main_func.text_order_number()
        main_func.close_modal_after_order_create()
        # Переход на страницу Лента заказов
        feed.click_on_feed()
        feed.waiting_orders_on_page()

        assert feed.find_order(order_number) == "Заказ есть в ленте"

    @allure.title("Тест: при создании нового заказа счётчик Выполнено за всё время увеличивается")
    def test_check_all_counter(self, feed, main_func, login, test_user_create):
        user_data = next(test_user_create)
        feed.click_on_feed()
        feed.waiting_orders_on_page()
        count_before_order = int(feed.total_count())
        feed.click_on_constructor()
        main_func.waiting_ingredient_to_clickable()
        main_func.move_and_drop()
        main_func.waiting_order_button_to_be_clickable()
        main_func.click_on_order_button()
        login.waiting_recover_password_button_to_click()
        login.input_email(user_data["email"])
        login.input_password(user_data["password"])
        login.click_login_button()
        main_func.waiting_order_button_to_be_clickable()
        main_func.click_on_order_button()
        main_func.waiting_modal_after_order_create()
        main_func.waiting_close_modal_after_order_create()
        main_func.close_modal_after_order_create()
        feed.click_on_feed()
        feed.waiting_orders_on_page()
        count_after_order = int(feed.total_count())

        assert count_after_order > count_before_order

    @allure.title("Тест: при создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_check_today_counter(self, feed, main_func, login, test_user_create):
        user_data = next(test_user_create)
        feed.click_on_feed()
        feed.waiting_orders_on_page()
        count_before_order = int(feed.today_count())
        feed.click_on_constructor()
        main_func.waiting_ingredient_to_clickable()
        main_func.move_and_drop()
        main_func.waiting_order_button_to_be_clickable()
        main_func.click_on_order_button()
        login.waiting_recover_password_button_to_click()
        login.input_email(user_data["email"])
        login.input_password(user_data["password"])
        login.click_login_button()
        main_func.waiting_order_button_to_be_clickable()
        main_func.click_on_order_button()
        main_func.waiting_modal_after_order_create()
        main_func.waiting_close_modal_after_order_create()
        main_func.close_modal_after_order_create()
        feed.click_on_feed()
        feed.waiting_orders_on_page()
        count_after_order = int(feed.today_count())

        assert count_after_order > count_before_order

    @allure.title("Тест: заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_check_order_in_work_status(self, feed, main_func, login, test_user_create):
        user_data = next(test_user_create)
        main_func.waiting_ingredient_to_clickable()
        main_func.move_and_drop()
        main_func.waiting_order_button_to_be_clickable()
        main_func.click_on_order_button()
        login.waiting_recover_password_button_to_click()
        login.input_email(user_data["email"])
        login.input_password(user_data["password"])
        login.click_login_button()
        main_func.waiting_order_button_to_be_clickable()
        main_func.click_on_order_button()
        main_func.waiting_modal_after_order_create()
        main_func.waiting_close_modal_after_order_create()
        order_number = main_func.text_order_number()
        main_func.close_modal_after_order_create()
        # Переход на страницу Лента заказов
        feed.click_on_feed()
        feed.waiting_loader_end()

        order_number_text = feed.text_status_order_in_work()
        assert f"0{order_number}" == order_number_text
