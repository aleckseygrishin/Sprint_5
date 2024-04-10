from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import urls
from locators import StellarBurgersLocators


class TestExitAccount:
    def test_exit_account(self, login):
        switch_personal_acc = login.find_element(*StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON)
        WebDriverWait(login, 10).until(expected_conditions.element_to_be_clickable(
            StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON))
        switch_personal_acc.click()

        WebDriverWait(login, 10).until(expected_conditions.element_to_be_clickable(
            StellarBurgersLocators.EXIT_BUTTON))

        exit_button = login.find_element(*StellarBurgersLocators.EXIT_BUTTON)
        exit_button.click()

        WebDriverWait(login, 10).until(expected_conditions.url_to_be(urls.URL_LOGIN))

        assert login.current_url == urls.URL_LOGIN

        login.quit()


