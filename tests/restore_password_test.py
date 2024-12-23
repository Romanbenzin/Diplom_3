import allure

from data.static_data import LOGIN_TEXT, MY_EMAIL, MY_PASSWORD


class TestRestorePassword:


    @allure.title("Тест: переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_restore_password(self, main, login, forgot_password):
        forgot_password.click_on_personal_account_button()
        login.waiting_register_button_to_click()
        login.click_recover_password_button_to()

        text_in_field = forgot_password.text_login_button()
        assert text_in_field == LOGIN_TEXT

    @allure.title("Тест: ввод почты и клик по кнопке «Восстановить»")
    def test_open_reset_pass_page(self, login, forgot_password, reset_password):
        forgot_password.click_on_personal_account_button()
        login.waiting_register_button_to_click()
        login.click_recover_password_button_to()
        forgot_password.input_email(MY_EMAIL)
        forgot_password.click_reset_button()
        reset_password.waiting_second_field_to_visible()

        text_in_field = reset_password.text_second_field()
        assert text_in_field == "Введите код из письма"

    @allure.title("Тест: клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    def test_check_hidden_pass(self, login, reset_password, forgot_password):
        forgot_password.click_on_personal_account_button()
        login.waiting_register_button_to_click()
        login.click_recover_password_button_to()
        forgot_password.input_email(MY_EMAIL)
        forgot_password.click_reset_button()
        reset_password.waiting_second_field_to_visible()
        reset_password.input_password(MY_PASSWORD)

        assert reset_password.attribute_type() == "password"
        reset_password.click_on_hidden_button()
        assert reset_password.attribute_type() == "text"
