from pages.login_page import LoginPage
from pages.device_search_page import SearchPage
from pages.device_card_page import CardPage

class Test_Enter(LoginPage):
    login = LoginPage()
    login.login_as('inv_operator_01_pechora', '1')

class Test_Grid(SearchPage):
    def test_text_navigation(self):
        exist = self.menu_not_available()
        assert 0 == exist
        #нужно проверить что отстуствует меню ресурсы/главная/настройки/отсутствует опция для создания площадок/оборудование
    def test_card_open(self):
        #нужно сделать выборку по сетевым девайсам
        self.enable_filter()
        self.open_device_card()

class Test_Card(CardPage):

   card = CardPage()
        # Check names for card's menu
        #не должно быть вкладки доступ/кнопок
        # проверить названия закладок

   def test_ua_text(self):
        self.ua_text()
        self.change_language_to_ru()
        self.ru_text()
        self.change_language_to_en()
        self.en_text()

   def test_ru_text(self):
        self.change_language_to_ru()
        self.ru_text()
        self.change_language_to_ru()
        self.ru_text()
        self.change_language_to_en()
        self.en_text()

   def test_en_text(self):
       self.change_language_to_en()
       self.en_text()
       self.change_language_to_ru()
       self.ru_text()
       self.change_language_to_ua()
       self.ua_text()
       self.close()

   def ua_text(self):
       assert "ПАРАМЕТРИ" == self.check_text_parameters()
       assert 0 == self.menu_parameters_not_available('ua')
       assert 0 == self.edit_button_not_available()

   def ru_text(self):
       assert "ПАРАМЕТРЫ" == self.check_text_parameters()
       assert 0 == self.menu_parameters_not_available('ua')
       assert 0 == self.edit_button_not_available()

   def en_text(self):
       assert "PARAMETERS" == self.check_text_parameters()
       assert 0 == self.menu_parameters_not_available('en')
       assert 0 == self.edit_button_not_available()
