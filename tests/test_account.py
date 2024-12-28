from data import Url
import allure
import pytest
from page_objects.account_page import AccountPageBurgers


@pytest.mark.usefixtures('driver', 'user')
class TestGoToAndFromAccount:

    @allure.title('Проверка функции входа в аккаунт пользователя')
    def test_check_account_login(self):
        account_login = AccountPageBurgers(self.driver, self.user)

        assert account_login.go_to_account_page() == True
        assert account_login.driver_current_url() == Url.PROFILE_PAGE

    @allure.title('Проверка раздела "История заказов" пользователя')
    def test_check_account_order_history(self):
        account_history = AccountPageBurgers(self.driver, self.user)
        account_history.make_user_order(add_ingr=True)

        assert len(account_history.go_to_order_history()) == 1
        assert account_history.driver_current_url() == Url.PROFILE_ORDER_HISTORY_PAGE

    @allure.title('Проверка функции выхода из аккаунта пользователя')
    def test_check_account_logout(self):
        account_logout = AccountPageBurgers(self.driver, self.user)

        assert account_logout.go_from_account_page() == True
        assert account_logout.driver_current_url() == Url.LOGIN_PAGE
