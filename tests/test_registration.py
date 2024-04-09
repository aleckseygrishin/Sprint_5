from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import urls
from locators import StellarBurgersLocators
from user_data import DataUser


class TestRegitration:
    #Тест успешной регистрации
    def test_registration_valid_user_data_success_transition_on_login_url(self, driver_registration, driver_login):
        user_name = driver_registration.find_element(*StellarBurgersLocators.REGISTRATION_NICKNAME)
        user_name.send_keys(DataUser.USER_REG_NAME)

        user_email = driver_registration.find_element(*StellarBurgersLocators.EMAIL)
        login = DataUser.USER_REG_EMAIL
        user_email.send_keys(login)

        user_password = driver_registration.find_element(*StellarBurgersLocators.PASSWORD)
        password = DataUser.USER_REG_PASSWORD
        user_password.send_keys(password)

        button_registration = driver_registration.find_element(*StellarBurgersLocators.REGISTRATION_BUTTON)
        button_registration.click()
        WebDriverWait(driver_registration, 3).until(expected_conditions.visibility_of_element_located(
            StellarBurgersLocators.TITLE_H2_ENTER))

        assert driver_registration.current_url == urls.URL_LOGIN

    # Тест некорректного пароля (меньше 6 символов)
    def test_registration_password_len_is_less_six_symbols_err_incorrect_password(self, driver_registration):
        user_password = driver_registration.find_element(*StellarBurgersLocators.PASSWORD)
        user_password.send_keys(DataUser.USER_ERROR_REG_PASSWORD)

        button_registration = driver_registration.find_element(*StellarBurgersLocators.REGISTRATION_BUTTON)
        button_registration.click()

        WebDriverWait(driver_registration, 3).until(expected_conditions.visibility_of_element_located(
            StellarBurgersLocators.ERROR_PASSWORD_LEN))

        p_element_error = driver_registration.find_element(*StellarBurgersLocators.ERROR_PASSWORD_LEN)

        assert p_element_error.is_displayed() and p_element_error.text == "Некорректный пароль"