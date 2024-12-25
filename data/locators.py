from selenium.webdriver.common.by import By

# Главная страница
feed_order_button = [By.XPATH, "//a[@class='AppHeader_header__link__3D_hX' and .//p[text()='Лента Заказов']]"]
constructor_button = [By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2']"]
main_page_personal_account = [By.XPATH, "//a[@class='AppHeader_header__link__3D_hX' and .//p[text()='Личный Кабинет']]"]
main_page_order_button = [By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']"]
ingredient = [By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']"]
modal_ingredient_text = [By.XPATH, "//p[@class='undefined text text_type_main-default text_color_inactive']"]
close_modal = [By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"]
move_place = [By.XPATH, "//span[@class='constructor-element__text']"]
counter_ingredient = [By.XPATH, "//p[@class='counter_counter__num__3nue1']"]
main_page_make_burger_text = [By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10']"]
create_order_modal = [By.XPATH, "//p[@class='undefined text text_type_main-small mb-2']"]

# Страница login
login_page_recover_password_button = [By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/forgot-password']"]
login_page_email_field = [By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @name='name']"]
login_page_password_field = [By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @name='Пароль']"]
login_page_login_button = [By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"]
register_button_in_personal_account = [By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/register']"]

# Страница forgot-password
forgot_page_login_button = [By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/login']"]
forgot_page_email_field = [By.XPATH, "//input[@class='text input__textfield text_type_main-default']"]

# Страница reset-password
reset_pass_page_field = [By.XPATH, "//input[@class='text input__textfield text_type_main-default']"]
reset_pass_hidden_button = [By.XPATH, "//div[@class='input__icon input__icon-action']"]
reset_pass_pass_field = [By.XPATH, "//input[@name='Введите новый пароль']"]
reset_pass_save_button = [By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"]
reset_pass_second_field = [By.XPATH, "//label[@class='input__placeholder text noselect text_type_main-default' and text()='Введите код из письма']"]

#Страница account
personal_account_exit_button = [By.XPATH, "//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']"]
personal_account_history_button = [By.XPATH, "//a[text()='История заказов']"]
modal_loader = [By.XPATH, "//p[@class='Modal_modal__loading__3534A']"]

# Страница feed
text_feed_order = [By.XPATH, "//h1[@class='text text_type_main-large mt-10 mb-5']"]
first_order = (By.XPATH, "//div[@class='OrderFeed_contentBox__3-tWb']//ul[@class='OrderFeed_list__OLh59']/li[1]")
text_field_in_modal = [By.XPATH, "//p[@class='text text_type_main-default text_color_inactive']"]
order_number_field = [By.XPATH, "//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']"]
wait_order_number_modal = [By.XPATH, "//div[@class='Modal_modal__P3_V5']"]
close_modal_order = [By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"]
order_in_work = [By.XPATH, "//li[@class='text text_type_digits-default mb-2']"]
find_order_number_in_list = [By.XPATH, "//p[@class='text text_type_digits-default']"]
total_count_all_time = [By.XPATH, "(//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'])[1]"]
total_today_count = [By.XPATH, "(//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'])[2]"]