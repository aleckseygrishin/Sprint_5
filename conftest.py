import pytest
from selenium import webdriver
import urls
from locators import StellarBurgersLocators
from user_data import DataUser


@pytest.fixture(scope='function')
def driver_registration():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(urls.URL_REGISTRATION)

    return chrome_driver


@pytest.fixture(scope='function')
def driver_login():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(urls.URL_LOGIN)

    return chrome_driver


@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()

    return chrome_driver


@pytest.fixture(scope='function')
def login(driver_login):
    driver_login.get(urls.URL_LOGIN)
    user_name = driver_login.find_element(*StellarBurgersLocators.EMAIL)
    user_name.send_keys(DataUser.AUTH_LOGIN)

    user_name = driver_login.find_element(*StellarBurgersLocators.PASSWORD)
    user_name.send_keys(DataUser.AUTH_PASSWORD)

    enter_button = driver_login.find_element(*StellarBurgersLocators.ENTER_BUTTON)
    enter_button.click()

    return driver_login
