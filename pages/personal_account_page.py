import allure

from data.locators import personal_account_history_button, personal_account_exit_button, login_page_login_button, \
    main_page_personal_account
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):

    @allure.step("Клик по кнопке личный кабинет")
    def click_on_personal_account_button(self):
        self.click_on_element(main_page_personal_account)

    @allure.step("Клик по кнопке История заказов")
    def click_history_button(self):
        self.click_on_element(personal_account_history_button)

    @allure.step("Клик по кнопке Выход")
    def click_exit_button(self):
        self.click_on_element(personal_account_exit_button)

    @allure.step("Ожидание появление кнопки Сохранить")
    def waiting_save_button_to_visible(self):
        self.waiting_element_to_visibility(login_page_login_button)

    @allure.step("Ожидание, когда кнопка выхода станет кликабельной")
    def waiting_recover_password_button_to_click(self):
        self.waiting_element_to_be_clickable(personal_account_exit_button)
