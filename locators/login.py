from selenium.webdriver.common.by import By


class LocatorsLogin:

    ACCOUNT_BUTTON = [By.XPATH, ".//p[text()='Личный Кабинет']"]
    LOGIN_BUTTON = [By.XPATH, ".//button[text()='Войти']"]
    ORDER_BUTTON = [By.XPATH, ".//button[text()='Оформить заказ']"]
    EMAIL_FIELD = [By.CSS_SELECTOR, "input[name='name']"]
    PASS_FIELD = [By.CSS_SELECTOR, "input[name='Пароль']"]
