import allure
import pytest
from selenium import webdriver

from config_for_driver import browser_name
from data.url import URL_MAIN_PAGE, URL_LOGIN_PAGE
from pages.base_page import BasePage
from pages.feed_page import FeedPage
from pages.login_page import ResetPassword
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage


class WebDriveFactory:
    @staticmethod
    def get_web_driver(browser):
        if browser == "fifefox":
            return webdriver.Firefox()
        elif browser == "chrome":
            return webdriver.Chrome()
        else:
            print("Для такого браузера нет драйвера")

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
@allure.step("Открытие главной страницы")
def recover_password(driver):
    return ResetPassword(driver)

@pytest.fixture()
@allure.step("Открытие главной страницы")
def personal_account(driver):
    return PersonalAccountPage(driver)

@pytest.fixture()
@allure.step("Открытие главной страницы")
def main_func(driver):
    return MainPage(driver)

@pytest.fixture()
@allure.step("Открытие главной страницы")
def feed_order(driver):
    return FeedPage(driver)

