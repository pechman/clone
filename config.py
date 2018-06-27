from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class Browser(object):
    driver = webdriver.Chrome(r'A:\test\drivers\chromedriver.exe')
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(10)
    driver.maximize_window()
    driver.get("https://uss-dev-01.pyxus.local/inventory/")
    wait = WebDriverWait(driver, 10)

    def close(self):
        self.driver.quit()