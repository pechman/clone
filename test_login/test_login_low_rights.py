
# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

class TestCaseForLowRights:
    driver = webdriver.Chrome(executable_path=r'C:\path\chromedriver.exe')
    driver.implicitly_wait(3)

    def test_login_low_rights(self):
        """
        Проверка логина для пользователя с понижеными правами
        недоступные меню настройки и ресурсы
        """
        driver = self.driver
        driver.get("https://uss-dev-01.pyxus.local/inventory/")
        userelement = driver.find_element_by_id('id_username')
        userelement.click()
        userelement.send_keys('tl')
        passelement = driver.find_element_by_id('id_password')
        passelement.click()
        passelement.send_keys('1')
        subelement = driver.find_element_by_id('idm_submit_button')
        subelement.click()
        time.sleep(2)
        userfield = driver.page_source
        text = collect(userfield)
        assert "Максим Низкий" in text
        # проверка, что меню Ресурсы и Настройки недоступны
        assert "Налаштування" not in driver.page_source
        assert "Ресурси" not in driver.page_source
        assert "Сайт" in driver.page_source
        assert "Обладнання" in driver.page_source
        # закрытие теста
        driver.find_element_by_class_name('user-box__user-text').click()
        logout = driver.find_element_by_xpath("//*[contains(text(), 'Вийти')]")
        logout.click()
        driver.switch_to.window(driver.window_handles[1])
        logoutpage = driver.find_element_by_xpath("//div[@class='login-page__form-title']")
        assert "Priocom Login" == logoutpage.text
        driver.quit()

def collect(source=''):
        soup = BeautifulSoup(source, "lxml")
        results = soup.find_all("span")
        i = 0
        list = []
        for result in results:
            i = i + 1
            option = result.text.strip()
            if option not in list:
                list.append(option)
        return list