# -*- coding: utf-8 -*-
from selenium import webdriver
import time
class TestLoginCase:

    driver = webdriver.Chrome(executable_path=r'C:\path\chromedriver.exe')
    driver.implicitly_wait(3)

    def test_login_for_inactive_user(self):
        """
        Проверка логина: ввод логина корректного пользователя, но не активного
        """
        driver = self.driver
        driver.get("https://uss-dev-01.pyxus.local/inventory/")
        userelement = driver.find_element_by_id('id_username')
        userelement.click()
        userelement.send_keys('test_u1')
        passelement = driver.find_element_by_id('id_password')
        passelement.click()
        passelement.send_keys('1')
        subelement = driver.find_element_by_id('idm_submit_button')
        subelement.click()
        time.sleep(3)
        errortip = driver.find_element_by_xpath("//*[contains(text(), 'Цей обліковий запис неактивний.')]")
        assert "Цей обліковий запис неактивний." == errortip.text
        driver.quit()