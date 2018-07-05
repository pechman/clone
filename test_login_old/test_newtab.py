from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from bs4 import BeautifulSoup

class TestNewtab:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()



    def test_opennewtab(self):
        """
        Проверка логина пользователя с уже открытым инстансом системы
        """
        driver = self.driver
        driver.get("https://uss-dev-01.pyxus.local/inventory/")
        time.sleep(1)
        userelement = driver.find_element_by_id('id_username')
        userelement.click()
        userelement.send_keys('r')
        passelement = driver.find_element_by_id('id_password')
        passelement.click()
        passelement.send_keys('1')
        subelement = driver.find_element_by_id('idm_submit_button')
        subelement.click()
        time.sleep(5)
        userfield = driver.page_source
        text = collect(userfield)
        assert "Ранд ал'Тор" in text

        """
        Open new tab: browser.execute_script("window.open('"+your url+"', '_blank')")
        # Открыть новую пустую вкладку
        driver.execute_script("window.open('','_blank');")
        # переключиться на новую вкладку (с индексом 1)
        driver.switch_to.window(driver.window_handles[1])
        # если необходимо
        # вернуться на предыдущую вкладку (с индексом 0)
        driver.switch_to.window(driver.window_handles[0])   
                
        # open a link in a new window
        actions = ActionChains(driver)
        about = driver.find_element_by_link_text('About')
        actions.key_down(Keys.CONTROL).click(about).key_up(Keys.CONTROL).perform()
        """
        driver.execute_script("window.open('https://uss-dev-01.pyxus.local/inventory/', 'new_window')")
        driver.switch_to.window(driver.window_handles[1])
        userfield_newtab = driver.page_source
        text = collect(userfield_newtab)
        assert "Ранд ал'Тор" in text
        time.sleep(3)

def collect(source=''):
        soup = BeautifulSoup(source, "lxml")
        results = soup.find_all("span")
        i = 0
        list = []
        for result in results:
            i = i + 1
            option = result.text.strip()
            if option not in list:
                list.append(option)
        return list