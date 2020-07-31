from pages.check_out.checkout_page import CheckoutPage
from utilities.teststatus import TestStatus
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class CheckoutTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetup):
        self.checkout = CheckoutPage(self.driver)
        self.ts = TestStatus(self.driver)

    def test_CheckOut(self):
        self.checkout.enterCustomerDetails()

    def test_FinalCheckout(self):
        result = self.checkout.checkoutSuccess()
        self.ts.markFinal("test_FinalCheckout", result, "Checked out")
