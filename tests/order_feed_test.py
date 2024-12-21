import allure
import pytest
from data.locators import text_feed_order, ingredient, main_page_order_button, login_page_recover_password_button, \
    create_order_modal, wait_order_number_modal, find_order_number_in_list, order_in_work, order_number_field, \
    first_order, text_field_in_modal, login_page_email_field, login_page_password_field, login_page_login_button


@pytest.mark.usefixtures("feed_order")
class TestOrderFeed:

    @allure.title("Тест: если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_click_order(self, feed_order):
        feed_order.waiting_object_to_be_clickable(ingredient)
        feed_order.click_on_feed()
        feed_order.waiting_object_to_visible(text_feed_order)
        feed_order.click_on_button(first_order)

        text_modal = feed_order.return_locator_text(text_field_in_modal)
        assert "i-GMT+3" in text_modal

    @allure.title("Тест: заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_check_order_create(self, feed_order, test_user_create):
        user_data = next(test_user_create)
        feed_order.waiting_object_to_be_clickable(ingredient)
        feed_order.move_and_drop()
        feed_order.waiting_object_to_be_clickable(main_page_order_button)
        feed_order.click_on_button(main_page_order_button)
        feed_order.waiting_object_to_be_clickable(login_page_recover_password_button)
        feed_order.input_data_in_field(login_page_email_field, user_data["email"])
        feed_order.input_data_in_field(login_page_password_field, user_data["password"])
        feed_order.click_on_button(login_page_login_button)
        feed_order.waiting_object_to_be_clickable(main_page_order_button)
        feed_order.click_on_button(main_page_order_button)
        feed_order.waiting_object_to_visible(create_order_modal)
        feed_order.waiting_object_to_visible(wait_order_number_modal)
        order_number = feed_order.return_locator_text(order_number_field)
        feed_order.click_close_modal_order()
        # Переход на страницу Лента заказов
        feed_order.click_on_feed()
        feed_order.waiting_object_present_on_page(find_order_number_in_list)

        assert feed_order.find_order(order_number) == "Заказ есть в ленте"

    @allure.title("Тест: при создании нового заказа счётчик Выполнено за всё время увеличивается")
    def test_check_all_counter(self, feed_order, test_user_create):
        user_data = next(test_user_create)
        feed_order.click_on_feed()
        feed_order.waiting_object_to_visible(find_order_number_in_list)
        count_before_order = feed_order.total_count()
        feed_order.click_on_constructor()
        feed_order.waiting_object_to_be_clickable(ingredient)
        feed_order.move_and_drop()
        feed_order.waiting_object_to_be_clickable(main_page_order_button)
        feed_order.click_on_button(main_page_order_button)
        feed_order.waiting_object_to_be_clickable(login_page_recover_password_button)
        feed_order.input_data_in_field(login_page_email_field, user_data["email"])
        feed_order.input_data_in_field(login_page_password_field, user_data["password"])
        feed_order.click_on_button(login_page_login_button)
        feed_order.waiting_object_to_be_clickable(main_page_order_button)
        feed_order.click_on_button(main_page_order_button)
        feed_order.waiting_object_to_visible(create_order_modal)
        feed_order.waiting_object_to_visible(wait_order_number_modal)
        feed_order.click_close_modal_order()
        feed_order.click_on_feed()
        feed_order.waiting_object_present_on_page(find_order_number_in_list)
        count_after_order = feed_order.total_count()

        assert count_after_order > count_before_order

    @allure.title("Тест: при создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_check_today_counter(self, feed_order, test_user_create):
        user_data = next(test_user_create)
        feed_order.click_on_feed()
        feed_order.waiting_object_to_visible(find_order_number_in_list)
        count_before_order = feed_order.today_count()
        feed_order.click_on_constructor()
        feed_order.waiting_object_to_be_clickable(ingredient)
        feed_order.move_and_drop()
        feed_order.waiting_object_to_be_clickable(main_page_order_button)
        feed_order.click_on_button(main_page_order_button)
        feed_order.waiting_object_to_be_clickable(login_page_recover_password_button)
        feed_order.input_data_in_field(login_page_email_field, user_data["email"])
        feed_order.input_data_in_field(login_page_password_field, user_data["password"])
        feed_order.click_on_button(login_page_login_button)
        feed_order.waiting_object_to_be_clickable(main_page_order_button)
        feed_order.click_on_button(main_page_order_button)
        feed_order.waiting_object_to_visible(create_order_modal)
        feed_order.waiting_object_to_visible(wait_order_number_modal)
        feed_order.click_close_modal_order()
        feed_order.click_on_feed()
        feed_order.waiting_object_present_on_page(find_order_number_in_list)
        count_after_order = feed_order.today_count()

        assert count_after_order > count_before_order

    @allure.title("Тест: заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_check_order_in_work_status(self, feed_order, test_user_create):
        user_data = next(test_user_create)
        feed_order.waiting_object_to_be_clickable(ingredient)
        feed_order.move_and_drop()
        feed_order.waiting_object_to_be_clickable(main_page_order_button)
        feed_order.click_on_button(main_page_order_button)
        feed_order.waiting_object_to_be_clickable(login_page_recover_password_button)
        feed_order.input_data_in_field(login_page_email_field, user_data["email"])
        feed_order.input_data_in_field(login_page_password_field, user_data["password"])
        feed_order.click_on_button(login_page_login_button)
        feed_order.waiting_object_to_be_clickable(main_page_order_button)
        feed_order.click_on_button(main_page_order_button)
        feed_order.waiting_object_to_visible(create_order_modal)
        feed_order.waiting_object_to_visible(wait_order_number_modal)
        order_number = feed_order.return_locator_text(order_number_field)
        feed_order.click_close_modal_order()
        # Переход на страницу Лента заказов
        feed_order.click_on_feed()
        feed_order.waiting_object_present_on_page(text_feed_order)

        order_number_text = feed_order.return_locator_text(order_in_work)
        assert f"0{order_number}" == order_number_text
