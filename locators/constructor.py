from selenium.webdriver.common.by import By


class LocatorsHome:

    ORDER_FEED_LINK = [By.XPATH, ".//p[text()='Лента Заказов']"]
    ORDER_FEED_TEXT = [By.XPATH, ".//h1[text()='Лента заказов']"]
    ORDER_FEED_LIST = [By.CSS_SELECTOR, "ul[class='OrderFeed_list__OLh59']"]
    ORDER_BUTTON = [By.XPATH, ".//button[text()='Оформить заказ']"]
    ORDER_WINDOW_ID = [By.XPATH,
                       ".//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']"]

    CONSTRUCTOR_LINK = [By.XPATH, ".//p[text()='Конструктор']"]
    CONSTRUCTOR_TEXT = [By.XPATH, ".//h1[text()='Соберите бургер']"]

    WINDOW_OPENED = [By.XPATH, ".//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']"]
    WINDOW_CLOSE_BUTTON = [By.CSS_SELECTOR,
                           "button[class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"]
