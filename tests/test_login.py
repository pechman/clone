from pages.login_page import LoginPage
from pages.device_search_page import SearchPage

class Test_login(LoginPage):

    def test_login_local_auth(self):
        self.login_as('R', '1')

class Test_Search(SearchPage):

    def test_check_user_name(self):
        assert "Ранд" == self.check_user_first_name()
        assert "ал'Тор" == self.check_user_last_name()