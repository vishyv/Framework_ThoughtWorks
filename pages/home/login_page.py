from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
import time


class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"

    # element interactions

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")

    def login(self, email="", password=""):
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("search_box")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Home Page")