from pages.home_page.search_page import productSearch
from pages.home_page.navigation import NavigationPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging
from ddt import ddt, data, unpack
from utilities.read_cvs_data import getCSVData


@pytest.mark.usefixtures('oneTimeSetUp', 'setUp')
@ddt
class SearchTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.sp = productSearch(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    @pytest.mark.run(order=1)
    @data(*getCSVData("textSearchSuccessful.csv"))
    @unpack
    def test_searchByNumSuccessful(self, text, numindatabase):
        self.log.info("Test successful text search on the home page")
        self.nav.backToHomePage()
        self.sp.searchProductsByText(text)
        result = self.sp.searchSuccesfulByNum(numindatabase)
        assert result == True

    @pytest.mark.run(order=2)
    @data(*getCSVData("textSearchByNum.csv"))
    @unpack
    def test_searchByTextSuccessful(self, text):
        self.log.info("Test successful text search on the home page")
        self.nav.backToHomePage()
        self.sp.searchProductsByText(text)
        result = self.sp.searchSuccessfulByText(text)
        assert result == True


    @pytest.mark.run(order=3)
    @data(*getCSVData("textSearchFailed.csv"))
    @unpack
    def test_searchByTextFailed(self,text):
        self.log.info("Test failed text search on the home page")
        self.nav.backToHomePage()
        self.sp.searchProductsByText(text)
        result = self.sp.searchFailed()
        assert result == True
        self.ts.markFinal("test_searchByTextFailed", result, "Text search on the home page verification SUCCESSED")

