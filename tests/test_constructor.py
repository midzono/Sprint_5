from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data import MAIN_URL
from locators import MainPageLocators


class TestConstructor:

    def test_switch_to_buns(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get(MAIN_URL)

        wait.until(EC.element_to_be_clickable(MainPageLocators.SAUCES_TAB)).click()
        wait.until(EC.element_to_be_clickable(MainPageLocators.BUNS_TAB)).click()

        active_buns = wait.until(EC.visibility_of_element_located(MainPageLocators.BUNS_TAB_ACTIVE))

        assert active_buns.is_displayed()
        driver.quit()

    def test_switch_to_sauces(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get(MAIN_URL)

        wait.until(EC.element_to_be_clickable(MainPageLocators.SAUCES_TAB)).click()

        active_sauces = wait.until(EC.visibility_of_element_located(MainPageLocators.SAUCES_TAB_ACTIVE))

        assert active_sauces.is_displayed()
        driver.quit()

    def test_switch_to_fillings(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get(MAIN_URL)

        wait.until(EC.element_to_be_clickable(MainPageLocators.FILLINGS_TAB)).click()

        active_fillings = wait.until(EC.visibility_of_element_located(MainPageLocators.FILLINGS_TAB_ACTIVE))

        assert active_fillings.is_displayed()
        driver.quit()
