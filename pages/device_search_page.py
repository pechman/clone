from pages.elements import PageElements
from pages.locators import LoginPageLocators
import math
import os, glob
import time

class SearchPage(PageElements):
    search_page = PageElements()

    # Check user name
    def check_user_first_name(self):
        return self.search_page.check_user_first_name(*LoginPageLocators.USER_INFO_FIRST_NAME)

    def check_user_last_name(self):
        return self.search_page.check_user_last_name(*LoginPageLocators.USER_INFO_LAST_NAME)

    # Check menu-item's name
    def check_menu_device(self):
        return self.search_page.check_text_for_menu(*LoginPageLocators.MENU_DEVICE)

    def check_menu_site(self):
        return self.search_page.check_text_for_menu(*LoginPageLocators.MENU_SITE)

    def check_menu_resource(self):
        return self.search_page.check_text_for_menu(*LoginPageLocators.MENU_RESOURCE)

    def check_menu_main(self):
        return self.search_page.check_text_for_menu(*LoginPageLocators.MENU_MAIN)

    def check_menu_settings(self):
        return self.search_page.check_text_for_menu(*LoginPageLocators.MENU_SETTINGS)

    def check_search_head(self):
        return self.search_page.check_text_for_menu(*LoginPageLocators.SEARCH_BOX_HEAD)

    def check_search_grid(self):
        return self.search_page.check_text_for_menu(*LoginPageLocators.SEARCH_BOX_GRID)

    def check_search_results(self):
        return self.search_page.check_text_for_menu(*LoginPageLocators.SEARCH_RESULT)

    # Check table_view
    def table_view(self):
        return self.click(*LoginPageLocators.VIEW_MODE_ICON)

    # Check column name for table
    def check_table_name(self):
        return self.search_page.check_text_for_table(*LoginPageLocators.TABLE_NAME)

    def check_table_city(self):
        return self.search_page.check_text_for_table(*LoginPageLocators.TABLE_CITY)

    def check_table_type(self):
        return self.search_page.check_text_for_table(*LoginPageLocators.TABLE_TYPE)

    def check_table_model(self):
        return self.search_page.check_text_for_table(*LoginPageLocators.TABLE_MODEL)

    def check_table_organization(self):
        return self.search_page.check_text_for_table(*LoginPageLocators.TABLE_ORGANIZATION)

    def check_table_site_name(self):
        return self.search_page.check_text_for_table(*LoginPageLocators.TABLE_SITE_NAME)

    def check_table_ip(self):
        return self.search_page.check_text_for_table(*LoginPageLocators.TABLE_IP)

    def check_text_for_result_number(self):
        return self.search_page.check_number(*LoginPageLocators.SEARCH_RESULT)

    def number_device(self, text_number_device):
        number_device = int(''.join(c for c in text_number_device if c.isdigit()))
        print("number of devices:", number_device)
        return number_device

    def number_cards(self):
        number_card = len(self.search_page.card_list(*LoginPageLocators.CARD_LIST))
        return number_card

    def number_rows(self):
        number_rows = len(self.search_page.card_list(*LoginPageLocators.ROW_LIST))
        return number_rows

    def number_of_pages(self, number):
        pages = math.ceil(number/30)
        print("number of pages:", pages)
        return pages

    def check_active_text_page(self):
        return self.search_page.active_page(*LoginPageLocators.PAGINATION_ACTIVE_PAGE)

    def check_text_page(self):
        return self.search_page.check_text_for_table(*LoginPageLocators.PAGINATION_PAGE)

    def check_text_next_page(self):
        return self.search_page.check_text_for_table(*LoginPageLocators.PAGINATION_ARROWHEAD_FORWARD)

    def check_text_end_page(self):
        return self.search_page.check_text_for_table(*LoginPageLocators.PAGINATION_ARROWHEAD_FORWARD_END)

    def check_text_previus_page(self):
        return self.search_page.check_text_for_table(*LoginPageLocators.PAGINATION_ARROWHEAD_BACK)

    def check_text_start_page(self):
        return self.search_page.check_text_for_table(*LoginPageLocators.PAGINATION_ARROWHEAD_BACK_START)

    def click_next_page(self):
        return self.search_page.click(*LoginPageLocators.PAGINATION_ARROWHEAD_FORWARD)

    def click_end_page(self):
        return self.search_page.click(*LoginPageLocators.PAGINATION_ARROWHEAD_FORWARD_END)

    def click_previous_page(self):
        return self.search_page.click(*LoginPageLocators.PAGINATION_ARROWHEAD_BACK)

    def click_start_page(self):
        return self.search_page.click(*LoginPageLocators.PAGINATION_ARROWHEAD_BACK_START)

    def check_current_view_mode(self):
        if len(self.search_page.view_active_mode(*LoginPageLocators.VIEW_MODE_CARDS))<1:
            mode = "table"
        if len(self.search_page.view_active_mode(*LoginPageLocators.VIEW_MODE_TABLE))<1:
            mode = "card"
        return mode

    def click_download_csv(self):
        for file in glob.glob(r'A:\download_csv\*.csv'):
            os.remove(file)
        self.search_page.click(*LoginPageLocators.BUTTON_EXPORT_CSV)
        time.sleep(1)
        self.search_page.click(*LoginPageLocators.POPUP_EXPORT_CSV)
        time.sleep(1)
        filelinks = glob.glob(r'A:\download_csv\*.csv')
        filescv = filelinks[0]
        inf_for_filesize = os.path.getsize(filescv)
        assert inf_for_filesize > 0
        # Проверка количества строк в файле и количества карточек найденых в системе.
        with open(filescv, newline='', encoding="utf-8") as my_file:
            row = [line.strip() for line in my_file]
            result = []
            for i in range(len(row)):
                if """;""" in row[i]:
                    result.append(row[i])
            number_cards = len(result) - 1
        assert numbers_device == number_cards
        print("число строк в CSV файле:", number_cards)
        print("количество карточек:", numbers_device)
        # Перевод в табличный вид грида
        table_icon = driver.find_element_by_xpath("//i[@class='fa fa-table']")
        table_icon.click()
        if numbers_device > 30:
            pages = math.ceil(numbers_device / 30)

            for p in range(pages):
                print("текущая страница=", p + 1)
                time.sleep(1)
                # Проверка наличия нужных карточек и сохранения их сортировки в файле
                device_names_one_page = driver.find_elements_by_xpath("//div/table/tbody/tr/td[1]")
                device_names = []
                for w in range(len(device_names_one_page)):
                    device_names.append(device_names_one_page[w].text)
                for k in range(len(device_names)):
                    print("p страница=", p + 1)
                    print("k номер в таблице=", k)
                    print("название карточки, что соответвует строке в файле:", device_names[k])
                    print("проверяемая строка в файле", result[k + 1 + p * 30])
                    assert device_names[k] in result[k + 1 + 30 * p]
                time.sleep(1)
                if p != (pages - 1):
                    driver.find_element_by_xpath("//html//ul[3]/li[1]").click()
