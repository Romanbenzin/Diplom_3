import allure
import pytest
from selenium import webdriver

from config_for_driver import browser_name
from data.url import URL_MAIN_PAGE
from pages.base_page import BasePage
from pages.login_page import ResetPassword
from pages.personal_account_page import PersonalAccountPage


class WebDriveFactory:
    @staticmethod
    def get_web_driver(browser):
        if browser == "fifefox":
            return webdriver.Firefox()
        elif browser == "chrome":
            return webdriver.Chrome()

@pytest.fixture(scope='function')
def driver():
    driver = WebDriveFactory.get_web_driver(browser_name)

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
    driver.get(URL_MAIN_PAGE)
    return ResetPassword(driver)

@pytest.fixture()
@allure.step("Открытие страницы заказов")
def personal_account(driver):
    driver.get(URL_MAIN_PAGE)
    return PersonalAccountPage(driver)
