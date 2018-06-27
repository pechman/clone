# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time


class Testdriveroption:
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--incognito')
    # chrome_options.add_argument("download.default_directory=A:/download_csv")
    # prefs = {'download.default_directory': 'A:\download_csv'}
    # chrome_options.add_experimental_option('prefs', prefs)
    chrome_options.add_argument('--start-maximized')
    chdriver = webdriver.Chrome(executable_path=r'A:\test\chromedriver.exe', chrome_options=chrome_options)
    chdriver.implicitly_wait(3)
    driver = webdriver.Edge(executable_path=r'A:\test\MicrosoftWebDriver.exe')
    driver.implicitly_wait(3)
    caps = DesiredCapabilities.INTERNETEXPLORER
    caps["se:ieOptions"] = {}
    caps["se:ieOptions"]["ie.ensureCleanSession"] = True
    iedriver = webdriver.Ie(desired_capabilities=caps)
    iedriver.implicitly_wait(3)

    ffdriver = webdriver.Firefox(executable_path=r'A:\test\geckodriver.exe')
    ffdriver.implicitly_wait(3)
    # profile.setPreference("browser.download.dir", "C:\\Users\\Admin\\Desktop\\ScreenShot\\");


    def test_chrome(self):
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
        time.sleep(1)
        driver.quit()

    def test_edge(self):
        driver = self.driver
        driver.get("https://uss-dev-01.pyxus.local/inventory/")
        time.sleep(2)
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(2)
        userelement = driver.find_element_by_id('id_username')
        userelement.click()
        userelement.send_keys('r')
        passelement = driver.find_element_by_id('id_password')
        passelement.click()
        passelement.send_keys('1')
        subelement = driver.find_element_by_id('idm_submit_button')
        subelement.click()
        driver.quit()
    def test_ie(self):
        driver = self.iedriver
        driver.get("https://uss-dev-01.pyxus.local/inventory/")
        time.sleep(4)
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(3)
        userelement = driver.find_element_by_id('id_username')
        userelement.click()
        userelement.send_keys('r')
        passelement = driver.find_element_by_id('id_password')
        passelement.click()
        passelement.send_keys('1')
        subelement = driver.find_element_by_id('idm_submit_button')
        subelement.click()
        driver.close()
        alertq = driver.switch_to.alert
        alertq.accept()
        driver.quit()

    def test_ff(self):
        driver = self.ffdriver
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

