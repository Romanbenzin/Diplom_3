from selenium.webdriver.common.by import By

#Страница регистрации
register_page_already_registered = "//p[@class='undefined text text_type_main-default text_color_inactive mb-4']"
register_page_fields= "//input[@class='text input__textfield text_type_main-default']"
register_page_register_button = "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"
register_page_error = "//p[@class='input__error text_type_main-default']"
register_page_login_button = "//a[@class='Auth_link__1fOlj' and @href='/login']"

#Главная страница
ssssregister_button_in_personal_account = "//a[@class='Auth_link__1fOlj' and @href='/register']"
ssssmain_page_login_button = [By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']"]

main_page_make_burger_text = "//h1[@class='text text_type_main-large mb-5 mt-10']"
main_page_select_sauce = ".//span[text()='Соусы']"
main_page_select_sauce_up = main_page_select_sauce + "/.."
main_page_select_filling = ".//span[text()='Начинки']"
main_page_select_filling_up = main_page_select_filling + "/.."
main_page_select_bun = ".//span[text()='Булки']"
main_page_select_bun_up = main_page_select_bun + "/.."
#Страница личный аккаунта
personal_account_save_button = "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"
personal_account_email_field = "//input[@class='text input__textfield text_type_main-default input__textfield-disabled']"
personal_account_exit_button = "//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']"
#Лого бургера и конструктор
constructor_button = "//p[@class='AppHeader_header__linkText__3q_va ml-2']"
burger_logo = "//a[@href='/']"
#Ожидамое значение для теста. Селект выбран
selected_this_one = "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"
#Ожидаемое значение для теста. Селект не выбран
selected_value_not_this = "tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect"


# Главная страница
main_page_login_button = [By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/register']"]
main_page_personal_account = [By.XPATH, "//a[@class='AppHeader_header__link__3D_hX' and .//p[text()='Личный Кабинет']]"]

# Страница login
login_page_recover_password_button = [By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/forgot-password']"]
login_page_email_field = [By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @name='name']"]
login_page_password_field = [By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @name='Пароль']"]
login_page_login_button = [By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"]

# Страница forgot-password
forgot_page_login_button = [By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/login']"]
forgot_page_email_field = [By.XPATH, "//input[@class='text input__textfield text_type_main-default']"]
forgot_page_recover_button = [By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"]

# Страница reset-password
reset_pass_page_field = [By.XPATH, "//input[@class='text input__textfield text_type_main-default']"]
reset_pass_hidden_button = [By.XPATH, "//div[@class='input__icon input__icon-action']"]
reset_pass_pass_field = [By.XPATH, "//input[@name='Введите новый пароль']"]

# test = [By.XPATH, ]





