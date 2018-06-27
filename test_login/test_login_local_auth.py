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
        Проверка логина: правильный ввод логина и пароля
        вход в систему для пользователя с методом авторизации ldap
        """
        driver = self.driver
        driver.get("https://uss-dev-01.pyxus.local/inventory/")
        userelement = driver.find_element_by_id('id_username')
        userelement.click()
        userelement.send_keys('r')
        passelement = driver.find_element_by_id('id_password')
        passelement.click()
        passelement.send_keys('1')
        subelement = driver.find_element_by_id('idm_submit_button')
        subelement.click()
        time.sleep(5)
        us_info = driver.find_element_by_xpath("//span[@class='user-box__user-text']/div[1]")
        print(us_info.text)

"""
        
        userfield = driver.page_source
        text = collect(userfield)
        assert "Ранд ал'Тор" in text
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
"""