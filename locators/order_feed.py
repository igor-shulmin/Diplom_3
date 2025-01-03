from selenium.webdriver.common.by import By


class LocatorsOrderFeed:

    ORDER_FEED_LIST = [By.CSS_SELECTOR, "ul[class='OrderFeed_list__OLh59']"]
    ORDER_IN_FEED = [By.CSS_SELECTOR, "a[class='OrderHistory_link__1iNby']"]
    ORDER_COUNTER_TEXT = [By.CSS_SELECTOR, "p[class='OrderFeed_number__2MbrQ text text_type_digits-large']"]
    ORDERS_IN_PROGRESS = [By.CSS_SELECTOR, "li[class='text text_type_digits-default mb-2']"]
