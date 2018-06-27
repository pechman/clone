# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import math
from bs4 import BeautifulSoup

class TestGridSearch:

    driver = webdriver.Chrome(executable_path=r'C:\path\chromedriver.exe')
    driver.implicitly_wait(3)

    def test_grid_search(self):
        """
        Проверка поиска в гриде. Открыта дефолтная страница поиска оборудования.
        Таблица содержит выборку, которая соответствует запросу в поле поиска.
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
        # Ввод в строку поиска для оборудования
        search_input = driver.find_element_by_xpath("//div[@class='search__field']//input[@type='text']")
        search_input.send_keys("29_111")
        search_result = driver.find_element_by_xpath("//html//div[@class='search__header']/div[1]")
        numbers_device = int(''.join(c for c in search_result.text if c.isdigit()))
        assert "Результати пошуку" in search_result.text
        # Получения количества оборудования из строки
        print(numbers_device)
        # Проверка отображения пагинации
        if numbers_device>30:
            pages = math.ceil(numbers_device/30)
            print(pages)
            assert "1" == driver.find_element_by_xpath("//li[@class='active']").text
            assert ">" == driver.find_element_by_xpath("//html//ul[3]/li[1]").text
            assert ">>" == driver.find_element_by_xpath("//html//ul[3]/li[2]").text
            card_list = driver.find_elements_by_class_name('card__body')
            assert 30 == len(card_list)
            driver.find_element_by_xpath("//html//ul[3]/li[2]").click()
            assert pages == int(driver.find_element_by_xpath("//li[@class='active']").text)
            assert "<" == driver.find_element_by_xpath("//html//ul[1]/li[2]").text
            assert "<<" == driver.find_element_by_xpath("//html//ul[1]/li[1]").text
        else:
            assert "1" not in driver.find_element_by_xpath("//ul[@class='pagination-items']").text
        assert "Головна" == driver.find_element_by_xpath("//div[@class='item wi active']").text
        time.sleep(1)
        assert "1" in search_result.text
        card_list = driver.find_elements_by_class_name('card__body')
        assert 1 == len(card_list)
        assert "29_111" in driver.find_element_by_xpath("//div[contains(@class,'card device')]").text
        time.sleep(1)
        driver.quit()
