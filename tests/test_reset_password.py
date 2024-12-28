import allure
import pytest
from data import Answers
from locators import Locators
from page_objects.reset_password_page import ResetPasswordPageBurgers


@pytest.mark.usefixtures('driver')
class TestPasswordRecovery:

    @allure.title('Проверка функции восстановления пароля')
    def test_check_reset_password(self, question_locator, answer_locator, answer_text):
        reset_password = ResetPasswordPageBurgers(self.driver)
        reset_password.go_to_page(Url.LOGIN_PAGE)


        assert answer_on_question == answer_text
