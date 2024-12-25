import random
import allure

@allure.step("Генерация пользовательских данных")
def return_random_user_for_register():
    random_number = random.randint(1000, 9999)
    random_email = f"r{random_number}:{random_number}@ya.ru"
    random_pass = f"password:{random_number}"
    random_username = f"Username:{random_number}"

    user_data = {
        "email": random_email,
        "password": random_pass,
        "name": random_username
    }
    return user_data
