# -*- coding: utf-8 -*-
from selenium import webdriver
import time
class TestLoginNonexistentUser:

    driver = webdriver.Chrome(executable_path=r'C:\path\chromedriver.exe')
    driver.implicitly_wait(3)

    def test_login_waste_symbol_username(self):
        """
        Проверка логина: не правильный ввод логина лишний спец символ/кирилица/казахский в конце или в начале
        """
        driver = self.driver
        driver.get("https://uss-dev-01.pyxus.local/inventory/")
        string = """☺~!@#$%^&*()?>,./\<]|"'[*<!–ÄäĞğÏïÜüÖÑñöŨũÇŞşçİiІієЄ₴їЇЁёъЪЫыэЭ"""
        try:
            for i in string:
                userelement = driver.find_element_by_id('id_username')
                userelement.click()
                time.sleep(1)
                username = "R"+i
                userelement.send_keys(username)
                passelement = driver.find_element_by_id('id_password')
                passelement.click()
                time.sleep(1)
                passelement.send_keys('1')
                subelement = driver.find_element_by_id('idm_submit_button')
                subelement.click()
                time.sleep(1)
                errortip = driver.find_element_by_xpath("//*[contains(text(), 'Будь ласка, введіть правильні')]")
                assert "Будь ласка, введіть правильні ім'я користувача та пароль. Зауважте, що поля можуть бути чутливі до регістру." == errortip.text
        except:
            print('символ со сбоем:"', i, '"', 'номер символа в строке:', string.index(i))
            checktip= driver.find_element_by_xpath("//*[contains(text(), 'Будь ласка, введіть правильні')]")
            assert "Будь ласка, введіть правильні ім'я користувача та пароль. Зауважте, що поля можуть бути чутливі до регістру." == checktip.text
        try:
            for k in string:
                userelement = driver.find_element_by_id('id_username')
                userelement.click()
                time.sleep(1)
                username = k+"R"
                userelement.send_keys(username)
                passelement = driver.find_element_by_id('id_password')
                passelement.click()
                time.sleep(1)
                passelement.send_keys('1')
                subelement = driver.find_element_by_id('idm_submit_button')
                subelement.click()
                time.sleep(1)
                errortip = driver.find_element_by_xpath("//*[contains(text(), 'Будь ласка, введіть правильні')]")
                assert "Будь ласка, введіть правильні ім'я користувача та пароль. Зауважте, що поля можуть бути чутливі до регістру." == errortip.text
        except:
            print('символ со сбоем:"', k, '"', 'номер символа в строке:', string.index(k))
            checktip= driver.find_element_by_xpath("//*[contains(text(), 'Будь ласка, введіть правильні')]")
            assert "Будь ласка, введіть правильні ім'я користувача та пароль. Зауважте, що поля можуть бути чутливі до регістру." == checktip.text
        driver.quit()