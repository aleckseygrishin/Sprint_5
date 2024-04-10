from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import urls
import pytest
from user_data import DataUser
from locators import StellarBurgersLocators


class TestLoginSite:

    @pytest.mark.parametrize('button_switch', [StellarBurgersLocators.ENTER_IN_ACC_MAIN_PAGE,
                                               StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON])
    def test_login_with_main_page_place_an_order_button_is_visible(self, driver, button_switch):
        driver.get(urls.URL_MAIN_PAGE)

        enter_in_acc = driver.find_element(*button_switch)
        enter_in_acc.click()

        user_login = driver.find_element(*StellarBurgersLocators.EMAIL)
        user_login.send_keys(DataUser.AUTH_LOGIN)

        user_password = driver.find_element(*StellarBurgersLocators.PASSWORD)
        user_password.send_keys(DataUser.AUTH_PASSWORD)

        enter_button = driver.find_element(*StellarBurgersLocators.ENTER_BUTTON)
        enter_button.click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            StellarBurgersLocators.PLACE_AN_ORDER_BUTTON))

        button_order = driver.find_element(*StellarBurgersLocators.PLACE_AN_ORDER_BUTTON)

        assert button_order.is_displayed() and button_order.text == "Оформить заказ"

    @pytest.mark.parametrize('url', [urls.URL_REGISTRATION, urls.URL_FORGOT_PASSWORD])
    def test_login_with_registration_and_forgot_password_pages_place_an_order_button_is_visible(self, driver, url):
        driver.get(url)

        enter_in_acc = driver.find_element(*StellarBurgersLocators.ENTER_HREF_FORM_REGISTRATION)
        enter_in_acc.click()

        user_login = driver.find_element(*StellarBurgersLocators.EMAIL)
        user_login.send_keys(DataUser.AUTH_LOGIN)

        user_password = driver.find_element(*StellarBurgersLocators.PASSWORD)
        user_password.send_keys(DataUser.AUTH_PASSWORD)

        enter_button = driver.find_element(*StellarBurgersLocators.ENTER_BUTTON)
        enter_button.click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            StellarBurgersLocators.PLACE_AN_ORDER_BUTTON))

        button_order = driver.find_element(*StellarBurgersLocators.PLACE_AN_ORDER_BUTTON)

        assert button_order.is_displayed() and button_order.text == "Оформить заказ"

