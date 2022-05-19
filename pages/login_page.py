from faker import Faker

from .base_page import BasePage
from .locators import LoginPageLocators

fake = Faker()

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_register_new_user(self):
        # действие по переходу к регистрации
        self.should_be_login_link()
        self.go_to_login_page()

        # проверка элементов регистрации
        self.should_be_login_url()
        self.should_be_register_form()
        self.should_be_email_form()
        self.should_be_password_form()
        self.should_be_repeat_password_form()
        self.should_be_btn_register()

        # регистрация нового пользователя
        self.browser.find_element(*LoginPageLocators.EMAIL_FORM).send_keys(fake.email())
        self.browser.find_element(*LoginPageLocators.PASSWORD_FORM).send_keys("edfrvbhjnmu")
        self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD_FORM).send_keys("edfrvbhjnmu")
        self.browser.find_element(*LoginPageLocators.BTN_REGISTER).click()
        
        # проверка что пользователь залогинент
        self.register_new_user()
        self.should_be_authorized_user()
        
    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "'login' not in current url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Don't have login form"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Don't have register form"
    
    def should_be_email_form(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_FORM), "Email form not found"

    def should_be_password_form(self):
        assert self.is_element_present(*LoginPageLocators.PASSWORD_FORM), "Password form not found"

    def should_be_repeat_password_form(self):
        assert self.is_element_present(*LoginPageLocators.REPEAT_PASSWORD_FORM), "Repeat password form not found"

    def should_be_btn_register(self):
        assert self.is_element_present(*LoginPageLocators.BTN_REGISTER), "Button register not found"

    def register_new_user(self):
        assert self.is_element_present(*LoginPageLocators.SUCCESS_MESSAGES_REGISTER), "Succes message not found"