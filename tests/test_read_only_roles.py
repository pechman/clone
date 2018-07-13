from pages.login_page import LoginPage
from pages.device_search_page import SearchPage
from pages.device_card_page import CardPage

class Test_Enter(LoginPage):
    login = LoginPage()
    login.login_as('inv_operator_01_pechora', '1')

class Test_Grid(SearchPage):
    def test_text_navigation(self):
        pass
        #нужно проверить что отстуствует меню ресурсы/главная/настройки/отсутствует опция для создания площадок/оборудование
    def test_card_open(self):
        #нужно сделать выборку по сетевым девайсам
        self.open_device_card()

class Test_Card(CardPage):
        # Check names for card's menu
   card = CardPage()
        #не должно быть вкладки доступ/кнопок
        # проверить названия закладок
        
   def test_ua_text(self):
        self.ua_text()
        self.click_button_edit()
        self.change_language_to_ru()
        self.click_button_cancel()
        self.ru_text()
        self.click_button_edit()
        self.change_language_to_en()
        self.click_button_submit()
        self.en_text()

   def test_ru_text(self):
        self.change_language_to_ru()
        self.ru_text()
        self.click_button_edit()
        self.change_language_to_ru()
        self.click_button_submit()
        self.ru_text()
        self.click_button_edit()
        self.change_language_to_en()
        self.click_button_cancel()
        self.en_text()

   def test_en_text(self):
       self.change_language_to_en()
       self.en_text()
       self.proceed_to_tab_access()
       self.click_button_edit()
       self.change_language_to_ru()
       self.proceed_to_tab_parameters()
       self.ru_text()
       self.proceed_to_tab_menu_first()
       self.change_language_to_ua()
       self.proceed_to_tab_history_previous()
       self.ua_text()

       self.close()

   def ua_text(self):
       assert "ПАРАМЕТРИ" == self.check_text_parameters()
       assert "ДОСТУП" == self.check_text_access()
       assert "ІНТЕРФЕЙСИ" == self.check_text_interface()
       assert "ШАССІ" == self.check_text_chassis()
       assert "ТОПОЛОГІЯ" == self.check_text_topology()
       assert "ДОКУМЕНТИ" == self.check_text_documents()
       assert "РЕДАГУВАТИ" == self.check_text_edit_button()
       assert "Тип:" == self.check_text_type()
       assert "Модель:" == self.check_text_model()
       assert "Місто:" == self.check_text_city()
       assert "Майданчик:" == self.check_text_site()

       # Check names for card's parameters
       assert "Загальна інформація" == self.check_text_general_information()
       assert "Модель:" == self.check_text_general_model()
       assert "Статус:" == self.check_text_status()
       assert "Код обладнання:" == self.check_text_equipment_code()
       assert "Серійний номер:" == self.check_text_serial_number()
       assert "Інвентарний номер:" == self.check_text_inventory_number()
       assert "Організація:" == self.check_text_organization()
       assert "Дата встановлення:" == self.check_text_installation_date()
       assert "Дата початку експлуатації:" == self.check_text_start_up_date()
       assert "Опис:" == self.check_text_description()

       assert "Загальні параметри" == self.check_text_general_parameters()
       assert "IP адреса:" == self.check_text_ip()
       assert "MAC адреса:" == self.check_text_mac()
       assert "Тип ОС:" == self.check_text_os_type()
       assert "Версія ОС:" == self.check_text_os_version()

       assert "Майданчик" == self.check_text_general_site()
       assert "Назва майданчика:" == self.check_text_site_name()
       assert "Адреса:" == self.check_text_address()
       assert "Тип майданчика:" == self.check_text_site_type()
       assert "Місто:" == self.check_text_site_city()
       assert "Ролі" == self.check_text_role()

   def ru_text(self):
       assert "ПАРАМЕТРЫ" == self.check_text_parameters()
       assert "ДОСТУП" == self.check_text_access()
       assert "ИНТЕРФЕЙСЫ" == self.check_text_interface()
       assert "ШАССИ" == self.check_text_chassis()
       assert "ТОПОЛОГИЯ" == self.check_text_topology()
       assert "ДОКУМЕНТЫ" == self.check_text_documents()
       assert "РЕДАКТИРОВАТЬ" == self.check_text_edit_button()
       assert "Тип:" == self.check_text_type()
       assert "Модель:" == self.check_text_model()
       assert "Город:" == self.check_text_city()
       assert "Площадка:" == self.check_text_site()

       # Check names for card's parameters
       assert "Общая информация" == self.check_text_general_information()
       assert "Модель:" == self.check_text_general_model()
       assert "Статус:" == self.check_text_status()
       assert "Код оборудования:" == self.check_text_equipment_code()
       assert "Серийный номер:" == self.check_text_serial_number()
       assert "Инвентарный номер:" == self.check_text_inventory_number()
       assert "Организация:" == self.check_text_organization()
       assert "Дата установки:" == self.check_text_installation_date()
       assert "Дата начала эксплуатации:" == self.check_text_start_up_date()
       assert "Описание:" == self.check_text_description()

       assert "Общие параметры" == self.check_text_general_parameters()
       assert "IP адрес:" == self.check_text_ip()
       assert "MAC адрес:" == self.check_text_mac()
       assert "Тип ОС:" == self.check_text_os_type()
       assert "Версия ОС:" == self.check_text_os_version()

       assert "Площадка" == self.check_text_general_site()
       assert "Название площадки:" == self.check_text_site_name()
       assert "Адрес:" == self.check_text_address()
       assert "Тип площадки:" == self.check_text_site_type()
       assert "Город:" == self.check_text_site_city()
       assert "Роли" == self.check_text_role()

   def en_text(self):
       assert "PARAMETERS" == self.check_text_parameters()
       assert "ACCESS" == self.check_text_access()
       assert "INTERFACE" == self.check_text_interface()
       assert "CHASSIS" == self.check_text_chassis()
       assert "TOPOLOGY" == self.check_text_topology()
       assert "DOCUMENTS" == self.check_text_documents()
       assert "EDIT" == self.check_text_edit_button()
       assert "Type:" == self.check_text_type()
       assert "Model:" == self.check_text_model()
       assert "City:" == self.check_text_city()
       assert "Site:" == self.check_text_site()

       # Check names for card's parameters
       assert "General information" == self.check_text_general_information()
       assert "Model:" == self.check_text_general_model()
       assert "Status:" == self.check_text_status()
       assert "Equipment code:" == self.check_text_equipment_code()
       assert "Serial number:" == self.check_text_serial_number()
       assert "Inventory number:" == self.check_text_inventory_number()
       assert "Organization:" == self.check_text_organization()
       assert "Installation date:" == self.check_text_installation_date()
       assert "Start-up Date:" == self.check_text_start_up_date()
       assert "Description:" == self.check_text_description()

       assert "General parameters" == self.check_text_general_parameters()
       assert "IP address:" == self.check_text_ip()
       assert "MAC address:" == self.check_text_mac()
       assert "OS type:" == self.check_text_os_type()
       assert "OS version:" == self.check_text_os_version()

       assert "Site" == self.check_text_general_site()
       assert "Site Name:" == self.check_text_site_name()
       assert "Address:" == self.check_text_address()
       assert "Site type:" == self.check_text_site_type()
       assert "City:" == self.check_text_site_city()
       assert "Roles" == self.check_text_role()