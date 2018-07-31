from pages.login_page import LoginPage
from pages.device_search_page import SearchPage

class TestFilter(LoginPage, SearchPage):
    login = LoginPage()
    login.login_as('R', '1')
    def test_click_filter(self):
        self.enable_filter()