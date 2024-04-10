import urls
import pytest
from locators import StellarBurgersLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestSwitchingConstructor:
    def test_switch_from_breads_to_sauces_added_css_class(self, driver):
        driver.get(urls.URL_MAIN_PAGE)

        sauces_chapter = driver.find_element(*StellarBurgersLocators.SAUCES_CONSTRUCTOR)
        sauces_chapter.click()

        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element_attribute(
            StellarBurgersLocators.SAUCES_CONSTRUCTOR, "class", "tab_tab_type_current__2BEPc"))

        checking_sauces_class = driver.find_element(*StellarBurgersLocators.SAUCES_CONSTRUCTOR)

        assert "tab_tab_type_current__2BEPc" in checking_sauces_class.get_attribute("class")

    @pytest.mark.parametrize('locator_from, locator_to', [
        [StellarBurgersLocators.SAUCES_CONSTRUCTOR, StellarBurgersLocators.FILLINGS_CONSTRUCTOR],
        [StellarBurgersLocators.FILLINGS_CONSTRUCTOR, StellarBurgersLocators.BREADS_CONSTRUCTOR]])
    def test_switch_from_sauces_and_fillings_to_another_chapter_added_css_class(self, driver, locator_from, locator_to):
        driver.get(urls.URL_MAIN_PAGE)

        sauces_chapter = driver.find_element(*locator_from)
        sauces_chapter.click()

        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element_attribute(
            locator_from, "class", "tab_tab_type_current__2BEPc"))

        fillings_chapter = driver.find_element(*locator_to)
        fillings_chapter.click()

        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element_attribute(
            locator_to, "class", "tab_tab_type_current__2BEPc"))

        checking_fillings_class = driver.find_element(*locator_to)

        assert "tab_tab_type_current__2BEPc" in checking_fillings_class.get_attribute("class")

