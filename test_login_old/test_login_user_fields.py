# -*- coding: utf-8 -*-
from selenium import webdriver
import time

class Test1:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--incognito')
    driver = webdriver.Chrome(executable_path=r'C:\path\chromedriver.exe', chrome_options=chrome_options)
    driver.implicitly_wait(3)

    def test_1(self):
        """
        Проверка отображения страницы логина: Корректные поля и подсказки к ним
        """
        driver = self.driver
        driver.get("https://uss-dev-01.pyxus.local/inventory/")
        logoutpage = driver.find_element_by_xpath("//div[@class='login-page__form-title']")
        assert "Priocom Login" == logoutpage.text
        userelement = driver.find_element_by_id('id_username')
        userelement.click()
        placeholderuser = userelement.get_attribute('placeholder')
        assert placeholderuser == "Ім’я користувача..."
        userelement.send_keys('r')
        passelement = driver.find_element_by_id('id_password')
        passelement.click()
        assert passelement.get_attribute('placeholder') == "Пароль..."
        passelement.send_keys('1')
        subelement = driver.find_element_by_id('idm_submit_button')
        assert subelement.get_attribute('value') == "Увійти"
        subelement.click()
        time.sleep(1)
        driver.quit()
