import time

import allure
import pytest

from conftest import driver
from data.locators import login_page_login_button, main_page_personal_account, main_page_make_burger_text, \
    main_page_order_button, personal_account_profile_button, personal_account_history_button, modal_loader, \
    modal_ingredient, ingredient, create_order_modal, login_page_recover_password_button
from data.static_data import MY_EMAIL, MY_PASSWORD
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("driver")
@pytest.mark.usefixtures("main_func")
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
        WebDriverWait(driver, 60).until(expected_conditions.invisibility_of_element_located(modal_loader))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/feed"

    @allure.title("Тест: если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_click_on_ingredient(self, driver, main_func):
        main_func.click_on_ingredient()
        WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located(modal_ingredient))

        assert main_func.text_calories() == "Калории,ккал"

    @allure.title("Тест: закрытие модалки")
    def test_close_ingredient_modal(self, driver, main_func):
        main_func.click_on_ingredient()
        main_func.close_modal_ingredient()
        WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable(main_page_order_button))

        assert main_func.text_burger() == "Соберите бургер"

    @allure.title("Тест: при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента")
    def test_ingredient_add(self, driver, main_func):
        main_func.move_and_drop()

        assert main_func.counter_bun() == "2"

    @allure.title("Тест: залогиненный пользователь может оформить заказ")
    def test_create_order(self, driver, main_func):
        WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable(ingredient))
        main_func.move_and_drop()
        WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable(main_page_order_button))
        main_func.click_order_button()
        WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable(login_page_recover_password_button))
        main_func.input_email(MY_EMAIL)
        main_func.input_password(MY_PASSWORD)
        main_func.click_login_button()
        WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable(main_page_order_button))
        main_func.click_order_button()
        WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located(create_order_modal))

        assert main_func.prepareding_order() == "Ваш заказ начали готовить"

