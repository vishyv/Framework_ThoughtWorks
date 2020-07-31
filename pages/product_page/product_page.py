from base.basepage import BasePage
import utilities.custom_logger as cl
import logging


class ProductPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators:
    _search_box = 'search_product_page'
    _search_item_icon = "search_icon"
    _quantity_addition = "add_quantity"
    _check_out = "check_out"
    _checkout_success = "checkout successful"

    # Element Interactions

    def searchBox(self, product):
        self.sendKeys(product, self._search_box)
        self.elementClick(locator=self._search_item_icon)

    def selectProductQty(self):
        self.elementClick(locator=self._quantity_addition)

    def clickCheckOut(self):
        self.elementClick(locator=self._check_out)

    def verifyCart(self):
        result = self.isElementPresent(locator=self._checkout_success)
        return result