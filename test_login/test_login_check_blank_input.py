# -*- coding: utf-8 -*-
from selenium import webdriver
import time

class TestLoginBlankInput:
    driver = webdriver.Chrome(executable_path=r'C:\path\chromedriver.exe')
    driver.implicitly_wait(3)

    def test_blank_input(self):
        """
               Проверка логина: выполнение входа с пустыми полями логина и пароля
        """
        driver = self.driver
        driver.get("https://uss-dev-01.pyxus.local/inventory/")
        userelement = driver.find_element_by_id('id_username')
        userelement.click()
        passelement = driver.find_element_by_id('id_password')
        passelement.click()
        subelement = driver.find_element_by_id('idm_submit_button')
        subelement.click()
        time.sleep(1)
        errortip = driver.find_element_by_xpath("//*[contains(text(), 'Будь ласка')]")
        assert "Будь ласка, зверніть увагу, що необхідно заповнити усі поля." == errortip.text
        driver.quit()