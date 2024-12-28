import allure
from locators.login import LocatorsLogin
from page_objects.base_page import BasePageBurgers
from data import Url


class LoginPageBurgers(BasePageBurgers):

    def __init__(self, driver, user):
        super().__init__(driver)
        self.user = user

    @allure.step('Авторизуем пользователя')
    def make_login(self):
        self.go_to_page(Url.BASE_PAGE)
        self.driver_wait_for_clickable_element(LocatorsLogin.ACCOUNT_BUTTON)
        element = self.driver_find_element(LocatorsLogin.ACCOUNT_BUTTON)
        self.driver_click_element(element)
        self.driver_wait_for_clickable_element(LocatorsLogin.LOGIN_BUTTON)
        element = self.driver_find_element(LocatorsLogin.EMAIL_FIELD)
        self.driver_send_keys_to_element(element, self.user.email)
        element = self.driver_find_element(LocatorsLogin.PASS_FIELD)
        self.driver_send_keys_to_element(element, self.user.password)
        element = self.driver_find_element(LocatorsLogin.LOGIN_BUTTON)
        self.driver_click_element(element)
        self.driver_wait_for_clickable_element(LocatorsLogin.ORDER_BUTTON)
