from selenium import webdriver

class WebDriveFactory:
    @staticmethod
    def get_web_driver(browser):
        if browser == "fifefox":
            return webdriver.Firefox()
        elif browser == "chrome":
            return webdriver.Chrome()
        else:
            print("Для такого браузера нет драйвера")
