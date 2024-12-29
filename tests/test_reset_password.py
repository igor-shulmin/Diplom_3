import allure
import pytest
from page_objects.reset_password_page import ResetPasswordPageBurgers


@pytest.mark.usefixtures('driver', 'user')
class TestPasswordRecovery:

    @allure.title('Проверка функции восстановления пароля')
    def test_check_reset_password(self):
        reset_pass = ResetPasswordPageBurgers(self.driver, self.user)

        assert reset_pass.reset_password() == True
