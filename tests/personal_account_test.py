import time

import allure
import pytest

from conftest import driver
from data.locators import login_page_login_button
from data.static_data import MY_EMAIL, MY_PASSWORD


@pytest.mark.usefixtures("driver")
@pytest.mark.usefixtures("personal_account")
class TestRestorePassword:

    driver = None
    @allure.title("Тест: переход по клику на «Личный кабинет»")
    def test_restore_password(self, driver, personal_account):
        personal_account.click_on_login_to_account()

        assert driver.find_element(*login_page_login_button).text == "Войти"

    @allure.title("Тест: переход в раздел «История заказов»")
    def test_orders_history(self, driver, personal_account):
        # Авторизация
        personal_account.click_on_login_to_account()
        personal_account.input_email(MY_EMAIL)
        personal_account.input_password(MY_PASSWORD)
        personal_account.click_login_button()

        personal_account.click_on_login_to_account()
        time.sleep(2)