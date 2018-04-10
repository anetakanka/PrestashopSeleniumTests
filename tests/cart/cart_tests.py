from base.selenium_driver import SeleniumDriver
from pages.cart_page.cart_page import CartPage
from utilities.teststatus import TestStatus
from pages.home_page.navigation import NavigationPage
from pages.home_page.login_page import LoginPage
import unittest
import pytest
import utilities.custom_logger as cl
import logging

@pytest.mark.usefixtures('oneTimeSetUp', 'setUp')
class CartTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.cp = CartPage(self.driver)
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)
        self.sd = SeleniumDriver(self.driver)

    @pytest.mark.run(order=1)
    def test_fewProductsCartSuccessful(self):
        self.log.info("Get few products to cart successful")
        result = self.cp.getFewProductsToCartSuccessful(quantity=2)
        assert result == True

    @pytest.mark.run(order=2)
    def test_priceOfProductsSuccessful(self):
        self.log.info("Price of products in cart page successful")
        self.nav.clearCartandGoToMainPage()
        result = self.cp.priceOfProductsInBasket(quantity=2)
        assert result == True

    @pytest.mark.run(order=3)
    def test_deleteFromCartSuccessful(self):
        self.log.info("Delete from cart successful")
        self.nav.clearCartandGoToMainPage()
        result = self.cp.deleteFromCart()
        assert result == True

    @pytest.mark.run(order=4)
    def test_changeQuantitySuccessful(self):
        self.log.info("Change quantity of products in cart successful")
        self.nav.clearCartandGoToMainPage()
        result = self.cp.changeQuantity()
        assert result == True
        self.ts.markFinal("test_changeQuantitySuccessful", result, "Changed quantity of products in cart Successful "
                                                                  "verification SUCCESSED")
