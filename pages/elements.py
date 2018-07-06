from config import Browser
import time
class PageElements(Browser):

    def fill(self, value, *locator):
        self.driver.find_element(*locator).send_keys(value)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def check_one_element_exists(self, *locator):
        time.sleep(1)
        element = self.driver.find_element(*locator)
        return element

    def check_set_elements_exist(self, *locator):
        time.sleep(1)
        elements = self.driver.find_elements(*locator)
        return elements