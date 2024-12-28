from selenium.webdriver.common.by import By


class LocatorsAccount:

    ACCOUNT_BUTTON = [By.XPATH, ".//p[text()='Личный Кабинет']"]
    LOGIN_BUTTON = [By.XPATH, ".//button[text()='Войти']"]
    LOGOUT_BUTTON = [By.XPATH, ".//button[text()='Выход']"]

    ORDER_HISTORY_LINK = [By.XPATH, ".//a[text()='История заказов']"]
    ORDER_HISTORY_LINK_ACTIVE = [By.XPATH, ".//a[contains(@class,'Account_link_active')]"]
    ORDER_HISTORY_PROFILE_LIST = [By.CSS_SELECTOR,
                                  "ul[class='OrderHistory_profileList__374GU OrderHistory_list__KcLDB']"]
    ORDER_HISTORY_PROFILE_ID = [By.CSS_SELECTOR, "li[class='OrderHistory_listItem__2x95r mb-6']"]
