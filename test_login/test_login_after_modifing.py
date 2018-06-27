# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains

class TestLoginPage:

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    def test_login_special_symbols(self):
        """
        Проверка логина пользователя после редактирования параметров пользователя в системе Identity
        """
        driver = self.driver
        driver.get("https://uss-dev-01.pyxus.local/inventory/")
        userelement = driver.find_element_by_id('id_username')
        userelement.click()
        userelement.send_keys('Ab')
        passelement = driver.find_element_by_id('id_password')
        passelement.click()
        passelement.send_keys('1')
        subelement = driver.find_element_by_id('idm_submit_button')
        subelement.click()
        time.sleep(5)
        userfield = driver.page_source
        text = collect(userfield)
        assert "Максим Печора" in text
        driver.quit()

def collect(source=''):
        """
        проверка есть ли указанный текст на странице
        """
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