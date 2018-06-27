# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from bs4 import BeautifulSoup

class Test1:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--incognito')
    driver = webdriver.Chrome(executable_path=r'C:\path\chromedriver.exe', chrome_options=chrome_options)
    driver.implicitly_wait(3)

    def test_1(self):
        """
        Проверка логина: правильный ввод логина и пароля с максимальным именем пользователя
        Pre-steps Создан валидный пользователь. Имя пользователя = минимальное
        Пользователь должен войти в систему Inventory. Поле пользователя, кабинет пользователя отображают соответствующую информацию
        """
        driver = self.driver
        driver.get("https://uss-dev-01.pyxus.local/inventory/")
        userelement = driver.find_element_by_id('id_username')
        userelement.click()
        userelement.send_keys('123456789012345678901234567890')
        passelement = driver.find_element_by_id('id_password')
        passelement.click()
        passelement.send_keys('1')
        subelement = driver.find_element_by_id('idm_submit_button')
        subelement.click()
        time.sleep(2)
        userfield = driver.page_source
        text = collect(userfield)
        assert "Макс Логин" in text
        driver.quit()

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