# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import math
from bs4 import BeautifulSoup

class TestGridSort:

    driver = webdriver.Chrome(executable_path=r'C:\path\chromedriver.exe')
    driver.implicitly_wait(3)

    def test_grid_sort(self):
        """
        Проверка сортировки в гриде. Открыта дефолтная страница поиска оборудования.
        Грид отображает правильную последовательность по убыванию соответственно названию оборудования,
        если включить сортировку desc по названию.
        """
        # Логин в систему
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
        time.sleep(2)
        # Открыта дефолтная странца- страница поиска оборудования
        device_tab = driver.find_element_by_xpath("//span[@class='main-tab__text']")
        assert "Обладнання" == device_tab.text
        assert "page" == driver.find_element_by_xpath("//a[@class='main-tab active']").get_attribute('aria-current')
        device_menu = driver.find_element_by_xpath("//a[@class='box device  active']")
        assert "Обладнання" == device_menu.text
        assert "page" == device_menu.get_attribute('aria-current')
        site_menu = driver.find_element_by_xpath("//a[contains(@class,'box site')]")
        assert "Майданчик" == site_menu.text
        # Перевод в табличный вид грида
        table_icon = driver.find_element_by_xpath("//i[@class='fa fa-table']")
        table_icon.click()
        # Проверка табличного вида
        assert "Назва" == driver.find_element_by_xpath("//html//thead//td[1]/div[1]").text
        assert "Місто" == driver.find_element_by_xpath("//div[@class='head-cell'][contains(text(),'Місто')]").text
        assert "Тип" == driver.find_element_by_xpath("//div[@class='head-cell'][contains(text(),'Тип')]").text
        assert "Модель" == driver.find_element_by_xpath("//div[@class='head-cell'][contains(text(),'Модель')]").text
        assert "Організація" == driver.find_element_by_xpath("//div[@class='head-cell'][contains(text(),'Організація')]").text
        assert "Назва майданчика" == driver.find_element_by_xpath("//div[@class='head-cell'][contains(text(),'Назва майданчика')]").text
        assert "IP адреса" == driver.find_element_by_xpath("//div[@class='head-cell'][contains(text(),'IP адреса')]").text
        # Ограничение вывода, ищем только оборудование, что содержит фильтр 111
        search_input = driver.find_element_by_xpath("//div[@class='search__field']//input[@type='text']")
        search_input.send_keys("111")
        time.sleep(1)
        # Включение сортировки по названию
        driver.find_element_by_xpath("//div[@class='head-cell'][contains(text(),'Назва')]").click()
        # Проверка последовательности для сортировки
        device_table = driver.find_elements_by_xpath("//html//tr//td[1]")
        device_names = []
        for i in range(len(device_table)):
            device_names.append(device_table[i].text)
        device_names.pop(0)
        print('имена:', device_names)
        device_names_sort = sorted(device_names)
        print('sort:', device_names_sort)
        assert device_names == device_names_sort
        driver.quit()
        time.sleep(1)


        """
        # Включение сортировки по названию
        driver.find_element_by_xpath("//div[@class='head-cell'][contains(text(),'Назва')]").click()
        # Проверка последовательности для сортировки
        device_table = driver.find_elements_by_xpath("//html//tr//td[1]")
        device_names = []
        i =1
        while i<len(device_table):
            device_names.append(device_table[i].text)
            i+=1
        print('имена:', device_names)
        device_names_sort = sorted(device_names)
        print('sort:', device_names_sort)
        assert device_names == device_names_sort
        driver.quit()
        time.sleep(1)

"""

