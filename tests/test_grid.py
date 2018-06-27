from pages.login_page import LoginPage
from pages.device_search_page import SearchPage

class Test_Enter(LoginPage):
    login = LoginPage()

    def test_login(self):
        self.login.login_as("r","1")

class Test_Grid(SearchPage):
    user = SearchPage()

    def test_check_user_name(self):
        assert "Ранд" == self.user.check_user_first_name()
        assert "ал'Тор" == self.user.check_user_last_name()
        print (self.user.check_user_first_name(),self.user.check_user_last_name())

    def test_correct_menu_text(self):
        assert "Майданчик" == self.check_menu_site()
        assert "Обладнання" == self.check_menu_device()
        assert "Ресурси" == self.check_menu_resource()
        assert "Головна" == self.check_menu_main()
        assert "Налаштування" == self.check_menu_settings()

    def test_correct_table_column(self):
        self.table_view()
        assert "Назва" == self.check_table_name()
        assert "Місто" == self.check_table_city()
        assert "Тип" == self.check_table_type()
        assert "Модель" == self.check_table_model()
        assert "Організація" == self.check_table_organization()
        assert "Назва майданчика" == self.check_table_site_name()
        assert "IP адреса" == self.check_table_ip()
        # Check pagination for table view
        self.pagination()
        self.table_view()
        # Check pagination for card view view
        self.pagination()


    def pagination(self):
    # back to card view
        self.table_view()
        result_search_cards = self.check_text_for_result_number()
        assert "Результати пошуку" in result_search_cards
    # Check pagination
        number_of_card_full = self.user.number_device(result_search_cards)
        if number_of_card_full > 30:
            pages = self.number_of_pages(number_of_card_full)
            assert 1 == self.check_active_text_page()
            assert "1" == self.check_text_page()
            assert ">" == self.check_text_next_page()
            assert ">>" == self.check_text_end_page()
            self.click_end_page()
            assert pages == self.check_active_text_page()
            assert "<" == self.check_text_previus_page()
            assert "<<" == self.check_text_start_page()
            self.click_previous_page()
            assert pages-1 == self.check_active_text_page()
            self.click_next_page()
            assert pages == self.check_active_text_page()
            self.click_start_page()
            assert 1 == self.check_active_text_page()
            if self.check_current_view_mode() == "card":
                assert 30 == self.number_cards()
            if self.check_current_view_mode() == "table":
                assert 30 == self.number_rows()
        else:
            assert "1" not in self.check_text_page()
    # Check export

    def export(self):
        pass



    # Check enter the card

    # Check search for search page: number of cards, pagination, sorting, filter option
    def test_display_grid_search_device(self):
        self.close()