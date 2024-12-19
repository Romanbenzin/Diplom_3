import time

import allure
import pytest
from selenium.webdriver.common.by import By

from conftest import driver
from data.locators import login_page_login_button, main_page_personal_account, main_page_make_burger_text, \
    main_page_order_button, personal_account_profile_button, personal_account_history_button
from data.static_data import MY_EMAIL, MY_PASSWORD
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


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
        # Нужна пауза
        time.sleep(1)
        personal_account.click_on_login_to_account()

        # Ожидание закрытие модального окна:
        time.sleep(1)

        personal_account.click_history_button()
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/order-history"

    @allure.title("Тест: выход из аккаунта")
    def test_logout(self, driver, personal_account):
        # Авторизация
        personal_account.click_on_login_to_account()
        personal_account.input_email(MY_EMAIL)
        personal_account.input_password(MY_PASSWORD)
        personal_account.click_login_button()
        # Нужна пауза
        time.sleep(1)

        personal_account.click_on_login_to_account()

        # Ожидание закрытие модального окна:
        time.sleep(1)

        # Логаут
        personal_account.click_exit_button()

        # Нужна пауза
        time.sleep(1)
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
