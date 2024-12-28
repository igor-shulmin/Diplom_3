import allure
from selenium.webdriver.common.by import By
from locators import LocatorsOrderPage
from page_objects.base_page import BasePageBurgers


class ResetPasswordPageBurgers(BasePageBurgers):

    def __init__(self, driver, order):
        super().__init__(driver)
        self.order = order

    @allure.step('Переходим на страницу восстановления пароля по кнопке "Восстановить пароль"')
    def set_name(self):
        element = self.driver_find_element(LocatorsOrderPage.name_field)
        self.driver_send_keys_to_element(element, self.order.name)

    @allure.step('Вводим почты и кликаем по кнопке "Восстановить"')
    def set_surname(self):
        element = self.driver_find_element(LocatorsOrderPage.surname_field)
        self.driver_send_keys_to_element(element, self.order.surname)

    @allure.step('Кликаем по кнопке "Показать/скрыть пароль"')
    def set_address(self):
        element = self.driver_find_element(LocatorsOrderPage.address_field)
        self.driver_send_keys_to_element(element, self.order.address)
