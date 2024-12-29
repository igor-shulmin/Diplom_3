from selenium.webdriver.common.by import By


class ResetPassword:

    RESET_PASSWORD_BUTTON = [By.XPATH, ".//*[contains(text(),'Восстановить пароль')]"]
    RESET_FIELD = [By.XPATH, ".//input[@name='name']"]
    RESET_PASSWORD_BUTTON_2 = [By.XPATH, ".//*[contains(text(),'Восстановить')]"]
    SHOW_PASS_BUTTON = [By.XPATH, ".//div[contains(@class, 'icon-action')]"]
    RESET_FIELD_ACTIVE = [By.XPATH, ".//div[contains(@class, 'input_status_active')]"]
