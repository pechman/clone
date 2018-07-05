# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from bs4 import BeautifulSoup

class TestLoginKeys:

    driver = webdriver.Chrome(executable_path=r'C:\path\chromedriver.exe')
    driver.implicitly_wait(3)

    def test_login_interaction_with_keys(self):
        """
        Проверка логина: ввод данных пользователя+ использование разных клавиш
        """
        driver = self.driver
        driver.get("https://uss-dev-01.pyxus.local/inventory/")
        userelement = driver.find_element_by_id('id_username')
        userelement.click()
        userelement.send_keys('ad')

        passelement = driver.find_element_by_id('id_password')
        passelement.send_keys(Keys.TAB)
        passelement.send_keys('priocom')

        userelement.send_keys(Keys.ALT+Keys.TAB)

        userelement.send_keys(Keys.ARROW_RIGHT)

        userelement.send_keys('min')

        subelement = driver.find_element_by_id('idm_submit_button')
        subelement.send_keys(Keys.ENTER)
        time.sleep(1)
        assert "Обладнання" in driver.page_source
        assert "Сайт" in driver.page_source
        driver.quit()
