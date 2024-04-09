import pytest
from selenium import webdriver
import urls


@pytest.fixture(scope='function')
def driver_registration():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(urls.URL_REGISTRATION)

    yield chrome_driver

    chrome_driver.quit()


@pytest.fixture(scope='function')
def driver_login():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(urls.URL_LOGIN)

    yield chrome_driver

    chrome_driver.quit()


@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()

    yield chrome_driver

    chrome_driver.quit()