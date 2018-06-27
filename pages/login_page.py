from pages.elements import PageElements
from pages.locators import LoginPageLocators

class LoginPage(PageElements):

    login_page = PageElements()

    def fill_username_field(self, name):
        self.login_page.fill(name, *LoginPageLocators.USERNAME_FIELD)

    def fill_user_password(self, user_password):
        self.login_page.fill(user_password, *LoginPageLocators.PASSWORD_FIELD)

    def sign_in(self):
        self.login_page.click(*LoginPageLocators.SUBMIT_BTN)

    def login_as(self, name, user_password):
        self.login_page.fill(name, *LoginPageLocators.USERNAME_FIELD)
        self.login_page.fill(user_password, *LoginPageLocators.PASSWORD_FIELD)
        self.login_page.click(*LoginPageLocators.SUBMIT_BTN)