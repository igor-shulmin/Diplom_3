from data import Url
import allure
import pytest
from page_objects.constructor_page import ConstructorPageBurgers


@pytest.mark.usefixtures('driver', 'user')
class TestConstructor:

    @allure.title('Проверка перехода в раздел "Конструктор"')
    def test_go_to_constructor(self):
        constructor_section = ConstructorPageBurgers(self.driver, self.user)
        constructor_section.go_to_order_feed()

        assert constructor_section.go_to_constructor() == True
        assert constructor_section.driver_current_url() == Url.BASE_PAGE

    @allure.title('Проверка перехода в раздел "Лента заказов"')
    def test_go_to_order_feed(self):
        order_feed_section = ConstructorPageBurgers(self.driver, self.user)

        assert order_feed_section.go_to_order_feed() == True
        assert order_feed_section.driver_current_url() == Url.ORDER_FEED_PAGE

    @allure.title('Проверка загрузки всплывающего окна с описанием ингредиента')
    def test_check_open_ingredient_window(self):
        ingredient_window = ConstructorPageBurgers(self.driver, self.user)

        assert ingredient_window.get_ingredient_info() == True

    @allure.title('Проверка закрытия всплывающего окна с описанием ингредиента')
    def test_check_close_ingredient_window(self):
        ingredient_window = ConstructorPageBurgers(self.driver, self.user)

        assert ingredient_window.close_ingredient_info() == True

    @allure.title('Проверка добавления ингредиентов в заказ и работы счётчиков ингредиентов')
    def test_check_add_ingredients_to_order(self):
        ingredients = ConstructorPageBurgers(self.driver, self.user)
        counters = ingredients.add_ingredients_to_order()

        assert counters[0][0] == 0 and counters[0][1] == 2
        assert counters[1][0] == 0 and counters[1][1] == 1
        assert counters[2][0] == 0 and counters[2][1] == 1

    @allure.title('Проверка оформления заказа авторизованным пользователем')
    def test_check_make_user_order(self):
        user_order = ConstructorPageBurgers(self.driver, self.user)

        assert user_order.make_user_order() == '9999'
