from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class Browser(object):
    chrome_options = webdriver.ChromeOptions()
    folder = "A:\download_csv"
    chrome_options.add_argument('--start-maximized')
    prefs = {'download.default_directory': 'A:\download_csv'}
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(executable_path=r'A:\Git\clone\drivers\chromedriver.exe', chrome_options=chrome_options)
    driver.implicitly_wait(5)
    driver.set_page_load_timeout(5)
    driver.get("https://uss-dev-01.pyxus.local/inventory/")
    wait = WebDriverWait(driver, 5)


    def close(self):
        self.driver.quit()