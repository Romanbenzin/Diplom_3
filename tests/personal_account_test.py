import time

import allure
import pytest
from selenium.webdriver.common.by import By

from conftest import driver
from data.locators import login_page_login_button, main_page_personal_account, main_page_make_burger_text, \
    main_page_order_button, personal_account_profile_button, personal_account_history_button, modal_loader, \
    register_button_in_personal_account
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
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(main_page_order_button))
        personal_account.click_on_login_to_account()
        # Нужна пауза
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(login_page_login_button))
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
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(login_page_login_button))
        personal_account.click_on_login_to_account()
        # Нужна пауза
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(login_page_login_button))
        # Логаут
        personal_account.click_exit_button()
        # Нужна пауза
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(register_button_in_personal_account))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
