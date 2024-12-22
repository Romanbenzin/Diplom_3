import allure
import pytest
import requests

from config_driver_selection import browser_name
from data.urls import URL_MAIN_PAGE, API_REGISTER, API_USER
from driver_selection import WebDriveFactory
from helpers import return_random_user_for_register
from pages.account_profile_page import AccountProfile
from pages.feed_page import FeedPage
from pages.forgot_password_page import ForgotPassword
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage
from pages.reset_password_page import ResetPassword


@pytest.fixture
@allure.step("Создание пользователя через api")
def test_user_create():
    random_user_for_register = return_random_user_for_register()
    response_create_user = requests.post(API_REGISTER, data=random_user_for_register)

    yield random_user_for_register

    # Удалить созданного через api пользователя
    data = {
        "Authorization": response_create_user.json()["accessToken"]
    }
    requests.delete(API_USER, headers=data)

@pytest.fixture(scope='function')
def driver():
    driver = WebDriveFactory.get_web_driver(browser_name)
    driver.get(URL_MAIN_PAGE)

    yield driver
    #Закрыть браузер:
    try:
        if driver:
            driver.quit()
    except Exception as e:
        print(f"Error closing driver: {e}")

@pytest.fixture()
@allure.step("Обращение к странице reset_password")
def reset_password(driver):
    return ResetPassword(driver)

@pytest.fixture()
@allure.step("Обращение к странице personal_account")
def personal_account(driver):
    return PersonalAccountPage(driver)

@pytest.fixture()
@allure.step("Обращение к странице main")
def main_func(driver):
    return MainPage(driver)

@pytest.fixture()
@allure.step("Обращение к странице feed")
def feed(driver):
    return FeedPage(driver)

@pytest.fixture()
@allure.step("Обращение к странице forgot_password")
def forgot_password(driver):
    return ForgotPassword(driver)

@pytest.fixture()
@allure.step("Обращение к странице account_profile")
def account_profile(driver):
    return AccountProfile(driver)

@pytest.fixture()
@allure.step("Открытие главной страницы")
def login(driver):
    return LoginPage(driver)
