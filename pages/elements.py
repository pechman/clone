from config import Browser
import time
class PageElements(Browser):

    def fill(self, value, *locator):
        self.driver.find_element(*locator).send_keys(value)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def check_user_first_name(self, *locator):
        time.sleep(2)
        first_name = self.driver.find_element(*locator).text
        return first_name

    def check_user_last_name(self, *locator):
        last_name = self.driver.find_element(*locator).text
        return last_name

    def check_text_for_menu(self, *locator):
        menu_text = self.driver.find_element(*locator).text
        return menu_text

    def check_text_for_table(self, *locator):
        table_text = self.driver.find_element(*locator).text
        return table_text

    def check_number(self, *locator):
        number_device = self.driver.find_element(*locator).text
        return number_device

    def card_list(self, *locator):
        cards = self.driver.find_elements(*locator)
        return cards

    def active_page(self, *locator):
        active = int(self.driver.find_element(*locator).text)
        return active

    def view_active_mode(self, *locator):
        view_icon_current = self.driver.find_elements(*locator)
        return view_icon_current