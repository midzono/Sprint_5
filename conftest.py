import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data import REGISTER_URL, USER_NAME
from helpers import generate_email, generate_password
from locators import RegisterPageLocators


@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--window-size=1440,1000")

    browser = webdriver.Chrome(options=chrome_options)
    browser.implicitly_wait(3)

    yield browser

    browser.quit()


@pytest.fixture
def user_credentials():
    return {
        "name": USER_NAME,
        "email": generate_email(),
        "password": generate_password(),
    }


@pytest.fixture
def registered_user(driver, user_credentials):
    wait = WebDriverWait(driver, 10)
    driver.get(REGISTER_URL)

    wait.until(EC.visibility_of_element_located(RegisterPageLocators.NAME_INPUT)).send_keys(user_credentials["name"])
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(user_credentials["email"])
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(user_credentials["password"])
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    #После успешной регистрации приложение переводит пользователя на страницу входа.
    wait.until(EC.url_contains("/login"))

    return user_credentials
