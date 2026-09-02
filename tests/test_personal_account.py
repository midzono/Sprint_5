from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data import LOGIN_URL, MAIN_URL
from locators import AccountPageLocators, AuthPageLocators, MainPageLocators


class TestPersonalAccount:

    def authorize(self, driver, credentials):
        wait = WebDriverWait(driver, 10)
        driver.get(LOGIN_URL)
        wait.until(EC.visibility_of_element_located(AuthPageLocators.EMAIL_INPUT)).send_keys(credentials["email"])
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(credentials["password"])
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()
        wait.until(EC.url_to_be(MAIN_URL))

    def test_open_personal_account(self, driver, registered_user):
        wait = WebDriverWait(driver, 10)
        self.authorize(driver, registered_user)

        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)).click()
        wait.until(EC.url_contains("/account"))

        assert "/account" in driver.current_url

    def test_go_from_account_to_constructor_by_constructor_link(self, driver, registered_user):
        wait = WebDriverWait(driver, 10)
        self.authorize(driver, registered_user)
        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)).click()
        wait.until(EC.url_contains("/account"))

        wait.until(EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_LINK)).click()
        wait.until(EC.url_to_be(MAIN_URL))

        assert driver.current_url == MAIN_URL

    def test_go_from_account_to_constructor_by_logo(self, driver, registered_user):
        wait = WebDriverWait(driver, 10)
        self.authorize(driver, registered_user)
        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)).click()
        wait.until(EC.url_contains("/account"))

        wait.until(EC.element_to_be_clickable(MainPageLocators.LOGO)).click()
        wait.until(EC.url_to_be(MAIN_URL))

        assert driver.current_url == MAIN_URL

    def test_logout_from_personal_account(self, driver, registered_user):
        wait = WebDriverWait(driver, 10)
        self.authorize(driver, registered_user)
        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)).click()
        wait.until(EC.url_contains("/account"))

        wait.until(EC.element_to_be_clickable(AccountPageLocators.LOGOUT_BUTTON)).click()
        wait.until(EC.url_to_be(LOGIN_URL))

        assert driver.current_url == LOGIN_URL
