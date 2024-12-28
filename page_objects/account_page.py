import allure
from locators.account import LocatorsAccount
from page_objects.base_page import BasePageBurgers
from page_objects.login_page import LoginPageBurgers


class AccountPageBurgers(BasePageBurgers):

    def __init__(self, driver, user):
        super().__init__(driver)
        self.user = user

    @allure.step('Переходим по клику на страницу личного кабинета')
    def go_to_account_page(self):
        LoginPageBurgers.make_login(self)

        self.driver_wait_for_clickable_element(LocatorsAccount.ACCOUNT_BUTTON)
        element = self.driver_find_element(LocatorsAccount.ACCOUNT_BUTTON)
        self.driver_click_element(element)
        self.driver_wait_for_clickable_element(LocatorsAccount.ORDER_HISTORY_LINK)
        if self.driver_find_element(LocatorsAccount.ORDER_HISTORY_LINK):

            return True

    @allure.step('Переходим в раздел "История заказов"')
    def go_to_order_history(self, order=False):
        element = self.driver_find_element(LocatorsAccount.ORDER_HISTORY_LINK)
        self.driver_click_element(element)
        if order:
            self.driver_wait_for_clickable_element(LocatorsAccount.ORDER_HISTORY_PROFILE_LIST)
            elements = self.driver_find_elements(LocatorsAccount.ORDER_HISTORY_PROFILE_ID)
            elements = [element.text[2:8] for element in elements]
            return elements
        else:
            return self.driver_find_element(LocatorsAccount.ORDER_HISTORY_LINK_ACTIVE)

    @allure.step('Выходим из аккаунта')
    def go_from_account_page(self):
        self.driver_wait_for_clickable_element(LocatorsAccount.LOGOUT_BUTTON)
        element = self.driver_find_element(LocatorsAccount.LOGOUT_BUTTON)
        self.driver_click_element(element)
        self.driver_wait_for_clickable_element(LocatorsAccount.LOGIN_BUTTON)
        if self.driver_find_element(LocatorsAccount.LOGIN_BUTTON):

            return True

    @allure.step('Получаем список заказов пользователя')
    def get_user_order_list(self):
        self.driver_wait_for_clickable_element(LocatorsAccount.ACCOUNT_BUTTON)
        element = self.driver_find_element(LocatorsAccount.ACCOUNT_BUTTON)
        self.driver_click_element(element)

        self.driver_wait_for_clickable_element(LocatorsAccount.ORDER_HISTORY_LINK)
        element = self.driver_find_element(LocatorsAccount.ORDER_HISTORY_LINK)
        self.driver_click_element(element)

        self.driver_wait_for_clickable_element(LocatorsAccount.ORDER_HISTORY_PROFILE_ID)
        elements = self.driver_find_elements(LocatorsAccount.ORDER_HISTORY_PROFILE_ID)
        user_order_list = [element.text[2:8] for element in elements]

        return user_order_list

    @allure.step('Работаем в личном кабинете')
    def account(self):
        self.go_to_account_page()
        self.go_to_order_history()
        self.go_from_account_page()

        return True
