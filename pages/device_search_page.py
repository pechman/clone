from pages.elements import PageElements
from pages.locators import LoginPageLocators
import math
import os, glob
import time

class SearchPage(PageElements):
    search_page = PageElements()

    # Check user name
    def check_user_first_name(self):
        return self.check_one_element_exists(*LoginPageLocators.USER_INFO_FIRST_NAME).text
    def check_user_last_name(self):
        return self.check_one_element_exists(*LoginPageLocators.USER_INFO_LAST_NAME).text

    # Check menu-item's name
    def check_menu_device(self):
        return self.check_one_element_exists(*LoginPageLocators.MENU_DEVICE).text

    def check_menu_site(self):
        return self.check_one_element_exists(*LoginPageLocators.MENU_SITE).text

    def check_menu_resource(self):
        return self.check_one_element_exists(*LoginPageLocators.MENU_RESOURCE).text

    def check_menu_main(self):
        return self.check_one_element_exists(*LoginPageLocators.MENU_MAIN).text

    def check_menu_settings(self):
        return self.check_one_element_exists(*LoginPageLocators.MENU_SETTINGS).text

    def check_search_head(self):
        return self.check_one_element_exists(*LoginPageLocators.SEARCH_BOX_HEAD).text

    def check_search_grid(self):
        return self.check_one_element_exists(*LoginPageLocators.SEARCH_BOX_GRID).text

    def check_search_results(self):
        return self.check_one_element_exists(*LoginPageLocators.SEARCH_RESULT).text

    # Check table_view
    def table_view(self):
        return self.click(*LoginPageLocators.VIEW_MODE_ICON)

    # Check column name for table
    def check_table_name(self):
        return self.check_one_element_exists(*LoginPageLocators.TABLE_NAME).text

    def check_table_city(self):
        return self.check_one_element_exists(*LoginPageLocators.TABLE_CITY).text

    def check_table_type(self):
        return self.check_one_element_exists(*LoginPageLocators.TABLE_TYPE).text

    def check_table_model(self):
        return self.check_one_element_exists(*LoginPageLocators.TABLE_MODEL).text

    def check_table_organization(self):
        return self.check_one_element_exists(*LoginPageLocators.TABLE_ORGANIZATION).text

    def check_table_site_name(self):
        return self.check_one_element_exists(*LoginPageLocators.TABLE_SITE_NAME).text

    def check_table_ip(self):
        return self.check_one_element_exists(*LoginPageLocators.TABLE_IP).text

    def check_text_for_result_number(self):
        return self.check_one_element_exists(*LoginPageLocators.SEARCH_RESULT).text

    def number_device(self, text_number_device):
        number_device = int(''.join(c for c in text_number_device if c.isdigit()))
        print("number of devices:", number_device)
        return number_device

    def number_cards(self):
        number_card = len(self.check_set_elements_exist(*LoginPageLocators.CARD_LIST))
        return number_card

    def number_rows(self):
        number_rows = len(self.check_set_elements_exist(*LoginPageLocators.ROW_LIST))
        return number_rows

    def number_of_pages(self, number):
        pages = math.ceil(number/30)
        print("number of pages:", pages)
        return pages

    def check_active_text_page(self):
        return int(self.check_one_element_exists(*LoginPageLocators.PAGINATION_ACTIVE_PAGE).text)

    def check_text_page(self):
        return self.check_one_element_exists(*LoginPageLocators.PAGINATION_PAGE).text

    def check_text_next_page(self):
        return self.check_one_element_exists(*LoginPageLocators.PAGINATION_ARROWHEAD_FORWARD).text

    def check_text_end_page(self):
        return self.check_one_element_exists(*LoginPageLocators.PAGINATION_ARROWHEAD_FORWARD_END).text

    def check_text_previus_page(self):
        return self.check_one_element_exists(*LoginPageLocators.PAGINATION_ARROWHEAD_BACK).text

    def check_text_start_page(self):
        return self.check_one_element_exists(*LoginPageLocators.PAGINATION_ARROWHEAD_BACK_START).text

    def click_next_page(self):
        return self.click(*LoginPageLocators.PAGINATION_ARROWHEAD_FORWARD)

    def click_end_page(self):
        return self.click(*LoginPageLocators.PAGINATION_ARROWHEAD_FORWARD_END)

    def click_previous_page(self):
        return self.click(*LoginPageLocators.PAGINATION_ARROWHEAD_BACK)

    def click_start_page(self):
        return self.click(*LoginPageLocators.PAGINATION_ARROWHEAD_BACK_START)

    def check_current_view_mode(self):
        if len(self.check_set_elements_exist(*LoginPageLocators.VIEW_MODE_CARDS))<1:
            mode = "table"
        if len(self.check_set_elements_exist(*LoginPageLocators.VIEW_MODE_TABLE))<1:
            mode = "card"
        return mode

    def click_download_csv(self):
        for file in glob.glob(r'A:\download_csv\*.csv'):
            os.remove(file)
        self.click(*LoginPageLocators.BUTTON_EXPORT_CSV)
        time.sleep(1)
        self.click(*LoginPageLocators.POPUP_EXPORT_CSV)
        time.sleep(2)
        filelinks = glob.glob(r'A:\download_csv\*.csv')
        filescv = filelinks[0]
        inf_for_filesize = os.path.getsize(filescv)
        list = []
        list.append(inf_for_filesize)
        list.append(filescv)
        return list
        # Проверка количества строк в файле и количества карточек найденых в системе.

    def check_equivalence_csv_grid(self, filescv):
        with open(filescv, newline='', encoding="utf-8") as my_file:
            row = [line.strip() for line in my_file]
            result = []
            for i in range(len(row)):
                if """;""" in row[i]:
                    result.append(row[i])
            number_cards_row = len(result) - 1
        # Перевод в табличный вид грида
        if self.check_current_view_mode()=="card":
            self.table_view()
            time.sleep(1)
            if number_cards_row > 30:
                pages = math.ceil(number_cards_row / 30)
                for p in range(pages):
                    time.sleep(1)
                    # Проверка наличия нужных карточек и сохранения их сортировки в файле
                    device_names_one_page = self.check_set_elements_exist(*LoginPageLocators.NAME_CARDS_SET_FOR_PAGE)
                    device_names = []
                    for w in range(len(device_names_one_page)):
                        device_names.append(device_names_one_page[w].text)
                    for k in range(len(device_names)):
                        assert device_names[k] in result[k + 1 + 30 * p]
                    time.sleep(1)
                    if p != (pages - 1):
                        self.click(*LoginPageLocators.PAGINATION_ARROWHEAD_FORWARD)
        return number_cards_row

    def open_device_card(self):
        if self.check_current_view_mode()=="card":
            self.table_view()
        self.click(*LoginPageLocators.NAME_FIRST_TD_TABLE)

    def menu_not_available(self):
        exist = 0
        try:
            self.check_one_element_exists(*LoginPageLocators.BOTTOM_AREA_MAIN)
            self.check_one_element_exists(*LoginPageLocators.BOTTOM_AREA_SETTINGS)
            self.check_one_element_exists(*LoginPageLocators.MENU_RESOURCE)
            self.click(*LoginPageLocators.ICON_ADD_CARD_SITE_DEVICE)
            self.check_one_element_exists(*LoginPageLocators.ADD_AREA_SITE_DEVICE)
            self.check_one_element_exists(*LoginPageLocators.ADD_AREA_SITE)
            self.check_one_element_exists(*LoginPageLocators.ADD_AREA_DEVICE)
            exist = 1
        except:
            exist = 0
        finally:
            return exist

    def enable_filter(self):
        self.click(*LoginPageLocators.FILTER_ICON)
        self.click(*LoginPageLocators.FILTER_TYPE_ROUTER)
        self.click(*LoginPageLocators.OPTION_TYPE_LOCATOR)



