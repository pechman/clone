# -*- coding: utf-8 -*-
from selenium import webdriver
import time
class TestLoginCase:

    driver = webdriver.Chrome(executable_path=r'C:\path\chromedriver.exe')
    driver.implicitly_wait(3)

    def test_login_for_user_with_upper_case(self):
        """
        Проверка логина: ввод логина с паролем, который содержит ввод upper and lower case,
        должен ввод же быть только lower case
        
        """
        driver = self.driver
        driver.get("https://uss-dev-01.pyxus.local/inventory/")
        userelement = driver.find_element_by_id('id_username')
        userelement.click()
        time.sleep(1)
        userelement.send_keys('admin')
        passelement = driver.find_element_by_id('id_password')
        passelement.click()
        time.sleep(1)
        passelement.send_keys('priOCom')
        subelement = driver.find_element_by_id('idm_submit_button')
        subelement.click()
        time.sleep(1)
        errortip = driver.find_element_by_xpath("//*[contains(text(), 'Будь ласка, введіть правильні')]")
        assert "Будь ласка, введіть правильні ім'я користувача та пароль. Зауважте, що поля можуть бути чутливі до регістру." == errortip.text
        driver.quit()