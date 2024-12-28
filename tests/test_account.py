from data import Url
import allure
import pytest
from page_objects.account_page import AccountPageBurgers


@pytest.mark.usefixtures('driver', 'user')
class TestAccount:

    @allure.title('Проверка функционала личного кабинета')
    def test_check_account(self):
        user_account = AccountPageBurgers(self.driver, self.user)

        assert user_account.account() == True
        assert user_account.driver_current_url() == Url.LOGIN_PAGE
