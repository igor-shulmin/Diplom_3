from selenium.webdriver.common.by import By


class Ingredients:

    BURGER_CONSTRUCTOR_DROP = [By.CSS_SELECTOR, "span.constructor-element__text"]

    BULKA = [By.CSS_SELECTOR, "img[src='https://code.s3.yandex.net/react/code/bun-01.png']"]
    BULKA_COUNTER = [By.XPATH,
                     ".//p[@class='counter_counter__num__3nue1']/parent::*/parent::a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']"]

    SOUS = [By.CSS_SELECTOR, "img[src='https://code.s3.yandex.net/react/code/sauce-03.png']"]
    SOUS_COUNTER = [By.XPATH,
                     ".//p[@class='counter_counter__num__3nue1']/parent::*/parent::a[@href='/ingredient/61c0c5a71d1f82001bdaaa74']"]

    NACHINKA = [By.CSS_SELECTOR, "img[src='https://code.s3.yandex.net/react/code/cheese.png']"]
    NACHINKA_COUNTER = [By.XPATH,
                     ".//p[@class='counter_counter__num__3nue1']/parent::*/parent::a[@href='/ingredient/61c0c5a71d1f82001bdaaa7a']"]
