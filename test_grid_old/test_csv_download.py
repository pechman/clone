# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import os, glob
import io
import csv
import re
import math
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


class TestGridSearchDownload:
    chrome_options = webdriver.ChromeOptions()
    folder = "A:\download_csv"
    #chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--start-maximized')
    prefs = {'download.default_directory': 'A:\download_csv'}
    chrome_options.add_experimental_option('prefs', prefs)
    chdriver = webdriver.Chrome(executable_path=r'A:\test\chromedriver.exe', chrome_options=chrome_options)

    def test_grid_search_download_csv(self):
        """
        Проверка выгрузки scv файла для страницы поиска оборудования/сайтов
        """
        # Логин в систему
        driver = self.chdriver
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
        # Получения количества оборудования из строки
        search_result = driver.find_element_by_xpath("//html//div[@class='search__header']/div[1]")
        numbers_device = int(''.join(c for c in search_result.text if c.isdigit()))
        assert "Результати пошуку" in search_result.text
        print("количество найденных карточек:",numbers_device)
        # Очистка файлов в папке. Теперь в папке будет только один только что загруженный файл
        for file in glob.glob(r'A:\download_csv\*.csv'):
            os.remove(file)
        # Загрузка файла
        scv_download_icon = driver.find_element_by_xpath("//div[@class='search-header-controls']//i[@class='fa fa-ellipsis-v']")
        scv_download_icon.click()
        time.sleep(1)
        download = driver.find_element_by_xpath("//*[@id='root']/div/section/div/div/div[2]/div[1]/div[2]/div/a")
        download.click()
        time.sleep(2)
        # Проверка размера файла
        filelinks = glob.glob(r'A:\download_csv\*.csv')
        filescv = filelinks[0]
        inf_for_filesize=os.path.getsize(filescv)
        assert inf_for_filesize>0
        # Проверка количества строк в файле и количества карточек найденых в системе.
        with open(filescv, newline='', encoding="utf-8") as my_file:
            row = [line.strip() for line in my_file]
            result=[]
            for i in range(len(row)):
                if """;""" in row[i]:
                    result.append(row[i])
            number_cards=len(result)-1
        assert numbers_device == number_cards
        print("число строк в CSV файле:", number_cards)
        print("количество карточек:", numbers_device)
        # Перевод в табличный вид грида
        table_icon = driver.find_element_by_xpath("//i[@class='fa fa-table']")
        table_icon.click()
        if numbers_device > 30:
            pages = math.ceil(numbers_device / 30)

            for p in range(pages):
                print("текущая страница=", p+1)
                time.sleep(1)
                # Проверка наличия нужных карточек и сохранения их сортировки в файле
                device_names_one_page = driver.find_elements_by_xpath("//div/table/tbody/tr/td[1]")
                device_names=[]
                for w in range(len(device_names_one_page)):
                    device_names.append(device_names_one_page[w].text)
                for k in range(len(device_names)):
                    print("p страница=", p+1)
                    print("k номер в таблице=", k)
                    print("название карточки, что соответвует строке в файле:", device_names[k])
                    print("проверяемая строка в файле",result[k+1 + p*30])
                    assert device_names[k] in result[k+1+30*p]
                time.sleep(1)
                if p!=(pages-1):
                    driver.find_element_by_xpath("//html//ul[3]/li[1]").click()
        my_file.close()
        driver.quit()

