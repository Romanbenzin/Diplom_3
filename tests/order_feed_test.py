import time

import allure
import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver
from data.locators import text_feed_order, ingredient


@pytest.mark.usefixtures("driver")
@pytest.mark.usefixtures("feed_order")
class TestOrderFeed:

    @allure.title("Тест: если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_click_order(self, driver, feed_order):
        WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable(ingredient))
        feed_order.click_on_feed()
        WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located(text_feed_order))
        feed_order.click_on_first_order()
        time.sleep(2)

