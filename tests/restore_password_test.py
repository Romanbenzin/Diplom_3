import allure
import pytest

from conftest import driver
from data.static_data import LOGIN_TEXT, MY_EMAIL
from data.locators import forgot_page_login_button


@pytest.mark.usefixtures("driver")
@pytest.mark.usefixtures("recover_password")
class TestRestorePassword:

    driver = None

    @allure.title("Тест: переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_restore_password(self, driver, recover_password):
        recover_password.click_on_login_to_account()
        recover_password.click_on_recover_password_button()

        login_text = driver.find_element(*forgot_page_login_button).text

        assert login_text == LOGIN_TEXT

    @allure.title("Тест: ввод почты и клик по кнопке «Восстановить»")
    def test_open_reset_pass_page(self, driver, recover_password):
        recover_password.click_on_login_to_account()
        recover_password.click_on_recover_password_button()
        recover_password.input_email_recover(MY_EMAIL)
        recover_password.click_recover_password()

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/reset-password"

    @allure.title("Тест: клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    def test_check_hidden_pass(self, driver, recover_password):
        recover_password.click_on_login_to_account()
        recover_password.click_on_recover_password_button()
        recover_password.input_email_recover(MY_EMAIL)
        recover_password.click_recover_password()

        recover_password.input_password("hidden_password")

        assert recover_password.attrebute_type() == "password"
        recover_password.click_on_hidden_button()
        assert recover_password.attrebute_type() == "text"



