from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[normalize-space()='Войти в аккаунт']")  #Кнопка «Войти в аккаунт» на главной странице
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//*[normalize-space()='Личный Кабинет']")  #Ссылка «Личный кабинет» в шапке
    CONSTRUCTOR_LINK = (By.XPATH, "//*[normalize-space()='Конструктор']")  #Ссылка «Конструктор» в шапке
    LOGO = (By.XPATH, "//header//a[.//*[name()='svg' and @viewBox='0 0 290 50']]")  #Логотип Stellar Burgers
    BUNS_TAB = (By.XPATH, "//span[normalize-space()='Булки']/parent::*")  #Вкладка «Булки»
    SAUCES_TAB = (By.XPATH, "//span[normalize-space()='Соусы']/parent::*")  #Вкладка «Соусы»
    FILLINGS_TAB = (By.XPATH, "//span[normalize-space()='Начинки']/parent::*")  #Вкладка «Начинки»
    ASSEMBLE_BURGER_TITLE = (By.XPATH, "//h1[normalize-space()='Соберите бургер']")  #Заголовок конструктора


class AuthPageLocators:
    EMAIL_INPUT = (By.XPATH, "//label[normalize-space()='Email']/parent::*//input")  #Поле Email
    PASSWORD_INPUT = (By.XPATH, "//label[normalize-space()='Пароль']/parent::*//input")  #Поле «Пароль»
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Войти']")  #Кнопка «Войти» в форме авторизации
    REGISTER_LINK = (By.XPATH, "//a[normalize-space()='Зарегистрироваться']")  #Ссылка на форму регистрации
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[normalize-space()='Восстановить пароль']")  #Ссылка на форму восстановления пароля


class RegisterPageLocators:
    NAME_INPUT = (By.XPATH, "//label[normalize-space()='Имя']/parent::*//input")  #Поле «Имя»
    EMAIL_INPUT = (By.XPATH, "//label[normalize-space()='Email']/parent::*//input")  #Поле Email
    PASSWORD_INPUT = (By.XPATH, "//label[normalize-space()='Пароль']/parent::*//input")  #Поле «Пароль»
    REGISTER_BUTTON = (By.XPATH, "//button[normalize-space()='Зарегистрироваться']")  #Кнопка «Зарегистрироваться»
    LOGIN_LINK = (By.XPATH, "//a[normalize-space()='Войти']")  #Ссылка «Войти» в форме регистрации
    INVALID_PASSWORD_ERROR = (By.XPATH, "//*[normalize-space()='Некорректный пароль']")  #Сообщение об ошибке короткого пароля


class ForgotPasswordPageLocators:
    LOGIN_LINK = (By.XPATH, "//a[normalize-space()='Войти']")  #Ссылка «Войти» в форме восстановления пароля


class AccountPageLocators:
    LOGOUT_BUTTON = (By.XPATH, "//button[normalize-space()='Выход'] | //button[normalize-space()='Выйти']")  #Кнопка выхода из аккаунта
    PROFILE_LINK = (By.XPATH, "//*[normalize-space()='Профиль']")  #Пункт «Профиль» в личном кабинете
