import allure
from data import Url
from locators.constructor import LocatorsConstructor
from locators.order_feed import LocatorsOrderFeed
from page_objects.base_page import BasePageBurgers
from page_objects.account_page import AccountPageBurgers
from page_objects.constructor_page import ConstructorPageBurgers


class OrderFeedPageBurgers(BasePageBurgers):

    def __init__(self, driver, user):
        super().__init__(driver)
        self.user = user

    @allure.step('Кликаем на заказ для загрузки окна с описанием')
    def get_order_info(self, index):
        self.go_to_page(Url.ORDER_FEED_PAGE)
        self.driver_wait_for_clickable_element(LocatorsOrderFeed.ORDER_FEED_LIST)
        element = self.driver_find_elements(LocatorsOrderFeed.ORDER_IN_FEED)[index]
        self.driver_wait_for_clickable_element(element)
        self.driver_scroll_to_element(element)
        self.driver_click_element(element)
        self.driver_wait_for_visibile_element(LocatorsConstructor.WINDOW_OPENED)
        if self.driver_find_element(LocatorsConstructor.WINDOW_OPENED):

            return True

    @allure.step('Получаем список последних 50 заказов в "Ленте" и список заказов пользователя')
    def get_top_50_order_list_and_user_order_list(self):
        ConstructorPageBurgers.make_user_order(self, add_ingr=True)
        user_order_list = AccountPageBurgers.get_user_order_list(self)

        self.go_to_page(Url.ORDER_FEED_PAGE)
        self.driver_wait_for_clickable_element(LocatorsOrderFeed.ORDER_FEED_LIST)
        elements = self.driver_find_elements(LocatorsOrderFeed.ORDER_IN_FEED)
        top_50_order_list = [element.text[2:8] for element in elements]

        return user_order_list, top_50_order_list

    @allure.step('Получаем данные счётчика "Выполнено за всё время" до и после заказа')
    def get_total_counter(self, order=False):
        if order:
            ConstructorPageBurgers.make_user_order(self, add_ingr=True)
        self.go_to_page(Url.ORDER_FEED_PAGE)
        self.driver_wait_for_visibile_element(LocatorsOrderFeed.ORDER_COUNTER_TEXT)
        elements = self.driver_find_elements(LocatorsOrderFeed.ORDER_COUNTER_TEXT)
        total_counter = elements[0].text

        return total_counter

    @allure.step('Получаем данные счётчика "Выполнено за сегодня" до и после заказа')
    def get_daily_counter(self, order=False):
        if order:
            ConstructorPageBurgers.make_user_order(self, add_ingr=True)
        self.go_to_page(Url.ORDER_FEED_PAGE)
        self.driver_wait_for_visibile_element(LocatorsOrderFeed.ORDER_COUNTER_TEXT)
        elements = self.driver_find_elements(LocatorsOrderFeed.ORDER_COUNTER_TEXT)
        daily_counter = elements[1].text

        return daily_counter

    @allure.step('Получаем данные из раздела "В работе"')
    def get_orders_in_progress_and_user_order(self):
        ConstructorPageBurgers.make_user_order(self, add_ingr=True)
        user_order_id = AccountPageBurgers.get_user_order_list(self)[0]

        self.go_to_page(Url.ORDER_FEED_PAGE)
        self.driver_wait_for_clickable_element(LocatorsOrderFeed.ORDER_FEED_LIST)
        element = self.driver_find_element(LocatorsOrderFeed.ORDERS_IN_PROGRESS)
        order_in_progress_id = element.text[1:]

        return user_order_id, order_in_progress_id
