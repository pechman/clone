# -*- coding: utf-8 -*-
from selenium import webdriver
import time

class Test1:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--incognito')
    driver = webdriver.Chrome(executable_path=r'C:\path\chromedriver.exe', chrome_options=chrome_options)
    driver.implicitly_wait(3)

    def test_1(self):
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
        userfield = driver.find_element_by_class_name('user-box__user-text')
        userfield.click()
        logout = driver.find_element_by_xpath("//*[contains(text(), 'Вийти')]")
        logout.click()
        logoutpage = driver.find_element_by_xpath("//div[@class='login-page__form-title']")
        assert "Priocom Login" == logoutpage.text
        driver.quit()
