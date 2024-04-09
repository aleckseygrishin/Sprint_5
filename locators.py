from selenium.webdriver.common.by import By


class StellarBurgersLocators:
    # Поля/Кнопки для регистрации
    # Поле - Имя
    REGISTRATION_NICKNAME = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    # Поле - Логин
    EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    # Поле - Пароль
    PASSWORD = (By.XPATH, "//input[@name='Пароль']")
    # Кнопка регистрации
    REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    # Кнопка входа
    ENTER_BUTTON = (By.XPATH, "//button[text()='Войти']")
    # h2 заголовок для проверки(Форма входа)
    TITLE_H2_ENTER = (By.XPATH, "//h2[text()='Вход']")
    # Ошибка при некорректном пароле
    ERROR_PASSWORD_LEN = (By.XPATH, "//p[text()='Некорректный пароль']")
    # Кнопка оформления заказа (Главная страница), неавторизованная зона
    PLACE_AN_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    # Кнопка войти в аккаунт на главной странице
    ENTER_IN_ACC_MAIN_PAGE = (By.XPATH, "//button[text()='Войти в аккаунт']")
    # Кнопка личного кабинета
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/account']")
    # Ссылка на кнопку входа с формы регистрации
    ENTER_HREF_FORM_REGISTRATION = (By.XPATH, "//a[@href='/login']")
    # Основная эмблема на главной странице (хедер)
    MAIN_LOGO = (By.XPATH, "//div/a[@href='/']")
    # Кнопка конструктора (хедер)
    CONSTRUCTOR_BUTTON = (By.XPATH, "//li/a[@href='/']")
