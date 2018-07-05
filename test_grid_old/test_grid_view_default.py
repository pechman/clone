# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import math
from bs4 import BeautifulSoup

class TestGridView:

    driver = webdriver.Chrome(executable_path=r'C:\path\chromedriver.exe')
    driver.implicitly_wait(3)

    def test_grid_view(self):
        """
        Проверка отображения грида. Открыта дефолтная страница поиска оборудования. Выборка отображается без учёта фильтра.
        В зависимости от прав пользователя и настроек системы могут отображаться следующие элементы: header таблицы,
        таблица с записями, нумерация для больше 30 записей, кнопки функциональности грида, иконки грида
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
        search_result = driver.find_element_by_xpath("//html//div[@class='search__header']/div[1]")
        assert "Результати пошуку" in search_result.text
        # Получения количества оборудования из строки
        numbers_device = int(''.join(c for c in search_result.text if c.isdigit()))
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
        driver.quit()







