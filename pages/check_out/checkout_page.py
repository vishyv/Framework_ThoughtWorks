from base.basepage import BasePage
import utilities.custom_logger as cl
import logging


class CheckoutPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators:
    _cu_name = 'name'
    _cu_mobile = "mobile"
    _cu_address = "address"
    _pay_option = "type_paytm"
    _submit = "submit"
    _checkout_success = "success_msg"

    # element interactions

    def enterCustomerName(self, name):
        self.sendKeys(name, locator=self._cu_name)

    def enterCustomerMobile(self, number):
        self.sendKeys(number, locator=self._cu_mobile)

    def enterCustomerAddress(self, address):
        self.sendKeys(address, locator=self._cu_address)

    def payOption(self):
        self.elementClick(locator=self._submit)

    def enterCustomerDetails(self, name, number, address):
        self.enterCustomerName(name)
        self.enterCustomerMobile(number)
        self.enterCustomerAddress(address)
        self.payOption()

    def checkoutSuccess(self):
        result = self.isElementPresent(locator=self._checkout_success)
        return result
