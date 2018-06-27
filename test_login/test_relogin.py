# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

class TestCaseForSecondEnter:
    driver = webdriver.Chrome(executable_path=r'C:\path\chromedriver.exe')
    driver.implicitly_wait(3)

    def test_repeat_enter(self):
        """
        Проверка повторного логина пользователя после выхода пользователя с уже открытого инстанса системы
        проверка сохранения отредактированных пользователем данных после релогина
        """
        driver = self.driver
        driver.get("https://uss-dev-01.pyxus.local/inventory/")
        userelement = driver.find_element_by_id('id_username')
        userelement.click()
        userelement.send_keys('mpechora')
        passelement = driver.find_element_by_id('id_password')
        passelement.click()
        passelement.send_keys('Pm1234%^')
        subelement = driver.find_element_by_id('idm_submit_button')
        subelement.click()
        time.sleep(2)
        userfield = driver.page_source
        text = collect(userfield)
        assert "Максим last name" in text
        # проверка открытия системы в соседнем окне
        driver.execute_script("window.open('https://uss-dev-01.pyxus.local/inventory');")
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(2)
        userfield = driver.page_source
        text = collect(userfield)
        assert "Максим last name" in text
        # Редактируем элемент
        search_element = driver.find_element_by_class_name('search__input')
        search_element.click()
        search_element.send_keys("29_122", Keys.ENTER)
        card = driver.find_element_by_xpath("//*[@class ='card__body'] // *[text()='29_122']")
        card.click()
        driver.find_element_by_xpath("//button[@class='button']").click()
        driver.find_element_by_name("serial_number").click()
        driver.find_element_by_name("serial_number").clear()
        # Изменяем серийник
        driver.find_element_by_name("serial_number").send_keys("555429_1")
        driver.find_element_by_xpath("//button[@class='button']").click()
        # первое окно релогин
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_class_name('user-box__user-text').click()
        logout = driver.find_element_by_xpath("//*[contains(text(), 'Вийти')]")
        logout.click()
        driver.switch_to.window(driver.window_handles[2])
        logoutpage = driver.find_element_by_xpath("//div[@class='login-page__form-title']")
        assert "Priocom Login" == logoutpage.text
        userelement = driver.find_element_by_id('id_username')
        userelement.click()
        userelement.send_keys('mpechora')
        passelement = driver.find_element_by_id('id_password')
        passelement.click()
        passelement.send_keys('Pm1234%^')
        subelement = driver.find_element_by_id('idm_submit_button')
        subelement.click()
        time.sleep(2)
        userfield = driver.page_source
        text = collect(userfield)
        assert "Максим last name" in text
        # проверка сохранения данных
        search_element = driver.find_element_by_xpath("//div[@class='search__field']//input[@type='text']")
        search_element.click()
        search_element.send_keys("555429_1", Keys.ENTER)
        card = driver.find_element_by_xpath("//*[@class ='card__body'] // *[text()='29_122']")
        card.click()
        serial = driver.find_element_by_xpath("//*[@id='card-bottom-row']/div[2]/div/div[2]/div/div/div[1]/div/div[4]/div[2]").text
        assert "555429_1" == serial
        # очистка серийника для последующих запусков теста
        driver.find_element_by_xpath("//button[@class='button']").click()
        driver.find_element_by_name("serial_number").click()
        driver.find_element_by_name("serial_number").clear()
        driver.find_element_by_xpath("//button[@class='button']").click()
        # закрытие теста
        driver.find_element_by_class_name('user-box__user-text').click()
        logout = driver.find_element_by_xpath("//*[contains(text(), 'Вийти')]")
        logout.click()
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