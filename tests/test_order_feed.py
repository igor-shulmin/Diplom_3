import allure
import pytest
from page_objects.order_feed_page import OrderFeedPageBurgers


@pytest.mark.usefixtures('driver', 'user')
class TestOrderFeed:

    @allure.title('Проверка загрузки всплывающего окна с описанием заказа')
    def test_check_order_info(self):
        order = OrderFeedPageBurgers(self.driver, self.user)

        assert order.get_order_info(49) == True

    @allure.title('Проверка наличия заказов пользователя на странице «Лента заказов»')
    def test_check_user_order_in_order_feed(self):
        user_order = OrderFeedPageBurgers(self.driver, self.user)
        user_order_list, top_50_order_list = user_order.get_top_50_order_list_and_user_order_list()

        assert set(user_order_list).issubset(top_50_order_list)
    #
    @allure.title('Проверка данных счётчика "Выполнено за всё время" до и после заказа')
    def test_check_total_counter(self):
        total = OrderFeedPageBurgers(self.driver, self.user)
        total_before = int(total.get_total_counter())
        total_after = int(total.get_total_counter(order=True))

        assert total_after > total_before

    @allure.title('Проверка данных счётчика "Выполнено за сегодня" до и после заказа')
    def test_check_daily_counter(self):
        daily = OrderFeedPageBurgers(self.driver, self.user)
        daily_before = int(daily.get_daily_counter())
        daily_after = int(daily.get_daily_counter(order=True))

        assert daily_after > daily_before

    @allure.title('Проверка номер заказа в разделе "В работе"')
    def test_check_info_from_orders_in_progress(self):
        orders = OrderFeedPageBurgers(self.driver, self.user)
        user_order_id, order_in_progress_id = orders.get_orders_in_progress_and_user_order()

        assert user_order_id == order_in_progress_id
