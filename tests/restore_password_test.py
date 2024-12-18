import allure
from confest import driver
from data.data import URL_MAIN_PAGE


class TestRestorePassword:

    @allure.title("Тест: переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_restore_password(self, driver):
        driver.get(URL_MAIN_PAGE)
        assert driver.current_url == URL_MAIN_PAGE
