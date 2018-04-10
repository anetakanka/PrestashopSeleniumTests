from pages.clothes_page.discounts_page import DiscountsPage
from utilities.teststatus import TestStatus
from pages.home_page.navigation import NavigationPage
from pages.home_page.login_page import LoginPage
import unittest
import pytest
import utilities.custom_logger as cl
import logging

@pytest.mark.usefixtures('oneTimeSetUp', 'setUp')
class DiscountTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.dp = DiscountsPage(self.driver)
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    @pytest.mark.run(order=1)
    def test_discountforloggedInSuccesfull(self):
        self.log.info("Test discount for logged in client successful")
        result = self.dp.discountForLoggedInClientSuccessful(email="test@test.com", password="abcabc123", discountnum=0.2)
        assert result == True

    @pytest.mark.run(order=2)
    def test_discountforloggedInFailed(self):
        self.log.info("Test discount for logged in client successful failed")
        result = self.dp.discountForLoggedInClientFailed()
        assert result == False

    @pytest.mark.run(order=3)
    def test_discountInfoClothesPage(self):
        self.log.info("Test discount info for logged in client on element on clothes page")
        result = self.dp.discountInfoOnClothesPageElements(email="test@test.com", password="abcabc123", elementNum=35)
        assert result == True
        self.ts.markFinal("test_discountInfoClothesPage", result, "Discounts for logged in and logout clients "
                                                                  "verification SUCCESSED")

