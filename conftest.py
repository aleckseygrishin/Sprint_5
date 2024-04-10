import pytest
from selenium import webdriver
import urls
from locators import StellarBurgersLocators
from user_data import DataUser


@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()

    yield chrome_driver

    chrome_driver.quit()


@pytest.fixture(scope='function')
def driver_registration(driver):
    driver.get(urls.URL_REGISTRATION)


@pytest.fixture(scope='function')
def driver_login(driver):
    driver.get(urls.URL_LOGIN)


@pytest.fixture(scope='function')
def login(driver_login, driver):
    user_name = driver.find_element(*StellarBurgersLocators.EMAIL)
    user_name.send_keys(DataUser.AUTH_LOGIN)

    user_name = driver.find_element(*StellarBurgersLocators.PASSWORD)
    user_name.send_keys(DataUser.AUTH_PASSWORD)

    enter_button = driver.find_element(*StellarBurgersLocators.ENTER_BUTTON)
    enter_button.click()

