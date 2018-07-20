# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import allure
import pytest


@allure.feature("Feature 11")
@allure.story("story 12")
class Test1:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--incognito')
    driver = webdriver.Chrome(executable_path=r'C:\path\chromedriver.exe', chrome_options=chrome_options)
    driver.implicitly_wait(3)
    @allure.step("step22")
    def test_1(self):
        """
        Проверка логина: правильный ввод логина и пароля с минимальным именем пользователя
        Pre-steps Создан валидный пользователь. Имя пользователя = минимальное
        вход в систему
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
        time.sleep(1)
        driver.quit()