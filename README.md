# Diplom_3
Проект по веб тестам
# Запуск тестов:
pytest tests/ --alluredir=allure-results

# Посмотреть результат в allure
allure serve allure_results

# Если тесты не запускаются на Windows через консоль:
$env:PYTHONPATH="."; pytest tests/ --alluredir=allure-results -v

# Посмотреть allure отчет на windows
allure generate allure-results -o allure-report --clean
allure open allure-report

# data/data.py
Статические данные

# pages/main_page.py
Функции для управления главной страницей