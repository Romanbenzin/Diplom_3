import allure
import pytest
from selenium import webdriver

from data.url import URL_MAIN_PAGE
from pages.base_page import BasePage
from pages.login_page import ResetPassword


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()

    yield driver

    #Закрыть браузер:
    try:
        if driver:
            driver.quit()
    except Exception as e:
        print(f"Error closing driver: {e}")

@pytest.fixture()
@allure.step("Открытие главной страницы")
def open_main_page(driver):
    driver.get(URL_MAIN_PAGE)
    return ResetPassword(driver)

@pytest.fixture()
@allure.step("Открытие страницы заказов")
def open_order_page(driver):
    driver.get(URL_MAIN_PAGE)
    return BasePage(driver)
