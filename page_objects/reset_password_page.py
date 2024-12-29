import allure
from data import Url
from locators.reset_password import ResetPassword
from page_objects.base_page import BasePageBurgers


class ResetPasswordPageBurgers(BasePageBurgers):

    def __init__(self, driver, user):
        super().__init__(driver)
        self.user = user

    @allure.step('Переходим на страницу восстановления пароля по кнопке "Восстановить пароль"')
    def go_to_reset_pass_page(self):
        self.user.register_new_user_and_return_login_password()
        self.go_to_page(Url.LOGIN_PAGE)
        self.driver_wait_for_clickable_element(ResetPassword.RESET_PASSWORD_BUTTON)
        element = self.driver_find_element(ResetPassword.RESET_PASSWORD_BUTTON)
        self.driver_scroll_to_element(element)
        self.driver_click_element(element)

    @allure.step('Вводим адрес почты и кликаем по кнопке "Восстановить"')
    def send_mail_and_click_button(self):
        self.driver_wait_for_visibile_element(ResetPassword.RESET_FIELD)
        element = self.driver_find_element(ResetPassword.RESET_FIELD)
        self.driver_send_keys_to_element(element, self.user.email)
        element = self.driver_find_element(ResetPassword.RESET_PASSWORD_BUTTON_2)
        self.driver_click_element(element)

    @allure.step('Кликаем по кнопке "Показать/скрыть пароль"')
    def click_button_show_pass(self):
        self.driver_wait_for_clickable_element(ResetPassword.SHOW_PASS_BUTTON)
        element = self.driver_find_element(ResetPassword.SHOW_PASS_BUTTON)
        self.driver_click_element(element)
        self.driver_wait_for_visibile_element(ResetPassword.RESET_FIELD_ACTIVE)
        if self.driver_find_element(ResetPassword.RESET_FIELD_ACTIVE):

            return True

    @allure.step('Восстановим пароль с использованием почты пользователя')
    def reset_password(self):
        self.go_to_reset_pass_page()
        self.send_mail_and_click_button()
        if self.click_button_show_pass():

            return True
