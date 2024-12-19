import allure
import pytest

from conftest import driver
from data.static_data import LOGIN_TEXT, MY_EMAIL
from locators import forgot_page_login_button


@pytest.mark.usefixtures("driver")
@pytest.mark.usefixtures("open_main_page")
class TestRestorePassword:

    driver = None

    @allure.title("Тест: переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_restore_password(self, driver, open_main_page):
        open_main_page.click_on_login_to_account()
        open_main_page.click_on_recover_password_button()

        login_text = driver.find_element(*forgot_page_login_button).text

        assert login_text == LOGIN_TEXT

    @allure.title("Тест: ввод почты и клик по кнопке «Восстановить»")
    def test_open_reset_pass_page(self, driver, open_main_page):
        open_main_page.click_on_login_to_account()
        open_main_page.click_on_recover_password_button()
        open_main_page.input_email_recover(MY_EMAIL)
        open_main_page.click_recover_password()

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/reset-password"

    @allure.title("Тест: клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    def test_open_reset_pass_page(self, driver, open_main_page):
        open_main_page.click_on_login_to_account()
        open_main_page.click_on_recover_password_button()
        open_main_page.input_email_recover(MY_EMAIL)
        open_main_page.click_recover_password()

        open_main_page.input_password("hidden_password")

        assert open_main_page.attrebute_type() == "password"
        open_main_page.click_on_hidden_button()
        assert open_main_page.attrebute_type() == "text"



