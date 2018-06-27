from pages.login_page import LoginPage
from pages.device_search_page import SearchPage

class Test_login(LoginPage):
    login = LoginPage()

    def test_login_local_ldap(self):

        self.login.fill_username_field("R")
        self.login.fill_user_password("1")
        self.login.sign_in()

class Test_Search(SearchPage):
    user = SearchPage()

    def check_user_name(self):
        assert "Ранд" == self.user.check_user_first_name()
        assert "ал'Тор" == self.user.check_user_last_name()

