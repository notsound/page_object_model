from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "It is not a login page"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form does not exist"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form does not exist"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(email)
        passwd_input = self.browser.find_element(*LoginPageLocators.PASSWD_FIELD).send_keys(password)
        passwd_confirm = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWD_FIELD).send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
