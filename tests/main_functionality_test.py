import allure
import pytest

from conftest import main_func
from data.locators import main_page_order_button, modal_loader, modal_ingredient, ingredient, create_order_modal, \
    login_page_recover_password_button, constructor_button, login_page_password_field, \
    login_page_email_field, main_page_make_burger_text, counter_ingredient, login_page_login_button
from data.urls import URL_MAIN_PAGE, URL_ORDER_FEED


@pytest.mark.usefixtures("main_func")
class TestMainFunctional:

    @allure.title("Тест: переход по клику на «Конструктор»")
    def test_click_on_constructor(self, main_func):
        main_func.click_on_personal_account_button()
        main_func.waiting_object_to_be_clickable(constructor_button)
        main_func.click_on_constructor()
        current_url = main_func.check_current_url()

        assert current_url == URL_MAIN_PAGE

    @allure.title("Тест: переход по клику на «Лента заказов»")
    def test_click_on_feed(self, main_func):
        main_func.click_on_personal_account_button()
        main_func.click_on_feed()
        main_func.waiting_object_to_disappear(modal_loader)
        current_url = main_func.check_current_url()

        assert current_url == URL_ORDER_FEED

    @allure.title("Тест: если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_click_on_ingredient(self, main_func):
        main_func.click_on_button(ingredient)
        main_func.waiting_object_present_on_page(modal_ingredient)

        assert main_func.text_calories() == "Калории,ккал"

    @allure.title("Тест: закрытие модалки")
    def test_close_ingredient_modal(self, main_func):
        main_func.click_on_button(ingredient)
        main_func.close_modal_ingredient()
        main_func.waiting_object_to_be_clickable(main_page_order_button)

        text_burger = main_func.return_locator_text(main_page_make_burger_text)
        assert text_burger == "Соберите бургер"

    @allure.title("Тест: при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента")
    def test_ingredient_add(self, main_func):
        main_func.move_and_drop()

        count_bun = main_func.return_locator_text(counter_ingredient)
        assert count_bun == "2"

    @allure.title("Тест: залогиненный пользователь может оформить заказ")
    def test_create_order(self, main_func, test_user_create):
        user_data = next(test_user_create)
        main_func.waiting_object_to_be_clickable(ingredient)
        main_func.move_and_drop()
        main_func.waiting_object_to_be_clickable(main_page_order_button)
        main_func.click_on_button(main_page_order_button)
        main_func.waiting_object_to_be_clickable(login_page_recover_password_button)
        main_func.input_data_in_field(login_page_email_field, user_data["email"])
        main_func.input_data_in_field(login_page_password_field, user_data["password"])
        main_func.click_on_button(login_page_login_button)
        main_func.waiting_object_to_be_clickable(main_page_order_button)
        main_func.click_on_button(main_page_order_button)
        main_func.waiting_object_to_visible(create_order_modal)

        prepare_order = main_func.return_locator_text(create_order_modal)
        assert prepare_order == "Ваш заказ начали готовить"
