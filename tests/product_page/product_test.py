from pages.product_page.product_page import ProductPage
from utilities.teststatus import TestStatus
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.products = ProductPage(self.driver)
        self.ts = TestStatus(self.driver)

    def test_productAddition(self):
        self.products.searchBox("item")
        self.products.selectProductQty()
        self.products.clickCheckOut()

    def test_checkoutSuccess(self):
        result = self.products.verifyCart()
        self.ts.markFinal("test_checkoutSuccess", result, "Checkout successful")