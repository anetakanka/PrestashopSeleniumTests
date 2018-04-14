from pages.clothes_page.filters_page import FiltersPage
from utilities.teststatus import TestStatus
from pages.home_page.navigation import NavigationPage
import unittest
import pytest
import utilities.custom_logger as cl
import logging


@pytest.mark.usefixtures('oneTimeSetUp', 'setUp')
class FiltersTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.fp = FiltersPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    @pytest.mark.run(order=1)
    def test_goToMenPage(self):
        self.log.info("Test go to men page successful")
        result = self.fp.goToMenPageSuccessful()
        assert result == True

    @pytest.mark.run(order=2)
    def test_collapseMenu(self):
        self.log.info("Test collapse menu women successful")
        self.fp.collapseMenuWomenBlouse()
        result = self.fp.clothesWomenBluzkiPage()
        assert result == True

    @pytest.mark.run(order=3)
    def test_hoverOverMenu(self):
        self.log.info("Test hover over menu clothes women successful")
        self.fp.clothesPagehoverOverMenu()
        result = self.fp.clothesWomenBluzkiPage()
        assert result == True

    @pytest.mark.run(order=4)
    def test_multiFilters(self):
        self.log.info("Multiple clothes used successful")
        self.fp.multipleFiltersClick()
        result = self.fp.multipleFiltersSuccessful()
        assert result == True
        self.ts.markFinal("test_multiFilters", result, "Multiple clothes use verification SUCCESSED")

