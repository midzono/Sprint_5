from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data import FORGOT_PASSWORD_URL, MAIN_URL, REGISTER_URL
from locators import (
    AuthPageLocators,
    ForgotPasswordPageLocators,
    MainPageLocators,
    RegisterPageLocators
)


class TestLogin:

    def login(self, driver, email, password):
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(AuthPageLocators.EMAIL_INPUT)).send_keys(email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()
        wait.until(EC.visibility_of_element_located(MainPageLocators.ASSEMBLE_BURGER_TITLE))

    def test_login_from_main_page_button(self, driver, registered_user):
        driver.get(MAIN_URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.LOGIN_ACCOUNT_BUTTON)).click()

        self.login(
            driver,
            registered_user["email"],
            registered_user["password"]
        )

        assert driver.current_url == MAIN_URL

    def test_login_from_personal_account_link(self, driver, registered_user):
        driver.get(MAIN_URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)).click()

        self.login(
            driver,
            registered_user["email"],
            registered_user["password"]
        )

        assert driver.current_url == MAIN_URL

    def test_login_from_registration_form(self, driver, registered_user):
        driver.get(REGISTER_URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(RegisterPageLocators.LOGIN_LINK)).click()

        self.login(
            driver,
            registered_user["email"],
            registered_user["password"]
        )

        assert driver.current_url == MAIN_URL

    def test_login_from_forgot_password_form(self, driver, registered_user):
        driver.get(FORGOT_PASSWORD_URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ForgotPasswordPageLocators.LOGIN_LINK)).click()

        self.login(
            driver,
            registered_user["email"],
            registered_user["password"]
        )

        assert driver.current_url == MAIN_URL
