import allure
import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from data.locators import text_feed_order, ingredient, main_page_order_button, login_page_recover_password_button, create_order_modal, wait_order_number_modal, find_order_number_in_list


@pytest.mark.usefixtures("driver")
@pytest.mark.usefixtures("feed_order")
class TestOrderFeed:

    @allure.title("Тест: если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_click_order(self, driver, feed_order):
        WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable(ingredient))
        feed_order.click_on_feed()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(text_feed_order))
        feed_order.click_on_first_order()
        assert "i-GMT+3" in feed_order.text_on_modal_window()

    @allure.title("Тест: заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_check_order_create(self, driver, feed_order, test_user_create):
        user_data = next(test_user_create)
        WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable(ingredient))
        feed_order.move_and_drop()
        WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable(main_page_order_button))
        feed_order.click_order_button()
        WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable(login_page_recover_password_button))
        feed_order.input_email(user_data["email"])
        feed_order.input_password(user_data["password"])
        feed_order.click_login_button()
        WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable(main_page_order_button))
        feed_order.click_order_button()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(create_order_modal))
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(wait_order_number_modal))

        order_number = feed_order.order_number()
        feed_order.click_close_modal_order()
        # Переход на страницу Лента заказов
        feed_order.click_on_feed()
        WebDriverWait(driver, 20).until(expected_conditions.presence_of_element_located(find_order_number_in_list))
        assert feed_order.find_order(order_number) == "Заказ есть в ленте"

    @allure.title("Тест: при создании нового заказа счётчик Выполнено за всё время увеличивается")
    def test_check_all_counter(self, driver, feed_order, test_user_create):
        user_data = next(test_user_create)
        feed_order.click_on_feed()
        WebDriverWait(driver, 20).until(expected_conditions.presence_of_element_located(find_order_number_in_list))

        count_before_order = feed_order.total_count()

        feed_order.click_on_constructor()
        WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable(ingredient))
        feed_order.move_and_drop()
        WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable(main_page_order_button))
        feed_order.click_order_button()
        WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable(login_page_recover_password_button))
        feed_order.input_email(user_data["email"])
        feed_order.input_password(user_data["password"])
        feed_order.click_login_button()
        WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable(main_page_order_button))
        feed_order.click_order_button()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(create_order_modal))
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(wait_order_number_modal))
        feed_order.click_close_modal_order()
        feed_order.click_on_feed()
        WebDriverWait(driver, 20).until(expected_conditions.presence_of_element_located(find_order_number_in_list))

        count_after_order = feed_order.total_count()

        assert count_after_order > count_before_order

    @allure.title("Тест: при создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_check_today_counter(self, driver, feed_order, test_user_create):
        user_data = next(test_user_create)
        feed_order.click_on_feed()
        WebDriverWait(driver, 20).until(expected_conditions.presence_of_element_located(find_order_number_in_list))

        count_before_order = feed_order.today_count()

        feed_order.click_on_constructor()
        WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable(ingredient))
        feed_order.move_and_drop()
        WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable(main_page_order_button))
        feed_order.click_order_button()
        WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable(login_page_recover_password_button))
        feed_order.input_email(user_data["email"])
        feed_order.input_password(user_data["password"])
        feed_order.click_login_button()
        WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable(main_page_order_button))
        feed_order.click_order_button()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(create_order_modal))
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(wait_order_number_modal))
        feed_order.click_close_modal_order()
        feed_order.click_on_feed()
        WebDriverWait(driver, 20).until(expected_conditions.presence_of_element_located(find_order_number_in_list))

        count_after_order = feed_order.today_count()

        assert count_after_order > count_before_order

    @allure.title("Тест: заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_check_order_in_work_status(self, driver, feed_order, test_user_create):
        user_data = next(test_user_create)
        WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable(ingredient))
        feed_order.move_and_drop()
        WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable(main_page_order_button))
        feed_order.click_order_button()
        WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable(login_page_recover_password_button))
        feed_order.input_email(user_data["email"])
        feed_order.input_password(user_data["password"])
        feed_order.click_login_button()
        WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable(main_page_order_button))
        feed_order.click_order_button()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(create_order_modal))
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(wait_order_number_modal))

        order_number = feed_order.order_number()
        feed_order.click_close_modal_order()
        # Переход на страницу Лента заказов
        feed_order.click_on_feed()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(text_feed_order))

        assert f"0{order_number}" == feed_order.check_order_on_feed_orders()
