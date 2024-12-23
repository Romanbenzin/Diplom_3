import allure

from data.locators import modal_loader, main_page_personal_account
from pages.base_page import BasePage


class AccountProfile(BasePage):

    @allure.step("Клик по кнопке личный кабинет")
    def click_on_personal_account_button(self):
        self.click_on_element(main_page_personal_account)

    @allure.step("Ожидание исчезновения модального окна")
    def waiting_modal_loader_to_disappear(self):
        self.waiting_element_to_invisibility(modal_loader)
