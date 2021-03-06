from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    USERNAME_FIELD = (By.ID, 'id_username')
    PASSWORD_FIELD = (By.ID, 'id_password')
    SUBMIT_BTN = (By.ID, 'idm_submit_button')
    ERROR_FIELD = (By.XPATH,"//*[contains(text(), 'Будь ласка')]")
    USER_INFO_FIRST_NAME = (By.XPATH, "//span[@class='user-box__user-text']/div[1]")
    USER_INFO_LAST_NAME = (By.XPATH, "//span[@class='user-box__user-text']/div[2]")
    USER_AREA = (By.XPATH, "//div[contains(@class, 'header-block__user-box user-box')]")
    USER_AREA_LANG = (By.XPATH, "//i[contains(@class, 'fas fa-language')]")
    USER_AREA_LOGOUT = (By.XPATH, "//*[contains(text(), 'Вийти')]")
    ICON_ADD_CARD_SITE_DEVICE = (By.XPATH, "//div[@class='btn-create__fa-wrapper']")
    ADD_AREA_SITE_DEVICE = (By.XPATH, "//div[contains(text(),'Cтворення')]")
    ADD_AREA_SITE = (By.XPATH, "//div[contains(text(),'Створити Майданчик')]")
    ADD_AREA_DEVICE = (By.XPATH, "//div[contains(text(),'Створити Обладнання')]")
    BOTTOM_AREA_MAIN = (By.XPATH, "//div[contains(text(),'Головна')]")
    BOTTOM_AREA_SETTINGS = (By.XPATH, "//div[contains(text(),'Налаштування')]")


    MENU_TAB_FIRST = (By.XPATH, "//a[contains(@class,'box site')]")
    TAB_PREVIOUS = (By.XPATH, "//html//nav[@class='head-tabs']/div[1]")

    # Locators for GRID search device page
    WRAP_ICON = (By.XPATH, "//div[contains(@class, 'menu-expander')]")

    ADD_BUTTON = (By.XPATH, "//div[@class='btn-create']")
    MENU_DEVICE = (By.XPATH, "//span[@class='nav-title'][contains(text(),'Обладнання')]")
    MENU_SITE = (By.XPATH, "//span[@class='nav-title'][contains(text(),'Майданчик')]")
    MENU_RESOURCE = (By.XPATH, "//span[@class='nav-title'][contains(text(),'Ресурси')]")
    MENU_MAIN = (By.XPATH, "//html//div[@class='menu apps-menu-bottom']/div[1]/div[1][contains(text(),'Головна')]")
    MENU_SETTINGS = (By.XPATH, "//html//div[@class='menu apps-menu-bottom']/div[2]/div[1][contains(text(),'Налаштування')]")
    SEARCH_RESULT = (By.XPATH, "//html//div[@class='search__header']/div[1]")
    SEARCH_BOX_HEAD = (By.XPATH, "//div[@class='header-block__search search']//input[@type='text']")
    SEARCH_BOX_GRID = (By.XPATH, "//div[@class='search__field']//input[@type='text']")
    VIEW_MODE_ICON = (By.XPATH, "//div[@class='search-header-controls']/i[1]")
    VIEW_MODE_TABLE = (By.XPATH, "//i[@class='fa fa-th']")
    VIEW_MODE_CARDS = (By.XPATH, "//i[@class='fa fa-table']")
    FILTER_ICON = (By.XPATH, "//div[@class='search-header-controls']/i[2]")
    EXPORT_ICON = (By.XPATH, "//div[@class='search-header-controls']/i[3]")
    TABLE_NAME = (By.XPATH, "//div[contains(@class, 'head-cell-text') and contains(text(), 'Назва')]")
    TABLE_CITY = (By.XPATH, "//div[contains(@class, 'head-cell-text') and contains(text(), 'Місто')]")
    TABLE_TYPE = (By.XPATH, "//div[contains(@class, 'head-cell-text') and contains(text(), 'Тип')]")
    TABLE_MODEL = (By.XPATH, "//div[contains(@class, 'head-cell-text') and contains(text(), 'Модель')]")
    TABLE_ORGANIZATION = (By.XPATH, "//div[contains(@class, 'head-cell-text') and contains(text(), 'Організація')]")
    TABLE_SITE_NAME = (By.XPATH, "//div[contains(@class, 'head-cell-text') and contains(text(), 'Назва майданчика')]")
    TABLE_IP = (By.XPATH, "//div[contains(@class, 'head-cell-text') and contains(text(), 'IP адреса')]")
    PAGINATION_PAGE = (By.XPATH, "//html//ul[@class='pagination-items']/li[1]")
    PAGINATION_ACTIVE_PAGE = (By.XPATH, "//li[@class='active']")
    PAGINATION_PAGE_NEXT = (By.XPATH, "//html//ul[@class='pagination-items']/li[2]")
    PAGINATION_ARROWHEAD_FORWARD = (By.XPATH, "//html//ul[3]/li[1]")
    PAGINATION_ARROWHEAD_FORWARD_END = (By.XPATH, "//html//ul[3]/li[2]")
    PAGINATION_ARROWHEAD_BACK = (By.XPATH, "//html//ul[1]/li[2]")
    PAGINATION_ARROWHEAD_BACK_START = (By.XPATH, "//html//ul[1]/li[1]")
    SORT_ARROWHEAD_DESC = (By.XPATH, "//i[@class='fas fa-sort-down']")
    SORT_ARROWHEAD_ASC = (By.XPATH, "//i[@class='fas fa-sort-up']")
    CARD_LIST = (By.XPATH, "//html//a/div/div[@class='card__body']")
    ROW_LIST = (By.XPATH, "//table[@class='table-grid']//tbody/tr")
    BUTTON_EXPORT_CSV = (By.XPATH, "//i[contains(@class, 'icon-kebab-vert')]")
    POPUP_EXPORT_CSV = (By.XPATH, "//div[contains(@class, 'popup search-header-popup')]/a")
    NAME_CARDS_SET_FOR_PAGE = (By.XPATH, "//div/table/tbody/tr/td[1]")
    NAME_FIRST_TD_TABLE = (By.XPATH, "//tr[1]/td[1]/div[contains(@class, 'item-cell')]/a[contains(@class, 'data-cell')]")


    # Locators for filter

    FILTER_TYPE = (By.XPATH, "//div[@class='Select container-comboBox is-clearable is-searchable Select--single']//div[@class='Select-control']")
    FILTER_TYPE_ROUTER = (By.XPATH, "//span[@id='react-select-2--value']/div[contains(@class, 'Select-placeholder')]")
    OPTION_TYPE_LOCATOR = (By.XPATH, "//div[@id='react-select-2--option-1']")



    # Locators for device card
    CARD_DEVICE_NAME = (By.XPATH, "//span[@class='head-title']")
    CARD_DEVICE_TYPE = (By.XPATH, "//html//div[@id='card-top-row']//div[2]/div[1]/div[1]")
    CARD_DEVICE_MODEL = (By.XPATH, "//html//div[@class='head-main-row']/div[2]/div[2]/div[1]")
    CARD_DEVICE_CITY = (By.XPATH, "//html//section[@class='main-block']//div[3]/div[1]/div[1]/span[1]")
    CARD_DEVICE_SITE = (By.XPATH, "//html//section[@class='main-block']//div[3]/div[2]/div[1]")

    CARD_DEVICE_ALL_TABS = (By.XPATH, "//a[contains(@class, 'tab-vertical')]")
    CARD_DEVICE_PARAMETERS = (By.XPATH, "//a[@class='tab-vertical active']")
    CARD_DEVICE_PARAMETERS_INACTIVE = (By.XPATH, "//a[@class='tab-vertical'][1]")
    CARD_DEVICE_ACCESS = (By.XPATH, "//a[@class='tab-vertical'][1]")
    CARD_DEVICE_ACCESS_TEXT_UA = (By.XPATH, "//a[contains(text(),'ДОСТУП')]")
    CARD_DEVICE_ACCESS_TEXT_EN = (By.XPATH, "//a[contains(text(),'ACCESS')]")
    CARD_DEVICE_INTERFACE = (By.XPATH, "//a[@class='tab-vertical'][2]")
    CARD_DEVICE_INTERFACE_TEXT_UA = (By.XPATH, "//a[contains(text(),'ІНТЕРФЕЙСИ')]")
    CARD_DEVICE_CHASSIS = (By.XPATH, "//a[@class='tab-vertical'][3]")
    CARD_DEVICE_TOPOLOGY = (By.XPATH, "//a[@class='tab-vertical'][4]")
    CARD_DEVICE_TOPOLOGY_TEXT_UA = (By.XPATH, "//a[contains(text(),'ТОПОЛОГІЯ')]")
    CARD_DEVICE_DOCUMENTS = (By.XPATH, "//a[@class='tab-vertical'][5]")
    CARD_DEVICE_DOCUMENTS_TEXT_UA = (By.XPATH, "//a[contains(text(),'ДОКУМЕНТИ')]")

    CARD_DEVICE_EDIT = (By.XPATH, "//button")
    CARD_DEVICE_SUBMIT = (By.XPATH, "//button[@class='button']")
    CARD_DEVICE_CANCEL = (By.XPATH, "//button[@class='button cancel']")

    CARD_DEVICE_GENERAL_INFORMATION = (By.XPATH, "//html//div[@class='col-lg-4 col-md-6 col-sm-12 read-only-group']/span[1]")
    CARD_DEVICE_GEN_MODEL = (By.XPATH, "//html//div[@class='col-lg-4 col-md-6 col-sm-12 read-only-group']/div[@class='read-only-items']/div[1]/div[1]")
    CARD_DEVICE_GEN_STATUS = (By.XPATH, "//html//div[@class='col-lg-4 col-md-6 col-sm-12 read-only-group']//div[2]/div[1]")
    CARD_DEVICE_GEN_EQUIPMENT_CODE = (By.XPATH, "//html//div[@class='col-lg-4 col-md-6 col-sm-12 read-only-group']//div[3]/div[1]")
    CARD_DEVICE_GEN_SERIAL_NUMBER = (By.XPATH, "//html//div[@class='col-lg-4 col-md-6 col-sm-12 read-only-group']//div[4]/div[1]")
    CARD_DEVICE_GEN_INVENTORY_NUMBER = (By.XPATH, "//html//div[@id='root']//div[5]/div[1]")
    CARD_DEVICE_GEN_ORGANIZATION = (By.XPATH, "//html//div[6]/div[1]")
    CARD_DEVICE_GEN_INSTALLATION_DATE = (By.XPATH, "//html//div[@class='content-spinner-wrapper']//div[7]/div[1]")
    CARD_DEVICE_GEN_START_UP_DATE = (By.XPATH, "//html//div[8]/div[1]")
    CARD_DEVICE_GEN_DESCRIPTION = (By.XPATH, "//html//div[9]/div[1]")

    CARD_DEVICE_GEN_PAR = (By.XPATH, "//html//div[@class='row no-gutters']/div[2]/span[1]")
    CARD_DEVICE_GEN_PAR_IP = (By.XPATH, "//html//div[@class='params-body-wrapper']//div[2]/div[1]/div[1]/div[1]")
    CARD_DEVICE_GEN_PAR_MAC = (By.XPATH, "//html//div[@id='card-bottom-row']/div[@class='bottom']//div[2]/div[1]/div[2]/div[1]")
    CARD_DEVICE_GEN_PAR_OS_TYPE = (By.XPATH, "//html//div[2]/div[1]/div[3]/div[1]")
    CARD_DEVICE_GEN_PAR_OS_VERSION = (By.XPATH, "//html//div[2]/div[1]/div[4]/div[1]")

    CARD_DEVICE_SITE_SITE = (By.XPATH, "//html//div[3]/span[1]")
    CARD_DEVICE_SITE_SITE_NAME = (By.XPATH, "//html//section[@class='main-block']//div[3]/div[1]/div[1]/div[1]")
    CARD_DEVICE_SITE_ADDRESS = (By.XPATH, "//html//div[@id='card-bottom-row']//div[3]/div[1]/div[2]/div[1]")
    CARD_DEVICE_SITE_SITE_TYPE = (By.XPATH, "//html//section[@class='main-block']//div[3]/div[1]/div[3]/div[1]")
    CARD_DEVICE_SITE_CITY = (By.XPATH, "//html//div[3]/div[1]/div[4]/div[1]")

    CARD_DEVICE_ROLES = (By.XPATH, "//html//div[@class='row no-gutters']/div[4]/span[1]")

    # LANGUAGE
    ICON_CHANGE_LANGUAGE = (By.XPATH, "//div[@class='header-block__user-box language-box']")
    ICON_UA_LANGUAGE = (By.XPATH, "//div[contains(@class, 'menu lang-menu')]//div[contains(text(),'Українська')]")
    ICON_RU_LANGUAGE = (By.XPATH, "//div[contains(@class, 'menu lang-menu')]//div[contains(text(),'Русский')]")
    ICON_EN_LANGUAGE = (By.XPATH, "//div[contains(@class, 'menu lang-menu')]//div[contains(text(),'English')]")