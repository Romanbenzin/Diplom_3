import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data.locators import modal_loader
from pages.base_page import BasePage


class AccountProfile(BasePage):
    @allure.step("Ожидание исчезновения модального окна")
    def waiting_modal_loader_to_disappear(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.invisibility_of_element_located(modal_loader))
