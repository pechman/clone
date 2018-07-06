from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    USERNAME_FIELD = (By.ID, 'id_username')
    PASSWORD_FIELD = (By.ID, 'id_password')
    SUBMIT_BTN = (By.ID, 'idm_submit_button')
    ERROR_FIELD = (By.XPATH,"//*[contains(text(), 'Будь ласка')]")
    USER_INFO_FIRST_NAME = (By.XPATH, "//span[@class='user-box__user-text']/div[1]")
    USER_INFO_LAST_NAME = (By.XPATH, "//span[@class='user-box__user-text']/div[2]")

    # Locators for GRID search device page
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
    TABLE_NAME = (By.XPATH, "//html//thead//td/div[@class='head-cell'][contains(text(),'Назва')]")
    TABLE_CITY = (By.XPATH, "//html//thead//td/div[@class='head-cell'][contains(text(),'Місто')]")
    TABLE_TYPE = (By.XPATH, "//html//thead//td/div[@class='head-cell'][contains(text(),'Тип')]")
    TABLE_MODEL = (By.XPATH, "//html//thead//td/div[@class='head-cell'][contains(text(),'Модель')]")
    TABLE_ORGANIZATION = (By.XPATH, "//html//thead//td/div[@class='head-cell'][contains(text(),'Організація')]")
    TABLE_SITE_NAME = (By.XPATH, "//html//thead//td/div[@class='head-cell'][contains(text(),'Назва майданчика')]")
    TABLE_IP = (By.XPATH, "//html//thead//td/div[@class='head-cell'][contains(text(),'IP адреса')]")
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
    BUTTON_EXPORT_CSV = (By.XPATH, "//div[@class='search-header-controls']//i[@class='fa fa-ellipsis-v']")
    POPUP_EXPORT_CSV = (By.XPATH, "//div[@class='popup search-header-popup']")
    NAME_CARDS_SET_FOR_PAGE = (By.XPATH, "//div/table/tbody/tr/td[1]")
