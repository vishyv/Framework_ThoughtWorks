import traceback
from selenium import webdriver


class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):
        baseURL = "https://testsite.com/"
        if self.browser == "iexplorer":
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox(executable_path="D:\\Python\\drivers\\geckodriver.exe")
        elif self.browser == "chrome":
            driver = webdriver.Chrome(executable_path="D:\\Python\\drivers\\chromedriver.exe")
        else:
            driver = webdriver.Chrome()
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseURL)
        return driver
