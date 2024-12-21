import allure
import pytest

from data.static_data import LOGIN_TEXT, MY_EMAIL, MY_PASSWORD
from data.locators import forgot_page_login_button, reset_pass_second_field, login_page_login_button, \
    login_page_recover_password_button, forgot_page_email_field, forgot_page_recover_button, reset_pass_save_button, \
    reset_pass_page_field


@pytest.mark.usefixtures("recover_password")
class TestRestorePassword:

    @allure.title("Тест: переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_restore_password(self, recover_password):
        recover_password.click_on_login_to_account()
        recover_password.waiting_object_to_be_clickable(login_page_login_button)
        recover_password.click_on_button(login_page_recover_password_button)

        text_in_field = recover_password.return_locator_text(forgot_page_login_button)
        assert text_in_field == LOGIN_TEXT

    @allure.title("Тест: ввод почты и клик по кнопке «Восстановить»")
    def test_open_reset_pass_page(self, recover_password):
        recover_password.click_on_login_to_account()
        recover_password.waiting_object_to_be_clickable(login_page_login_button)
        recover_password.click_on_button(login_page_recover_password_button)
        recover_password.input_data_in_field(forgot_page_email_field, MY_EMAIL)
        recover_password.click_on_button(reset_pass_save_button)
        recover_password.waiting_object_to_visible(reset_pass_second_field)

        text_in_field = recover_password.return_locator_text(reset_pass_second_field)
        assert text_in_field == "Введите код из письма"

    @allure.title("Тест: клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    def test_check_hidden_pass(self, recover_password):
        recover_password.click_on_login_to_account()
        recover_password.waiting_object_to_be_clickable(login_page_login_button)
        recover_password.click_on_button(login_page_recover_password_button)
        recover_password.input_data_in_field(forgot_page_email_field, MY_EMAIL)
        recover_password.click_on_button(forgot_page_recover_button)
        recover_password.waiting_object_to_visible(reset_pass_second_field)
        recover_password.input_data_in_field(reset_pass_page_field, MY_PASSWORD)

        assert recover_password.attribute_type() == "password"
        recover_password.click_on_hidden_button()
        assert recover_password.attribute_type() == "text"
