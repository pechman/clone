from pages.elements import PageElements
from pages.locators import LoginPageLocators


class CardPage(PageElements):
    card_page = PageElements()

    def click_button_edit(self):
        return self.click(*LoginPageLocators.CARD_DEVICE_EDIT)

    def click_button_submit(self):
        return self.click(*LoginPageLocators.CARD_DEVICE_SUBMIT)

    def enter_button(self):
        self.enter_key(*LoginPageLocators.CARD_DEVICE_SUBMIT)

    def click_button_cancel(self):
        return self.click(*LoginPageLocators.CARD_DEVICE_CANCEL)

    def esc_button(self):
        self.ecs_key(*LoginPageLocators.CARD_DEVICE_CANCEL)

    # Check card-item's name
    def check_text_parameters(self):
        return self.check_one_element_exists(*LoginPageLocators.CARD_DEVICE_PARAMETERS).text

    def check_text_access(self):
        return self.check_one_element_exists(*LoginPageLocators.CARD_DEVICE_ACCESS).text

    def check_text_interface(self):
        return self.check_one_element_exists(*LoginPageLocators.CARD_DEVICE_INTERFACE).text

    def check_text_chassis(self):
        return self.check_one_element_exists(*LoginPageLocators.CARD_DEVICE_CHASSIS).text

    def check_text_topology(self):
        return self.check_one_element_exists(*LoginPageLocators.CARD_DEVICE_TOPOLOGY).text

    def check_text_documents(self):
        return self.check_one_element_exists(*LoginPageLocators.CARD_DEVICE_DOCUMENTS).text

    # button edit text
    def check_text_edit_button(self):
        return self.check_one_element_exists(*LoginPageLocators.CARD_DEVICE_EDIT).text

    # card description
    def check_text_name(self):
        return self.check_one_element_exists(*LoginPageLocators.CARD_DEVICE_NAME).text

    def check_text_type(self):
        return self.check_one_element_exists(*LoginPageLocators.CARD_DEVICE_TYPE).text

    def check_text_model(self):
        return self.check_one_element_exists(*LoginPageLocators.CARD_DEVICE_MODEL).text

    def check_text_city(self):
        return self.check_one_element_exists(*LoginPageLocators.CARD_DEVICE_CITY).text

    def check_text_site(self):
        return self.check_one_element_exists(*LoginPageLocators.CARD_DEVICE_SITE).text

    # Check names for card's general information
    def check_text_general_information(self):
        return self.check_one_element_exists(*LoginPageLocators.CARD_DEVICE_GENERAL_INFORMATION).text

    def check_text_general_model(self):
        return self.check_one_element_exists(*LoginPageLocators.CARD_DEVICE_GEN_MODEL).text

    def check_text_status(self):
        return self.check_one_element_exists(*LoginPageLocators.CARD_DEVICE_GEN_STATUS).text

    def check_text_equipment_code(self):
        return self.check_one_element_exists(*LoginPageLocators.CARD_DEVICE_GEN_EQUIPMENT_CODE).text

    def check_text_serial_number(self):
        return self.check_one_element_exists(*LoginPageLocators.CARD_DEVICE_GEN_SERIAL_NUMBER).text

    def check_text_inventory_number(self):
        return self.check_one_element_exists(*LoginPageLocators.CARD_DEVICE_GEN_INVENTORY_NUMBER).text

    def check_text_organization(self):
        return self.check_one_element_exists(*LoginPageLocators.CARD_DEVICE_GEN_ORGANIZATION).text

    def check_text_installation_date(self):
        return self.check_one_element_exists(*LoginPageLocators.CARD_DEVICE_GEN_INSTALLATION_DATE).text

    def check_text_start_up_date(self):
        return self.check_one_element_exists(*LoginPageLocators.CARD_DEVICE_GEN_START_UP_DATE).text

    def check_text_description(self):
        return self.check_one_element_exists(*LoginPageLocators.CARD_DEVICE_GEN_DESCRIPTION).text

    # Check names for card's general parameters

    def check_text_general_parameters(self):
        return self.check_one_element_exists(*LoginPageLocators.CARD_DEVICE_GEN_PAR).text

    def check_text_ip(self):
        return self.check_one_element_exists(*LoginPageLocators.CARD_DEVICE_GEN_PAR_IP).text

    def check_text_mac(self):
        return self.check_one_element_exists(*LoginPageLocators.CARD_DEVICE_GEN_PAR_MAC).text

    def check_text_os_type(self):
        return self.check_one_element_exists(*LoginPageLocators.CARD_DEVICE_GEN_PAR_OS_TYPE).text

    def check_text_os_version(self):
        return self.check_one_element_exists(*LoginPageLocators.CARD_DEVICE_GEN_PAR_OS_VERSION).text

    # Check names for card's general parameters

    def check_text_general_site(self):
        return self.check_one_element_exists(*LoginPageLocators.CARD_DEVICE_SITE_SITE).text

    def check_text_site_name(self):
        return self.check_one_element_exists(*LoginPageLocators.CARD_DEVICE_SITE_SITE_NAME).text

    def check_text_address(self):
        return self.check_one_element_exists(*LoginPageLocators.CARD_DEVICE_SITE_ADDRESS).text

    def check_text_site_type(self):
        return self.check_one_element_exists(*LoginPageLocators.CARD_DEVICE_SITE_SITE_TYPE).text

    def check_text_site_city(self):
        return self.check_one_element_exists(*LoginPageLocators.CARD_DEVICE_SITE_CITY).text

    def check_text_role(self):
        return self.check_one_element_exists(*LoginPageLocators.CARD_DEVICE_ROLES).text

    # Change language
    def change_language_to_ua(self):
        self.click(*LoginPageLocators.ICON_CHANGE_LANGUAGE)
        self.click(*LoginPageLocators.ICON_UA_LANGUAGE)

    def change_language_to_ru(self):
        self.click(*LoginPageLocators.ICON_CHANGE_LANGUAGE)
        self.click(*LoginPageLocators.ICON_RU_LANGUAGE)

    def change_language_to_en(self):
        self.click(*LoginPageLocators.ICON_CHANGE_LANGUAGE)
        self.click(*LoginPageLocators.ICON_EN_LANGUAGE)

    #Change active tab for card
    def proceed_to_tab_access(self):
        self.click(*LoginPageLocators.CARD_DEVICE_ACCESS)

    def proceed_to_tab_interface(self):
        self.click(*LoginPageLocators.CARD_DEVICE_INTERFACE)

    def proceed_to_tab_parameters(self):
        self.click(*LoginPageLocators.CARD_DEVICE_PARAMETERS_INACTIVE)

    def proceed_to_tab_menu_first(self):
        self.click(*LoginPageLocators.MENU_TAB_FIRST)

    def proceed_to_tab_history_previous(self):
        self.click(*LoginPageLocators.TAB_PREVIOUS)

    def menu_parameters_not_available(self, locator):
        exist = 0
        if locator == 'ua':
            try:
                self.check_one_element_exists(*LoginPageLocators.CARD_DEVICE_ACCESS_TEXT_UA)
                exist = 1
            except:
                exist = 0
            finally:
                return exist
        if locator == 'en':
            try:
                self.check_one_element_exists(*LoginPageLocators.CARD_DEVICE_ACCESS_TEXT_EN)
                exist = 1
            except:
                exist = 0
            finally:
                return exist

    def edit_button_not_available(self):
        exist = 1
        try:
            self.check_one_element_exists(*LoginPageLocators.CARD_DEVICE_EDIT)
            exist = 1
        except:
            exist = 0
        finally:
            return exist
