from config import Browser
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

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

    def wait(self, n_seconds):
        time.sleep(n_seconds)

    def enter_key(self, *locator):
        time.sleep(1)
        self.driver.switch_to_active_element()
        self.driver.find_element(*locator).send_keys(Keys.ENTER)

    def arrow_down_key1(self, *locator):
        time.sleep(1)
        self.driver.switch_to_active_element()
        self.driver.find_element(*locator).send_keys(Keys.DOWN)

    def arrow_down_key2(self, *locator):
        time.sleep(1)
        self.driver.switch_to_active_element()
        self.driver.find_element(*locator).send_keys(Keys.ARROW_DOWN)

    def tab_key(self, *locator):
        time.sleep(1)
        self.driver.switch_to_active_element()
        self.driver.find_element(*locator).send_keys(Keys.TAB)

    def ecs_key(self, *locator):
        self.driver.switch_to_active_element()
        self.driver.find_element(*locator).send_keys(Keys.ESCAPE)