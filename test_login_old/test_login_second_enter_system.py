# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

class TestCaseForSecondEnter:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--incognito')
    driver = webdriver.Chrome(executable_path=r'C:\path\chromedriver.exe', chrome_options=chrome_options)
    driver.implicitly_wait(3)

    def test_repeat_enter(self):
        """
        Проверка логина: правильный ввод логина и пароля
        вход в систему для пользователя
        Проверка логина пользователя с уже открытым инстансом системы
        """
        driver = self.driver
        driver.get("https://uss-dev-01.pyxus.local/inventory/")
        userelement = driver.find_element_by_id('id_username')
        userelement.click()
        userelement.send_keys('mpechora')
        passelement = driver.find_element_by_id('id_password')
        passelement.click()
        passelement.send_keys('Pm1234%^')
        subelement = driver.find_element_by_id('idm_submit_button')
        subelement.click()
        time.sleep(2)
        userfield = driver.page_source
        text = collect(userfield)
        assert "Максим last name" in text
        # проверка открытия системы в том же окне
        driver.get("https://uss-dev-01.pyxus.local/inventory/")
        time.sleep(2)
        userfield = driver.page_source
        text = collect(userfield)
        assert "Максим last name" in text
        # проверка открытия системы в соседнем окне
        driver.execute_script("window.open('https://uss-dev-01.pyxus.local/inventory');")
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(2)
        userfield = driver.page_source
        text = collect(userfield)
        assert "Максим last name" in text

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