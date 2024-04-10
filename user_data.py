from faker import Faker


class DataUser:
    fake = Faker()
    # Данные для регистрации пользователя
    # Рандомное имя
    USER_REG_NAME = fake.name()
    # Рандомный пароль подходящий под условия
    USER_REG_PASSWORD = fake.password(length=6)
    # рандомный пароль не подходящий под условия
    USER_ERROR_REG_PASSWORD = fake.password(length=5)
    # Рандомная почка(логин)
    USER_REG_EMAIL = fake.email()

    # Логин для входа на сайт
    AUTH_LOGIN = "g_alexey@yandex.ru"
    # Пароль для входа на сайт
    AUTH_PASSWORD = "Qwerty1!"
