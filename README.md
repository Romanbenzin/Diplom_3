# Diplom_3
Проект по веб тестам
# Запуск тестов:
pytest test/ --alluredir=allure-results
pytest test/test_order_page.py::TestClickOnLogo::test_example --alluredir=allure-results

# Если тесты не запускаются на Windows через консоль:
$env:PYTHONPATH="."; pytest test/ --alluredir=allure-results -v

# Посмотреть результат в allure
allure serve allure_results

# Посмотреть allure отчет на windows
allure generate allure-results -o allure-report --clean
allure open allure-report

# data/data.py
Статические данные

# pages/main_page.py
Функции для управления главной страницей