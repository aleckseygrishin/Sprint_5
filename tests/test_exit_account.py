from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import urls
from locators import StellarBurgersLocators


class TestExitAccount:
    def test_exit_account(self, login, driver):
        switch_personal_acc = driver.find_element(*StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(
            StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON))
        switch_personal_acc.click()

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(
            StellarBurgersLocators.EXIT_BUTTON))

        exit_button = driver.find_element(*StellarBurgersLocators.EXIT_BUTTON)
        exit_button.click()

        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(urls.URL_LOGIN))

        assert driver.current_url == urls.URL_LOGIN



