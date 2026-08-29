from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data import MAIN_URL
from locators import MainPageLocators


def is_active(element):
    return "current" in element.get_attribute("class")


def test_switch_to_buns(driver):
    wait = WebDriverWait(driver, 10)
    driver.get(MAIN_URL)

    #Сначала уходим с вкладки «Булки», затем возвращаемся на неё.
    wait.until(EC.element_to_be_clickable(MainPageLocators.SAUCES_TAB)).click()
    buns = wait.until(EC.element_to_be_clickable(MainPageLocators.BUNS_TAB))
    buns.click()

    wait.until(lambda _: is_active(buns))
    assert is_active(buns)


def test_switch_to_sauces(driver):
    wait = WebDriverWait(driver, 10)
    driver.get(MAIN_URL)

    sauces = wait.until(EC.element_to_be_clickable(MainPageLocators.SAUCES_TAB))
    sauces.click()

    wait.until(lambda _: is_active(sauces))
    assert is_active(sauces)


def test_switch_to_fillings(driver):
    wait = WebDriverWait(driver, 10)
    driver.get(MAIN_URL)

    fillings = wait.until(EC.element_to_be_clickable(MainPageLocators.FILLINGS_TAB))
    fillings.click()

    wait.until(lambda _: is_active(fillings))
    assert is_active(fillings)
