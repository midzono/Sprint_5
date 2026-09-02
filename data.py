BASE_URL = "https://stellarburgers.education-services.ru"

MAIN_URL = f"{BASE_URL}/"
LOGIN_URL = f"{BASE_URL}/login"
REGISTER_URL = f"{BASE_URL}/register"
FORGOT_PASSWORD_URL = f"{BASE_URL}/forgot-password"
ACCOUNT_URL = f"{BASE_URL}/account"

#Имя пользователя для регистрации
USER_NAME = "Aleksandra"

#Пароль короче 6 символов — для негативного теста регистрации
INVALID_PASSWORD = "12345"

#Текст ошибки при слишком коротком пароле
INVALID_PASSWORD_ERROR = "Некорректный пароль"
