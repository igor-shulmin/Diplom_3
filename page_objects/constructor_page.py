import allure
from data import Url
from locators.home import LocatorsHome
from locators.ingredients import Ingredients
from page_objects.login_page import LoginPageBurgers


class HomePageBurgers(LoginPageBurgers):

    @allure.step('Переходим по клику в раздел «Лента заказов»')
    def go_to_home_page_to_order_feed(self):
        self.go_to_page(Url.BASE_PAGE)
        self.driver_wait_for_clickable_element(LocatorsHome.ORDER_FEED_LINK)
        element = self.driver_find_element(LocatorsHome.ORDER_FEED_LINK)
        self.driver_click_element(element)
        self.driver_wait_for_clickable_element(LocatorsHome.ORDER_FEED_TEXT)
        if self.driver_find_element(LocatorsHome.ORDER_FEED_TEXT):

            return True

    @allure.step('Переходим по клику в раздел «Конструктор»')
    def go_to_home_page_to_constructor(self):
        self.go_to_home_page_to_order_feed()
        self.driver_wait_for_clickable_element(LocatorsHome.CONSTRUCTOR_LINK)
        element = self.driver_find_element(LocatorsHome.CONSTRUCTOR_LINK)
        self.driver_click_element(element)
        self.driver_wait_for_visibile_element(LocatorsHome.CONSTRUCTOR_TEXT)
        if self.driver_find_element(LocatorsHome.CONSTRUCTOR_TEXT):

            return True

    @allure.step('Кликаем на ингредиент бургера для загрузки окна с описанием')
    def get_ingredient_info(self):
        self.go_to_home_page_to_constructor()
        self.driver_wait_for_clickable_element(Ingredients.BULKA)
        element = self.driver_find_element(Ingredients.BULKA)
        self.driver_click_element(element)
        self.driver_wait_for_visibile_element(LocatorsHome.WINDOW_OPENED)
        if self.driver_find_element(LocatorsHome.WINDOW_OPENED):

            return True

    @allure.step('Закрываем всплывающее окно с информацией об ингредиенте')
    def close_ingredient_info(self):
        self.get_ingredient_info()
        self.driver_wait_for_clickable_element(LocatorsHome.WINDOW_CLOSE_BUTTON)
        element = self.driver_find_element(LocatorsHome.WINDOW_CLOSE_BUTTON)
        self.driver_click_element(element)
        if len(self.driver_find_elements(LocatorsHome.WINDOW_OPENED)) == 0:

            return True

    @allure.step('Добавляем ингредиенты в заказ и считаем их кол-во')
    def add_ingredients_to_order(self):
        self.go_to_home_page_to_constructor()

        def add_ingredient_to_order_and_count(locator_ingr, locator_counter):
            self.driver_wait_for_clickable_element(locator_ingr)
            ingr = self.driver_find_element(locator_ingr)
            counter_ingr_before = int(self.driver_find_element(locator_counter).text[0])
            self.driver_wait_for_clickable_element(Ingredients.BURGER_CONSTRUCTOR_DROP)
            constructor = self.driver_find_element(Ingredients.BURGER_CONSTRUCTOR_DROP)
            self.driver_scroll_to_element(ingr)
            self.driver_drag_and_drop_element(ingr, constructor)
            counter_ingr_after = int(self.driver_find_element(locator_counter).text[0])

            return counter_ingr_before, counter_ingr_after

        return (add_ingredient_to_order_and_count(Ingredients.BULKA, Ingredients.BULKA_COUNTER),
                add_ingredient_to_order_and_count(Ingredients.SOUS, Ingredients.SOUS_COUNTER),
                add_ingredient_to_order_and_count(Ingredients.NACHINKA, Ingredients.NACHINKA_COUNTER))

    @allure.step('Оформляем заказ авторизованного пользователя')
    def make_user_order(self, add_ingr=False):
        self.make_login()
        if add_ingr:
            self.add_ingredients_to_order()
        self.driver_wait_for_clickable_element(LocatorsHome.ORDER_BUTTON)
        element = self.driver_find_element(LocatorsHome.ORDER_BUTTON)
        self.driver_click_element(element)

        self.driver_wait_for_visibile_element(LocatorsHome.ORDER_WINDOW_ID)
        user_order_id = self.driver_find_element(LocatorsHome.ORDER_WINDOW_ID).text
        element = self.driver_find_element(LocatorsHome.WINDOW_CLOSE_BUTTON)
        self.driver_click_element(element)

        return user_order_id
