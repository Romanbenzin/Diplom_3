import allure
import pytest

from conftest import test_user_create
from data.locators import login_page_login_button, main_page_order_button, register_button_in_personal_account, \
    personal_account_exit_button, login_page_email_field, login_page_password_field
from data.urls import URL_LOGIN_PAGE, URL_ORDER_HISTORY


@pytest.mark.usefixtures("personal_account")
class TestRestorePassword:

    @allure.title("Тест: переход по клику на «Личный кабинет»")
    def test_restore_password(self, personal_account):
        personal_account.click_on_login_to_account()

        locator_text = personal_account.return_locator_text(login_page_login_button)
        assert locator_text == "Войти"

    @allure.title("Тест: переход в раздел «История заказов»")
    def test_orders_history(self, personal_account, test_user_create):
        user_data = next(test_user_create)
        # Авторизация
        personal_account.click_on_login_to_account()
        personal_account.input_data_in_field(login_page_email_field, user_data["email"])
        personal_account.input_data_in_field(login_page_password_field, user_data["password"])
        personal_account.click_on_button(login_page_login_button)
        # Нужна пауза
        personal_account.waiting_object_to_visible(main_page_order_button)
        personal_account.click_on_login_to_account()
        # Нужна пауза
        personal_account.waiting_object_to_visible(login_page_login_button)
        personal_account.click_history_button()

        current_url = personal_account.check_current_url()
        assert current_url == URL_ORDER_HISTORY

    @allure.title("Тест: выход из аккаунта")
    def test_logout(self, personal_account, test_user_create):
        user_data = next(test_user_create)
        # Авторизация
        personal_account.click_on_login_to_account()
        personal_account.input_data_in_field(login_page_email_field, user_data["email"])
        personal_account.input_data_in_field(login_page_password_field, user_data["password"])
        personal_account.click_on_button(login_page_login_button)
        # Нужна пауза
        personal_account.waiting_object_to_be_clickable(login_page_login_button)
        personal_account.click_on_login_to_account()
        # Нужна пауза
        personal_account.waiting_object_to_be_clickable(personal_account_exit_button)
        # Логаут
        personal_account.click_exit_button()
        # Нужна пауза
        personal_account.waiting_object_to_be_clickable(register_button_in_personal_account)

        current_url = personal_account.check_current_url()
        assert current_url == URL_LOGIN_PAGE
