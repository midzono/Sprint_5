from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data import INVALID_PASSWORD, INVALID_PASSWORD_ERROR, LOGIN_URL, REGISTER_URL
from helpers import generate_user_data
from locators import RegisterPageLocators


class TestRegistration:

    def test_successful_registration(self, driver):
        user_credentials = generate_user_data()
        wait = WebDriverWait(driver, 10)
        driver.get(REGISTER_URL)

        wait.until(EC.visibility_of_element_located(RegisterPageLocators.NAME_INPUT)).send_keys(user_credentials["name"])
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(user_credentials["email"])
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(user_credentials["password"])
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        wait.until(EC.url_to_be(LOGIN_URL))
        assert driver.current_url == LOGIN_URL

    def test_registration_with_short_password_shows_error(self, driver):
        user_credentials = generate_user_data()
        wait = WebDriverWait(driver, 10)
        driver.get(REGISTER_URL)

        wait.until(EC.visibility_of_element_located(RegisterPageLocators.NAME_INPUT)).send_keys(user_credentials["name"])
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(user_credentials["email"])
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(INVALID_PASSWORD)
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        error = wait.until(EC.visibility_of_element_located(RegisterPageLocators.INVALID_PASSWORD_ERROR))
        assert error.text == INVALID_PASSWORD_ERROR
