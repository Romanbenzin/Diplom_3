import time

import allure
import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver
from data.static_data import LOGIN_TEXT, MY_EMAIL
from data.locators import forgot_page_login_button, reset_pass_save_button, reset_pass_second_field, \
    login_page_login_button


@pytest.mark.usefixtures("driver")
@pytest.mark.usefixtures("recover_password")
class TestRestorePassword:

    driver = None

    @allure.title("Тест: переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_restore_password(self, driver, recover_password):
        recover_password.click_on_login_to_account()
        WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable(login_page_login_button))
        recover_password.click_on_recover_password_button()

        login_text = driver.find_element(*forgot_page_login_button).text

        assert login_text == LOGIN_TEXT

    @allure.title("Тест: ввод почты и клик по кнопке «Восстановить»")
    def test_open_reset_pass_page(self, driver, recover_password):
        recover_password.click_on_login_to_account()
        WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable(login_page_login_button))
        recover_password.click_on_recover_password_button()
        recover_password.input_email_recover(MY_EMAIL)
        recover_password.click_recover_password()
        WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located(reset_pass_second_field))
        assert recover_password.text_second_pass_field() == "Введите код из письма"

    @allure.title("Тест: клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    def test_check_hidden_pass(self, driver, recover_password):
        recover_password.click_on_login_to_account()
        WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable(login_page_login_button))
        recover_password.click_on_recover_password_button()
        recover_password.input_email_recover(MY_EMAIL)
        recover_password.click_recover_password()
        WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located(reset_pass_second_field))
        recover_password.input_password("hidden_password")

        assert recover_password.attribute_type() == "password"
        recover_password.click_on_hidden_button()
        assert recover_password.attribute_type() == "text"



