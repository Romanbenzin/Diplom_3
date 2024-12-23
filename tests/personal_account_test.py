import allure

from data.urls import URL_LOGIN_PAGE, URL_ORDER_HISTORY


class TestRestorePassword:

    @allure.title("Тест: переход по клику на «Личный кабинет»")
    def test_restore_password(self, personal_account, login):
        personal_account.click_on_personal_account_button()

        locator_text = login.text_login_button()
        assert locator_text == "Войти"

    @allure.title("Тест: переход в раздел «История заказов»")
    def test_orders_history(self, personal_account, login, main, test_user_create):
        user_data = next(test_user_create)
        # Авторизация
        personal_account.click_on_personal_account_button()
        login.input_email(user_data["email"])
        login.input_password(user_data["password"])
        login.click_login_button()
        # Нужна пауза
        main.waiting_order_button_to_be_clickable()
        personal_account.click_on_personal_account_button()
        # Нужна пауза
        personal_account.waiting_save_button_to_visible()
        personal_account.click_history_button()

        current_url = personal_account.check_current_url()
        assert current_url == URL_ORDER_HISTORY

    @allure.title("Тест: выход из аккаунта")
    def test_logout(self, personal_account, login, main, test_user_create):
        user_data = next(test_user_create)
        # Авторизация
        personal_account.click_on_personal_account_button()
        login.input_email(user_data["email"])
        login.input_password(user_data["password"])
        login.click_login_button()
        # Нужна пауза
        main.waiting_order_button_to_be_clickable()
        personal_account.click_on_personal_account_button()
        # Нужна пауза
        personal_account.waiting_recover_password_button_to_click()
        # Логаут
        personal_account.click_exit_button()
        # Нужна пауза
        login.waiting_register_button_to_click()

        current_url = personal_account.check_current_url()
        assert current_url == URL_LOGIN_PAGE
