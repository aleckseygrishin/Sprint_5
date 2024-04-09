import urls
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import StellarBurgersLocators
from user_data import DataUser


class TestSwitchPages:
    def test_switch_from_main_page_to_personal_acc_page_urls_correct(self, driver):
        driver.get(urls.URL_LOGIN)

        user_name = driver.find_element(*StellarBurgersLocators.EMAIL)
        user_name.send_keys(DataUser.AUTH_LOGIN)

        user_name = driver.find_element(*StellarBurgersLocators.PASSWORD)
        user_name.send_keys(DataUser.AUTH_PASSWORD)

        enter_button = driver.find_element(*StellarBurgersLocators.ENTER_BUTTON)
        enter_button.click()

        switch_personal_acc = driver.find_element(*StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON)
        switch_personal_acc.click()

        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(urls.URL_PROFILE))

        assert driver.current_url == urls.URL_PROFILE

    @pytest.mark.parametrize('switch_locators', [StellarBurgersLocators.MAIN_LOGO,
                                                 StellarBurgersLocators.CONSTRUCTOR_BUTTON])
    def test_switch_from_personal_acc_page_to_main_logo_and_constructor_pages_urls_correct(
            self, driver, switch_locators):
        driver.get(urls.URL_LOGIN)

        user_name = driver.find_element(*StellarBurgersLocators.EMAIL)
        user_name.send_keys(DataUser.AUTH_LOGIN)

        user_name = driver.find_element(*StellarBurgersLocators.PASSWORD)
        user_name.send_keys(DataUser.AUTH_PASSWORD)

        enter_button = driver.find_element(*StellarBurgersLocators.ENTER_BUTTON)
        enter_button.click()

        switch_personal_acc = driver.find_element(*StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON)
        switch_personal_acc.click()

        switch_with_personal_acc = driver.find_element(*switch_locators)
        switch_with_personal_acc.click()

        assert driver.current_url == urls.URL_MAIN_PAGE
