import time

import allure
import pytest

from conftest import driver
from data.locators import login_page_login_button, main_page_personal_account, main_page_make_burger_text, \
    main_page_order_button, personal_account_profile_button, personal_account_history_button, modal_loader, \
    modal_ingredient
from data.static_data import MY_EMAIL, MY_PASSWORD
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("driver")
@pytest.mark.usefixtures("personal_account")
class TestMainFunctional:

    @allure.title("Тест: переход по клику на «Конструктор»")
    def test_click_on_constructor(self, driver, main_func):
        main_func.click_on_personal_account_button()
        main_func.click_on_constructor()

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    @allure.title("Тест: переход по клику на «Лента заказов»")
    def test_click_on_feed(self, driver, main_func):
        main_func.click_on_personal_account_button()
        main_func.click_on_feed()
        WebDriverWait(driver, 10).until(expected_conditions.invisibility_of_element_located(modal_loader))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/feed"

    @allure.title("Тест: если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_click_on_ingredient(self, driver, main_func):
        main_func.click_on_ingredient()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(modal_ingredient))

        assert main_func.text_calories() == "Калории,ккал"

