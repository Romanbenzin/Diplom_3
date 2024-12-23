import allure

from data.urls import URL_MAIN_PAGE, URL_ORDER_FEED

class TestMainFunctional:

    @allure.title("Тест: переход по клику на «Конструктор»")
    def test_click_on_constructor(self, main):
        main.click_on_personal_account_button()
        main.waiting_constructor_button_to_be_clickable()
        main.click_on_constructor()
        current_url = main.current_url()

        assert current_url == URL_MAIN_PAGE

    @allure.title("Тест: переход по клику на «Лента заказов»")
    def test_click_on_feed(self, main, account_profile):
        main.click_on_personal_account_button()
        main.click_on_feed()
        account_profile.waiting_modal_loader_to_disappear()
        current_url = main.current_url()

        assert current_url == URL_ORDER_FEED

    @allure.title("Тест: если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_click_on_ingredient(self, main):
        main.click_on_first_ingredient()

        assert main.text_calories() == "Калории,ккал"

    @allure.title("Тест: закрытие модалки")
    def test_close_ingredient_modal(self, main):
        main.click_on_first_ingredient()
        main.close_modal_ingredient()
        main.waiting_order_button_to_be_clickable()

        text_burger = main.return_make_burger_text()
        assert text_burger == "Соберите бургер"

    @allure.title("Тест: при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента")
    def test_ingredient_add(self, main):
        main.move_and_drop_bun()
        count_bun = main.return_count_ingredient_in_cart()
        assert count_bun == "2"

    @allure.title("Тест: залогиненный пользователь может оформить заказ")
    def test_create_order(self, main, login, test_user_create):
        user_data = next(test_user_create)
        main.waiting_ingredient_to_clickable()
        main.move_and_drop_bun()
        main.waiting_order_button_to_be_clickable()
        main.click_on_order_button()
        login.waiting_recover_password_button_to_click()
        login.input_email(user_data["email"])
        login.input_password(user_data["password"])
        login.click_login_button()
        main.waiting_ingredient_to_clickable()
        main.click_on_order_button()
        main.waiting_modal_after_order_create()

        prepare_order = main.text_modal_after_order_create()
        assert prepare_order == "Ваш заказ начали готовить"
